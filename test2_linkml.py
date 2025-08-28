from typing import List
from dash.html import Sub
import models.shared
import flask
from flask import jsonify
import os
from pathlib import Path
from sqlalchemy import select, and_

# from models.metadata import Book, Author, Document, File, Submission, Submitter
from models.linkml.models import (
    Base,
    DashboardUser,
    Organization,
    Person,
    MetadataRole,
    OadsMetadata,
    File,
    RelatedDataset,
    Address,
    ContactInformation,
    Submission,
)

import constants

from sqlalchemy.orm import Session

from pydantic import ValidationError

db = models.shared.db
server = flask.Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:docker@127.0.0.1:5432"
)
server.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
db.init_app(server)

with server.app_context():
    Base.metadata.create_all(bind=constants.postgres_engine)

# book1 = Book(title="A Good Book")
# book2 = Book(title="A Better Book")
# author = Author(name="Joe Blow", books=[book1, book2])

with Session(constants.postgres_engine) as session:
    stmt = select(MetadataRole).where(MetadataRole.name=='Data Submitter')
    data_submitter_role = session.scalars(stmt).one()
    stmt2 = select(MetadataRole).where(MetadataRole.name=='Investigator')
    investigator_role = session.scalars(stmt2).one()
    ustmt = select(DashboardUser).where(DashboardUser.email=='roland.schweitzer@noaa.gov')
    user = session.scalars(ustmt).one()
    data_submitter_person = session.scalars(select(Person).where(and_((Person.first_name=='Jane'),(Person.last_name=='Explorer')))).one()                    
    investigator_person1 = session.scalars(select(Person).where(and_((Person.first_name=='Joyce'),(Person.last_name=='Experimenter')))).one()
    investigator_person2 = session.scalars(select(Person).where(and_((Person.first_name=='Bill'),(Person.last_name=='Labworker')))).one()

    print('Dashboard users id', user.id, 'Dashboard user email', user.email)
    print('with', len(user.submissions), 'submissions.')
    submission = Submission(
        files=[
            File(filename="data1.csv", category="data", mime="text/csv"),
            File(filename="more1.nc", mime="application/netcdf", category="data"),
        ],
        oads_metadata=[OadsMetadata(
            data_license="https://wiki.creativecommons.org/wiki/PDM_FAQ",  # What should this be
            title="More Great Data from the Agriculture and Commerce State",
            abstract="""An investigation of something else.""",
            related_datasets=[
                RelatedDataset(
                    dataset="NYC Cab Trip Records",
                    link="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
                ),
                RelatedDataset(
                    dataset="2024 TPOS Drone 1033",
                    link="https://data.pmel.noaa.gov/pmel/erddap/tabledap/sd1033_tpos_2024.html",
                ),
            ],
            investigators=[
                investigator_person1,
                investigator_person2
            ],
            data_submitters=[
                data_submitter_person
            ]
        )],
    )
    user.submissions.append(submission)
    session.commit()
    session.refresh(user)

    Path(os.path.join(constants.UPLOAD_DIRECTORY, str(user.submissions[0].id))).mkdir(
        parents=True, exist_ok=True
    )
    with open(f"{constants.UPLOAD_DIRECTORY}/{user.submissions[0].id}/data1.csv", "w") as f:
        f.write("lat,lon,time,sst\n45.0,0.0,2024-01-01:00:00:00,35.6")

    with open(f"{constants.UPLOAD_DIRECTORY}/{user.submissions[0].id}/more1.nc", "w") as f:
        f.write("netCDF")

    user2 = DashboardUser(email='joe.science@noaa.gov')
    victoria = Person(
        first_name="Victoria",
        last_name="Atmos",
        organizations=[
            Organization(
                organization_identifier="https://ror.org/01g9vbr38",
                organization_identifier_type="ror",
                name="Oklahoma State University"
            )
        ],
        contact_information=[ContactInformation(
            email="victoria@okstate.edu",
            link="https://go.okstate.edu/undergraduate-academics/majors/environmental-science.html",
            address=[Address(
                delivery_points=[
                    "Oklahoma State University"
                ],
                city="Stillwater",
                administrative_area="OK",
                postal_code="74078",
            )],
        )],
        metadata_role=[investigator_role],
    )
    odelia = Person(
        first_name="Odelia",
        last_name="Iceberg",
        organizations=[
            Organization(
                organization_identifier="https://ror.org/05p1j8758",
                organization_identifier_type="ror",
                name="Kansas State University"
            )
        ],
        contact_information=[ContactInformation(
            email="odelia@k-state.edu",
            link="https://www.k-state.edu/environmental-science/",
            address=[Address(
                delivery_points=[
                    "College of Arts and Sciences 009G Calvin Hall",
                    "802 Mid Campus Dr South"
                ],
                city="Manhattan",
                administrative_area="KS",
                postal_code="66506-0121",
            )],
        )],
        metadata_role=[investigator_role],
    )
    ellie =  Person(first_name="Ellie",
            last_name="O'Donnel",
            organizations=[
                Organization(organization_identifier="https://ror.org/03xrrjk67", organization_identifier_type="ror", name="University of Alabama"),
                Organization(name="Eastern Pipefitters Local 1138")
            ],
            contact_information=[ContactInformation(
                email="ellieo@ua.edu",
                link="https://geography.ua.edu/research/earth-system-science/",
                address=[Address(
                    delivery_points=[
                        "Department of Geography",
                        "The University of Alabama",
                        "Box 870322"
                    ],
                    city="Tuscaloosa",
                    administrative_area="AL",
                    postal_code="35401-0322",
                )],
            )],
            metadata_role=[data_submitter_role]
    )
    user2.people = [victoria, odelia, ellie]
    submission = Submission(
                files=[
                    File(filename="data3.csv", category="data", mime="text/csv"),
                    File(filename="more3.nc", mime="application/netcdf", category="data"),
                ],
                oads_metadata=[OadsMetadata(
                    data_license="https://wiki.creativecommons.org/wiki/PDM_FAQ",  # What should this be
                    title="Joe has made some data",
                    abstract="""A great number of data items were created and then studied and then made public.""",
                    related_datasets=[
                        RelatedDataset(
                            dataset="GOES-17",
                            link="https://console.cloud.google.com/marketplace/product/noaa-public/goes-17?project=aw-8a5d408d-02e1-4907-9163-b4d",
                        ),
                    ],
                    investigators=[
                        victoria, odelia
                    ],
                    data_submitters=[
                        ellie       
                    ]
                )],
            )
  
    user2.submissions = [submission]

    session.add(user2)
    session.commit()
    session.refresh(user2)

    Path(os.path.join(constants.UPLOAD_DIRECTORY, str(user.submissions[0].id))).mkdir(
        parents=True, exist_ok=True
    )
    with open(f"{constants.UPLOAD_DIRECTORY}/{user.submissions[0].id}/data3.csv", "w") as f:
        f.write("lat,lon,time,sst\n45.0,0.0,2024-01-01:00:00:00,35.6")

    with open(f"{constants.UPLOAD_DIRECTORY}/{user.submissions[0].id}/more3.nc", "w") as f:
        f.write("netCDF")
#     # print(json.dumps(om, cls=CustomJSONEncoder, indent=4))
#     print(
#         "first name of investigator:", user.submissions[0].investigators[0].first_name
#     )
#     if DashboardUserSchema.model_validate(user):
#         user_schema = DashboardUserSchema.from_orm(user)
#         print(
#             user_schema.model_dump_json(
#                 indent=4, exclude_defaults=True, exclude_none=True
#             )
#         )
