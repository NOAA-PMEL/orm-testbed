from models.models_association import (
    MetadataDocument,
    PersonRef,
    OrganizationRef,
    Person,
    Organization,
    Variable,
    TaVariable,
    PhVariable,
    Co2Variable,
    Co2Autonomous,
    Co2Discrete,
    Base
)

import constants
import flask
import os

from models.shared import db as db

from sqlalchemy.orm import Session, relationship

server = flask.Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:docker@127.0.0.1:5432"
)
server.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
db.init_app(server)

from flask import jsonify


with server.app_context():
    Base.metadata.create_all(bind=constants.postgres_engine)

with Session(constants.postgres_engine) as session:
    organization1 = Organization(
        PID = 'https://ror.org/02aqsxs83',
        name='University of Oklahoma',
        description = 'Educational Institution'
    )

    organization2 = Organization(
        PID = 'https://ror.org/01g9vbr38',
        name='Oklahoma State University',
        description = 'Educational Institution'
    )

 
    person1 = Person(
        PID = 'ORCAIDxxxxx',
        first_name = "Joe",
        last_name = "Morrow",
        address = "15 E. Lewis St., Norman, OK, 73019-3072",
    )

    person1.organizations.append(organization1)

    person2 = Person(
        PID = 'ORCAIDyyyyy',
        first_name = "Jane",
        last_name = "Brown",
        address = "12 E. Hall of Fame St., Stillwater, OK, 74075",
        # organization_id = organization2.id
    )

    person2.organizations.append(organization2)

    person3 = Person(
        PID = 'ORCAIDzzzzz',
        first_name = "Julie",
        last_name = "Jefferies",
        address = "75 E. Monroe St., Stillwater, OK, 74075",
    )

    person3.organizations.append(organization2)

    metadata_document = MetadataDocument()

    organization_ref1 = OrganizationRef(
        role = 'responsible_party',
        description = 'Responsible Organization',
        metadata_document=metadata_document
    )
    organization_ref1.organization = organization1

    organization_ref2 = OrganizationRef(
        role='researcher',
        description='Some Researchers work Here',
        metadata_document=metadata_document
    )
    organization_ref2.organization = organization2


    person_ref1 = PersonRef(
        description="Data Submitter",
        role="data_submitter",
        metadata_document=metadata_document,
        person=person1
    )

    person_ref11 = PersonRef(
        description="Researcher",
        role="researcher",
        metadata_document=metadata_document,
        person=person1
    )

    person_ref2 = PersonRef(
        description="Researcher",
        role="researcher",
        person=person2
    )

    person_ref3 = PersonRef(
        description="Lab Worker",
        role="worker",
        person=person3,
    )

    metadata_document.people.extend([person_ref1, person_ref2, person_ref3, person_ref11])
    metadata_document.organizations.extend([organization_ref1, organization_ref2])


    # --- Example s ---

    # 1. Variable 
    var_ = Variable(
        name = 'Sea Surface Temperature',
        standard_name = 'sea_surface_temperature',
        description = 'The temperature of the sea water at the surface.',
        dataset_variable_name = 'SST',
        units = 'Celsius',
        variable_type='base'
    )

    # 2. TaVariable 
    ta_var_ = TaVariable(
        name = 'Total Alkalinity',
        standard_name = 'sea_water_total_alkalinity',
        description = 'The total alkalinity of a seawater sample.',
        dataset_variable_name = 'TA',
        units = 'micromol/kg',
        cellType = 'Open Cell',
        curveFitting = 'Non-linear least squares',
        blankCorrection = 'Applied',
        variable_type='ta_variable'
    )

    # 3. PhVariable 
    ph_var_ = PhVariable(
        name = 'pH',
        standard_name = 'sea_water_ph_reported_on_total_scale',
        description = 'The pH of a seawater sample.',
        dataset_variable_name = 'pH_total',
        units = 'Total scale',
        phScale = 'Total',
        measurement_temperature = '25 C',
        temperature_correction_method = 'Dickson Lab Manual',
        ph_report_temperature = '25 C',
        variable_type='ph_variable'
    )

    # 4. Co2Variable 
    co2_var_ = Co2Variable(
        name = 'pCO2',
        standard_name = 'surface_partial_pressure_of_carbon_dioxide_in_air',
        description = 'Partial pressure of CO2 in air.',
        dataset_variable_name = 'pCO2_air',
        units = 'µatm',
        gasDetector = 'LI-COR 7000',
        waterVaporCorrection = 'Yes, applied',
        temperatureCorrectionMethod = 'Gordon and Jones 1973',
        co2ReportTemperature = '20 C',
        variable_type='co2_variable'
    )


    # 5. Co2Autonomous 
    co2_auto_ = Co2Autonomous(
        name = 'Autonomous pCO2',
        standard_name = 'surface_partial_pressure_of_carbon_dioxide_in_sea_water',
        description = 'Autonomous measurement of pCO2 in seawater.',
        dataset_variable_name = 'pCO2_sw',
        units = 'µatm',
        gasDetector = 'Pro-Oceanus Mini-pCO2',
        waterVaporCorrection = 'Yes',
        temperatureCorrectionMethod = 'Takahashi et al. 1993',
        co2ReportTemperature = 'In-situ',
        locationSeawaterIntake = 'Bow of ship',
        depthSeawaterIntake = '5 meters',
        equilibrator = 'Showerhead type',
        variable_type='co2_autonomous'
    )

    # 6. Co2Discrete 
    co2_discrete_ = Co2Discrete(
        name = 'Discrete pCO2',
        standard_name = 'partial_pressure_of_carbon_dioxide_in_sea_water',
        description = 'Discrete measurement of pCO2 in seawater from bottle sample.',
        dataset_variable_name = 'pCO2_bottle',
        units = 'µatm',
        gasDetector = 'GC-FID',
        waterVaporCorrection = 'Applied post-measurement',
        temperatureCorrectionMethod = 'None',
        co2ReportTemperature = '20 C',
        storageMethod = 'Mercuric chloride',
        seawaterVolume = '500 mL',
        headspaceVolume = '10 mL',
        measurementTemperature = '20 C',
        variable_type='co2_discrete'
    )

    metadata_document.variables.extend([var_, ta_var_, ph_var_, co2_var_, co2_auto_, co2_discrete_])

    session.add(metadata_document)
    session.commit()
    session.refresh(metadata_document)
