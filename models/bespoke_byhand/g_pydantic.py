import uuid
import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Union, Literal, Annotated

# ====================================================================
# 1. Schemas for Core Entities (Person, Organization)
# ====================================================================
# These are defined first but have forward references ("OrganizationSchema")
# We will resolve these references at the end.

class OrganizationSchemaBase(BaseModel):
    """
    Pydantic schema for reading an Organization.
    """
    # Tell Pydantic to read from object attributes (SQLAlchemy model)
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: Optional[str] = None
    description: Optional[str] = None
    PID: Optional[str] = None

class OrganizationSchema(OrganizationSchemaBase):
    people: List["PersonSchemaBase"] = []


class PersonSchemaBase(BaseModel):
    """
    Pydantic schema for reading a Person.
    """
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    PID: Optional[str] = None


class PersonSchema(PersonSchemaBase):
    organizations: List[OrganizationSchemaBase] = []


# ====================================================================
# 2. Schemas for Association Objects (PersonRef, OrganizationRef)
# ====================================================================
# These link models include their own data (role, description)
# and also link to the full Person/Organization object.

class PersonRefSchema(BaseModel):
    """
    Pydantic schema for the PersonRef association object.
    Includes the nested Person.
    """
    model_config = ConfigDict(from_attributes=True)

    metadata_document_id: uuid.UUID
    person_id: uuid.UUID
    role: str
    description: str
    
    # This corresponds to the 'person_' relationship with lazy="joined"
    person: PersonSchema


class ResponsiblePartySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    organization_id: uuid.UUID
    role: str
    description: str


class OrganizationRefSchema(BaseModel):
    """
    Pydantic schema for the OrganizationRef association object.
    Includes the nested Organization.
    """
    model_config = ConfigDict(from_attributes=True)

    metadata_document_id: uuid.UUID
    organization_id: uuid.UUID
    role: str
    description: str
    
    # This corresponds to the 'organization' relationship with lazy="joined"
    organization: OrganizationSchema


# ====================================================================
# 3. Schemas for Polymorphic Variables
# ====================================================================

# This is the Pydantic *base* class. It contains all common fields.
class VariableBaseSchema(BaseModel):
    """
    Pydantic base schema for all Variable types.
    """
    model_config = ConfigDict(from_attributes=True)
    
    id: uuid.UUID
    name: Optional[str] = None
    standard_name: Optional[str] = None
    description: Optional[str] = None
    dataset_variable_name: Optional[str] = None
    units: Optional[str] = None
    metadata_document_id: Optional[uuid.UUID] = None
    # Note: 'variable_type' is defined in the subclasses as the discriminator


# --- Concrete Variable Subclasses ---

class VariableSchema(VariableBaseSchema):
    """ Schema for the 'base' polymorphic identity """
    variable_type: Literal["base"]


class TaVariableSchema(VariableBaseSchema):
    """ Schema for the 'ta_variable' polymorphic identity """
    variable_type: Literal["ta_variable"]
    cellType: Optional[str] = None
    curveFitting: Optional[str] = None
    blankCorrection: Optional[str] = None


class PhVariableSchema(VariableBaseSchema):
    """ Schema for the 'ph_variable' polymorphic identity """
    variable_type: Literal["ph_variable"]
    phScale: Optional[str] = None
    measurement_temperature: Optional[str] = None
    temperature_correction_method: Optional[str] = None
    ph_report_temperature: Optional[str] = None


# --- CO2 Variable Hierarchy ---

class Co2VariableBaseSchema(VariableBaseSchema):
    """
    A Pydantic base for CO2 variables, containing shared fields
    from the 'co2_variable' SQLAlchemy model.
    """
    gasDetector: Optional[str] = None
    waterVaporCorrection: Optional[str] = None
    temperatureCorrectionMethod: Optional[str] = None
    co2ReportTemperature: Optional[str] = None


class Co2VariableSchema(Co2VariableBaseSchema):
    """ Schema for the 'co2_variable' polymorphic identity """
    variable_type: Literal["co2_variable"]


class Co2AutonomousSchema(Co2VariableBaseSchema):
    """ Schema for the 'co2_autonomous' polymorphic identity """
    variable_type: Literal["co2_autonomous"]
    locationSeawaterIntake: Optional[str] = None
    depthSeawaterIntake: Optional[str] = None
    equilibrator: Optional[str] = None


class Co2DiscreteSchema(Co2VariableBaseSchema):
    """ Schema for the 'co2_discrete' polymorphic identity """
    variable_type: Literal["co2_discrete"]
    storageMethod: Optional[str] = None
    seawaterVolume: Optional[str] = None
    headspaceVolume: Optional[str] = None
    measurementTemperature: Optional[str] = None


# --- Tagged Union for all Variable types ---

# This Union tells Pydantic to validate against one of the following models
# based on the value of the 'variable_type' field.
AnyVariable = Annotated[
    Union[
        VariableSchema,
        TaVariableSchema,
        PhVariableSchema,
        Co2VariableSchema,
        Co2AutonomousSchema,
        Co2DiscreteSchema
    ],
    Field(discriminator="variable_type")
]


# ====================================================================
# 4. Main MetadataDocument Schema
# ====================================================================

class MetadataDocumentSchema(BaseModel):
    """
    Pydantic schema for the main MetadataDocument.
    """
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    submit_time: Optional[datetime.datetime] = None
    
    # Relationships based on roles
    # responsible_party: Optional[OrganizationRefSchema] = None
    responsible_party: Optional[ResponsiblePartySchema] = None
    data_submitter: Optional[PersonRefSchema] = None
    researchers: List[PersonRefSchema] = []
    
    # Polymorphic variables
    variables: List[AnyVariable] = []
    
    # Full lists of all associated people/orgs
    people: List[PersonRefSchema] = []
    organizations: List[OrganizationRefSchema] = []


# ====================================================================
# 5. Resolve All Forward References
# ====================================================================
# This is a crucial step! It allows Pydantic models to
# refer to each other before they are all fully defined.

PersonSchema.model_rebuild()
OrganizationSchema.model_rebuild()
PersonRefSchema.model_rebuild()
OrganizationRefSchema.model_rebuild()
MetadataDocumentSchema.model_rebuild()