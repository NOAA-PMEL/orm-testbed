from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
import uuid


class MetadataSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID


class MetadataDocumentSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    submit_time: Optional[datetime] = None
    responsible_party_id: uuid.UUID
    data_submitter_id: uuid.UUID
    researchers: Optional[list["PersonRefSchema"]]
    variables: Optional[list["VariableSchema"]]
    people: Optional[list["PersonInstanceSchema"]]
    organizations: Optional[list["OrganizationInstanceSchema"]]


class ElementRefSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    description: Optional[str] = None
    role: Optional[str] = None
    object_id: Optional[str] = None


class PersonRefSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID


class OrganizationRefSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID


class ElementInstanceSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    object_id: Optional[str] = None


class ElementSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID


class PersonSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID


class PersonBaseSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    PID: Optional[str] = None


class OrganizationSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID


class PersonInstanceSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    organization_id: uuid.UUID


class OrganizationBaseSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    PID: Optional[str] = None


class OrganizationInstanceSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    name: Optional[str] = None
    description: Optional[str] = None


class VariableSchema(BaseModel):
    model_config  = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: uuid.UUID
    variable_type: str
    name: Optional[str] = None
    standard_name: Optional[str] = None
    description: Optional[str] = None
    dataset_variable_name: Optional[str] = None
    units: Optional[str] = None
    cellType: Optional[str] = None
    curveFitting: Optional[str] = None
    blankCorrection: Optional[str] = None
    phScale: Optional[str] = None
    measurement_temperature: Optional[str] = None
    temperature_correction_method: Optional[str] = None
    ph_report_temperature: Optional[str] = None
    gasDetector: Optional[str] = None
    waterVaporCorrection: Optional[str] = None
    temperatureCorrectionMethod: Optional[str] = None
    co2ReportTemperature: Optional[str] = None
    locationSeawaterIntake: Optional[str] = None
    depthSeawaterIntake: Optional[str] = None
    equilibrator: Optional[str] = None
    storageMethod: Optional[str] = None
    seawaterVolume: Optional[str] = None
    headspaceVolume: Optional[str] = None
    measurementTemperature: Optional[str] = None
