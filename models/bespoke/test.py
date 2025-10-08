from models.models import (
    MetadataDocument,
    PersonRef,
    OrganizationRef,
    PersonInstance,
    OrganizationInstance,
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

from sqlalchemy.orm import Session

server = flask.Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:docker@127.0.0.1:5432"
)
server.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
db.init_app(server)

from flask import jsonify


with server.app_context():
    Base.metadata.create_all(bind=constants.postgres_engine)

organization1 = OrganizationInstance(
    PID = 'https://ror.org/02aqsxs83',
    name='University of Oklahoma',
    description = 'Educational Institution'
)

organization2 = OrganizationInstance(
    PID = 'https://ror.org/01g9vbr38',
    name='Oklahoma State University',
    description = 'Educational Institution'
)



with Session(constants.postgres_engine) as session:
    session.add(organization1)
    session.add(organization2)
    session.commit()
    session.refresh(organization1)
    session.refresh(organization2)


organization_ref1 = OrganizationRef(
    role = 'who knows',
    description = 'whatever',
    object_id = organization1.id
)

organization_ref2 = OrganizationRef(
    role = 'data_submitter_organization',
    description = 'Data Submitter Organization',
    object_id = organization2.id
)

with Session(constants.postgres_engine) as session:
    session.add(organization_ref1)
    session.add(organization_ref2)
    session.commit()
    session.refresh(organization_ref1)
    session.refresh(organization_ref2)

person1 = PersonInstance(
    PID = 'ORCAIDxxxxx',
    first_name = "Joe",
    last_name = "Morrow",
    address = "15 E. Lewis St., Stillwater, OK, 74075",
    organization_id = organization_ref2.id
)

person2 = PersonInstance(
    PID = 'ORCAIDxxxxx',
    first_name = "Jane",
    last_name = "Brown",
    address = "12 E. Hall of Fame St., Stillwater, OK, 74075",
    organization_id = organization_ref2.id
)

person3 = PersonInstance(
    PID = 'ORCAIDxxxxx',
    first_name = "Julie",
    last_name = "Jefferies",
    address = "75 E. Monroe St., Stillwater, OK, 74075",
    organization_id = organization_ref2.id
)

with Session(constants.postgres_engine) as session:
    session.add(person1)
    session.add(person2)
    session.add(person3)
    session.commit()
    session.refresh(person1)
    session.refresh(person2)
    session.refresh(person3)

person_ref1 = PersonRef(
    object_id = person1.id,
    description="Data Submitter",
    role="data_submitter"
)

person_ref2 = PersonRef(
    object_id = person2.id,
    description="Researcher",
    role="researcher"
)

person_ref3 = PersonRef(
    object_id = person1.id,
    description="Researcher",
    role="researcher"
)

person_ref4 = PersonRef(
    object_id = person1.id,
    description="Principal Investigator",
    role="pi"
)

with Session(constants.postgres_engine) as session:
    session.add(person_ref1)
    session.add(person_ref2)
    session.add(person_ref3)
    session.add(person_ref4)
    session.commit()
    session.refresh(person_ref1)
    session.refresh(person_ref2)
    session.refresh(person_ref3)
    session.refresh(person_ref4)

# --- Example Instances ---

# 1. Variable Instance
var_instance = Variable(
    name = 'Sea Surface Temperature',
    standard_name = 'sea_surface_temperature',
    description = 'The temperature of the sea water at the surface.',
    dataset_variable_name = 'SST',
    units = 'Celsius',
    variable_type='base'
)

# 2. TaVariable Instance
ta_var_instance = TaVariable(
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

# 3. PhVariable Instance
ph_var_instance = PhVariable(
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

# 4. Co2Variable Instance
co2_var_instance = Co2Variable(
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


# 5. Co2Autonomous Instance
co2_auto_instance = Co2Autonomous(
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

# 6. Co2Discrete Instance
co2_discrete_instance = Co2Discrete(
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



metadata_document = MetadataDocument(
    responsible_party_id = organization_ref1.id,
    data_submitter_id = person_ref1.id,
    researchers = [person_ref4, person_ref2, person_ref3],
    people = [person1, person2, person3],
    organizations = [organization1, organization2],
)

with Session(constants.postgres_engine) as session:
    session.add(metadata_document)
    session.commit()
    session.flush()
    session.refresh(metadata_document)
    session.add(var_instance)
    var_instance.metadata_document = metadata_document
    var_instance.metadata_document_id = metadata_document.id
    metadata_document.variables.append(var_instance)
    session.add(ta_var_instance)
    ta_var_instance.metadata_document = metadata_document
    ta_var_instance.metadata_document_id = metadata_document.id
    metadata_document.variables.append(ta_var_instance)
    session.add(ph_var_instance)
    ph_var_instance.metadata_document = metadata_document
    ph_var_instance.metadata_document_id = metadata_document.id
    session.add(co2_var_instance)
    co2_var_instance.metadata_document = metadata_document
    co2_var_instance.metadata_document_id = metadata_document.id
    session.add(co2_auto_instance)
    co2_auto_instance.metadata_document = metadata_document
    co2_auto_instance.metadata_document_id = metadata_document.id
    session.add(co2_discrete_instance)
    co2_discrete_instance.metadata_document = metadata_document
    co2_discrete_instance.metadata_document_id = metadata_document.id
    session.commit()
    session.refresh(metadata_document)
