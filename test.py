import models.shared
import os
import flask
from pathlib import Path
from sqlalchemy import select

# from models.metadata import Book, Author, Document, File, Submission, Submitter
from models.sqlalchemy.models import (
    Base,
    DashboardUser,
    Organization,
    Person,
    DashboardUserSchema,
    MetadataRole,
    OadsMetadata,
    File,
    RelatedDataset,
    Address,
    ContactInformation,
    OadsMetadataSchema,
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
    user = DashboardUser(email='roland.schweitzer@noaa.gov')
    submission = Submission(
                files=[
                    File(filename="data.csv", category="data", mime="text/csv"),
                    File(filename="more.nc", mime="application/netcdf", category="data"),
                ],
                oads_metadata=OadsMetadata(
                    data_license="https://wiki.creativecommons.org/wiki/PDM_FAQ",  # What should this be
                    title="Some Great Data from the Agriculture and Commerce State",
                    abstract="""An investigation of the potential environmental and health impacts in the immediate aftermath of one of the largest coal ash \
    spills in U.S. history at the Tennessee Valley Authority (TVA) Kingston coal-burning power plant has revealed three major \
    findings. First, the surface release of coal ash with high levels of toxic elements (As = 75 mg/kg; Hg = 150 μg/kg) \
    and radioactivity (226Ra + 228Ra = 8 pCi/g) to the environment has the potential to generate resuspended ambient \
    fine particles (<10 μm) containing these toxics into the atmosphere that may pose a health risk to local communities. \
    Second, leaching of contaminants from the coal ash caused contamination of surface waters in areas of restricted water exchange, \
    but only trace levels were found in the downstream Emory and Clinch Rivers due to river dilution. Third, the \
    accumulation of Hg- and As-rich coal ash in river sediments has the potential to have an impact on the ecological system \
    in the downstream rivers by fish poisoning and methylmercury formation in anaerobic river sediments.""",
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
                        Person(
                            first_name="Sally",
                            last_name="Scientist",
                            dashboard_user = user,
                            organizations=[
                                Organization(
                                    ror_id="https://ror.org/05rfqv493",
                                    name="East Tennessee State University",
                                ),
                                Organization(
                                    name="Association of Concerned Scientists"
                                )
                            ],
                            contact_information=ContactInformation(
                                email="sally@etsu.edu",
                                link="https://www.etsu.edu/cas/geosciences/programs/degrees.php",
                                address=Address(
                                    delivery_points=[
                                        "Ross Hall 307",
                                        "Corner of Smith and Jones"
                                    ],
                                    city="Johnson City",
                                    administrative_area="TN",
                                    postal_code="37614",
                                ),
                            ),
                            metadata_roles=[investigator_role],
                        ),
                        Person(
                            first_name="Jane",
                            last_name="Explorer",
                            dashboard_user = user,
                            organizations=[
                                Organization(
                                    ror_id="https://ror.org/01s7b5y08",
                                    name="University of South Alabama"
                                )
                            ],
                            contact_information=ContactInformation(
                                email="jane@southalabama.edu",
                                link="https://www.southalabama.edu/colleges/artsandsci/earthsci/meteorology/",
                                address=Address(
                                    delivery_points=[
                                        "ELSB 136",
                                        "100 Cool Street"
                                    ],
                                    city="Mobile",
                                    administrative_area="AL",
                                    postal_code="36688",
                                ),
                            ),
                            metadata_roles=[investigator_role],
                        ),
                        Person(
                            first_name="Joyce",
                            last_name="Experimenter",
                            dashboard_user = user,
                            organizations=[
                                Organization(
                                    ror_id="https://ror.org/02s1t7068",
                                    name="Eastern Oklahoma State College"
                                )
                            ],
                            contact_information=ContactInformation(
                                email="sally@eosc.edu",
                                link="https://www.eosc.edu/",
                                address=Address(
                                    delivery_points=[
                                        "1301 W. Main St."
                                    ],
                                    city="Wilburton",
                                    administrative_area="OK",
                                    postal_code="74578",
                                ),
                            ),
                            metadata_roles=[investigator_role],
                        )
                    ],
                    data_submitter=[
                            Person(first_name="Bill",
                                last_name="Labworker",
                                dashboard_user = user,
                                organizations=[
                                    Organization(
                                        ror_id="https://ror.org/05rfqv493",
                                        name="East Tennessee State University"
                                    ),
                                    Organization(
                                        ror_id="https://ror.org/03xrrjk67",
                                        name="University of Alabama"
                                    ),
                                    Organization(
                                        name="A&M Consolidated High School"
                                    )
                                ],
                                contact_information=ContactInformation(
                                    email="bill@etsu.edu",
                                    link="https://www.etsu.edu/cas/geosciences/programs/degrees.php",
                                    address=Address(
                                        delivery_points=[
                                            "Ross Hall 307"
                                        ],
                                        city="Johnson City",
                                        administrative_area="TN",
                                        postal_code="37614",
                                    ),
                                ),
                                metadata_roles=[data_submitter_role]
                        ),
                    ]
                ),
            )
  
    user.submissions = [submission]

    session.add(user)
    session.commit()
    session.refresh(user)

    Path(os.path.join(constants.UPLOAD_DIRECTORY, str(user.submissions[0].id))).mkdir(
        parents=True, exist_ok=True
    )
    with open(f"{constants.UPLOAD_DIRECTORY}/{user.submissions[0].id}/data.csv", "w") as f:
        f.write("lat,lon,time,sst\n45.0,0.0,2024-01-01:00:00:00,35.6")

    with open(f"{constants.UPLOAD_DIRECTORY}/{user.submissions[0].id}/more.nc", "w") as f:
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
