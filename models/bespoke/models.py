from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, relationship, Mapped, mapped_column
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from sqlalchemy import func

from typing import List, Optional

class Base(MappedAsDataclass, DeclarativeBase):
    pass

class Metadata(Base):
    __tablename__ = "metadata"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())

    def __repr__(self):
        return f"<Metadata(id='{self.id}')>"

class MetadataDocument(Base):
    __tablename__ = "metadata_document"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    submit_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    responsible_party_id: Mapped[PG_UUID] = mapped_column(ForeignKey("organization_ref.id"), default=None)
    data_submitter_id: Mapped[PG_UUID] = mapped_column(ForeignKey("person_ref.id"), default=None)
    researchers: Mapped[List["PersonRef"]] = relationship("PersonRef", back_populates="metadata_document", foreign_keys="PersonRef.metadata_document_id", default_factory=list)
    variables: Mapped[List["Variable"]] = relationship("Variable", back_populates="metadata_document", foreign_keys="Variable.metadata_document_id", default_factory=list)
    people: Mapped[List["PersonInstance"]] = relationship("PersonInstance", back_populates="metadata_document", foreign_keys="PersonInstance.metadata_document_id", default_factory=list)
    organizations: Mapped[List["OrganizationInstance"]] = relationship("OrganizationInstance", back_populates="metadata_document", foreign_keys="OrganizationInstance.metadata_document_id", default_factory=list)

    def __repr__(self):
        return f"<MetadataDocument(id='{self.id}', submit_time='{self.submit_time}')>"

class ElementRefMixIn():
    description: Mapped[String] = mapped_column(String, default=None)
    role: Mapped[String] = mapped_column(String, default=None)
    object_id: Mapped[String] = mapped_column(String, default=None)

    def __repr__(self):
        return f"<ElementRef(id='{self.id}', description='{self.description}', role='{self.role}', object_id='{self.object_id}')>"

class PersonRef(Base, ElementRefMixIn):
    __tablename__ = "person_ref"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())

    def __repr__(self):
        return f"<PersonRef(id='{self.id}')>"

class OrganizationRef(Base, ElementRefMixIn):
    __tablename__ = "organization_ref"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())

    def __repr__(self):
        return f"<OrganizationRef(id='{self.id}')>"

class ElementInstanceMixIn():
    object_id: Mapped[String] = mapped_column(String, default=None)

    def __repr__(self):
        return f"<ElementInstance(id='{self.id}', object_id='{self.object_id}')>"

class ElementMixIn():
    pass

class PersonMixIn():
    pass

class PersonBaseMixIn():
    PID: Mapped[String] = mapped_column(String, default=None)

    def __repr__(self):
        return f"<PersonBase(id='{self.id}', PID='{self.PID}')>"

class OrganizationMixIn():
    pass

class PersonInstance(Base, PersonBaseMixIn):
    __tablename__ = "person_instance"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    first_name: Mapped[String] = mapped_column(String, default=None)
    last_name: Mapped[String] = mapped_column(String, default=None)
    address: Mapped[String] = mapped_column(String, default=None)
    organization_id: Mapped[PG_UUID] = mapped_column(ForeignKey("organization_ref.id"), default=None)

    def __repr__(self):
        return f"<PersonInstance(id='{self.id}', first_name='{self.first_name}', last_name='{self.last_name}', address='{self.address}')>"

class OrganizationBaseMixIn():
    PID: Mapped[String] = mapped_column(String, default=None)

    def __repr__(self):
        return f"<OrganizationBase(id='{self.id}', PID='{self.PID}')>"

class OrganizationInstance(Base, OrganizationBaseMixIn):
    __tablename__ = "organization_instance"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    name: Mapped[String] = mapped_column(String, default=None)
    description: Mapped[String] = mapped_column(String, default=None)

    def __repr__(self):
        return f"<OrganizationInstance(id='{self.id}', name='{self.name}', description='{self.description}')>"

class VariableMixIn():
    name: Mapped[String] = mapped_column(String, default=None)
    standard_name: Mapped[String] = mapped_column(String, default=None)
    description: Mapped[String] = mapped_column(String, default=None)
    dataset_variable_name: Mapped[String] = mapped_column(String, default=None)
    units: Mapped[String] = mapped_column(String, default=None)
    

class Variable(VariableMixIn):
    __tablename__ = "variable"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    variable_type: Mapped[String] = mapped_column(String, default=None)
    __mapper_args__ = {
        "polymorphic_on": "variable_type",
        "polymorphic_identity": "base"
    }

    def __repr__(self):
        return f"<Variable(id='{self.id}', name='{self.name}', standard_name='{self.standard_name}', description='{self.description}', dataset_variable_name='{self.dataset_variable_name}', units='{self.units}')>"

class TaVariable(Variable, VariableMixIn):
    __tablename__ = "ta_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    __mapper_args__ = {
        "polymorphic_identity": "ta_variable"
    }

    def __repr__(self):
        return f"<TaVariable(id='{self.id}', cellType='{self.cellType}', curveFitting='{self.curveFitting}', blankCorrection='{self.blankCorrection}')>"

class PhVariable(Variable, VariableMixIn):
    __tablename__ = "ph_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    __mapper_args__ = {
        "polymorphic_identity": "ph_variable"
    }

    def __repr__(self):
        return f"<PhVariable(id='{self.id}', phScale='{self.phScale}', measurement_temperature='{self.measurement_temperature}', temperature_correction_method='{self.temperature_correction_method}', ph_report_temperature='{self.ph_report_temperature}')>"

class Co2VariableMixIn():
    gasDetector: Mapped[String] = mapped_column(String, default=None)
    waterVaporCorrection: Mapped[String] = mapped_column(String, default=None)
    temperatureCorrectionMethod: Mapped[String] = mapped_column(String, default=None)
    co2ReportTemperature: Mapped[String] = mapped_column(String, default=None)
    

class Co2Variable(Variable, Co2VariableMixIn):
    __tablename__ = "co2_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    __mapper_args__ = {
        "polymorphic_identity": "co2_variable"
    }

    def __repr__(self):
        return f"<Co2Variable(id='{self.id}', gasDetector='{self.gasDetector}', waterVaporCorrection='{self.waterVaporCorrection}', temperatureCorrectionMethod='{self.temperatureCorrectionMethod}', co2ReportTemperature='{self.co2ReportTemperature}')>"

class Co2Autonomous(Variable, Co2VariableMixIn):
    __tablename__ = "co2_autonomous"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("co2_variable.id"), primary_key=True, default=func.gen_random_uuid())
    __mapper_args__ = {
        "polymorphic_identity": "co2_discrete"
    }

    def __repr__(self):
        return f"<Co2Autonomous(id='{self.id}', locationSeawaterIntake='{self.locationSeawaterIntake}', depthSeawaterIntake='{self.depthSeawaterIntake}', equilibrator='{self.equilibrator}')>"

class Co2Discrete(Variable, Co2VariableMixIn):
    __tablename__ = "co2_discrete"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("co2_variable.id"), primary_key=True, default=func.gen_random_uuid())
    __mapper_args__ = {
        "polymorphic_identity": "co2_discrete"
    }

    def __repr__(self):
        return f"<Co2Discrete(id='{self.id}', storageMethod='{self.storageMethod}', seawaterVolume='{self.seawaterVolume}', headspaceVolume='{self.headspaceVolume}', measurementTemperature='{self.measurementTemperature}')>"

