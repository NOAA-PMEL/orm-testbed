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


class MetadataDocument(Base):
    __tablename__ = "metadata_document"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    submit_time: Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now())
    responsible_party_id: Mapped[PG_UUID] = mapped_column(ForeignKey("organization_ref.id"), default=None)
    data_submitter_id: Mapped[PG_UUID] = mapped_column(ForeignKey("person_ref.id"), default=None)
    researchers: Mapped[List["PersonRef"]] = relationship("PersonRef", back_populates="metadata_document", foreign_keys="PersonRef.metadata_document_id", default_factory=list)
    variables: Mapped[List["Variable"]] = relationship("Variable", back_populates="metadata_document", foreign_keys="Variable.metadata_document_id", default_factory=list)
    people: Mapped[List["PersonInstance"]] = relationship("PersonInstance", back_populates="metadata_document", foreign_keys="PersonInstance.metadata_document_id", default_factory=list)
    organizations: Mapped[List["OrganizationInstance"]] = relationship("OrganizationInstance", back_populates="metadata_document", foreign_keys="OrganizationInstance.metadata_document_id", default_factory=list)


class ElementRefMixIn():
    description: Mapped[Optional[String]] = mapped_column(String, default=None)
    role: Mapped[Optional[String]] = mapped_column(String, default=None)
    object_id: Mapped[Optional[String]] = mapped_column(String, default=None)


class PersonRef(Base, ElementRefMixIn):
    __tablename__ = "person_ref"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    metadata_document_id: Mapped[Optional[PG_UUID]] = mapped_column(PG_UUID, ForeignKey("metadata_document.id"), default=None)
    metadata_document: Mapped[Optional["MetadataDocument"]] = relationship("MetadataDocument", back_populates="researchers", foreign_keys=[metadata_document_id], default=None)


class OrganizationRef(Base, ElementRefMixIn):
    __tablename__ = "organization_ref"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())


class ElementInstanceMixIn():
    object_id: Mapped[Optional[String]] = mapped_column(String, default=None)


class PersonMixIn(ElementInstanceMixIn):
    pass


class PersonBaseMixIn(PersonMixIn):
    PID: Mapped[Optional[String]] = mapped_column(String, default=None)


class OrganizationMixIn(ElementInstanceMixIn):
    pass


class PersonInstance(Base, PersonBaseMixIn):
    __tablename__ = "person_instance"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    first_name: Mapped[Optional[String]] = mapped_column(String, default=None)
    last_name: Mapped[Optional[String]] = mapped_column(String, default=None)
    address: Mapped[Optional[String]] = mapped_column(String, default=None)
    organization_id: Mapped[PG_UUID] = mapped_column(ForeignKey("organization_ref.id"), default=None)
    metadata_document_id: Mapped[Optional[PG_UUID]] = mapped_column(PG_UUID, ForeignKey("metadata_document.id"), default=None)
    metadata_document: Mapped[Optional["MetadataDocument"]] = relationship("MetadataDocument", back_populates="people", foreign_keys=[metadata_document_id], default=None)


class OrganizationBaseMixIn(OrganizationMixIn):
    PID: Mapped[Optional[String]] = mapped_column(String, default=None)


class OrganizationInstance(Base, OrganizationBaseMixIn):
    __tablename__ = "organization_instance"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    name: Mapped[Optional[String]] = mapped_column(String, default=None)
    description: Mapped[Optional[String]] = mapped_column(String, default=None)
    metadata_document_id: Mapped[Optional[PG_UUID]] = mapped_column(PG_UUID, ForeignKey("metadata_document.id"), default=None)
    metadata_document: Mapped[Optional["MetadataDocument"]] = relationship("MetadataDocument", back_populates="organizations", foreign_keys=[metadata_document_id], default=None)


class VariableMixIn():
    name: Mapped[Optional[String]] = mapped_column(String, default=None)
    standard_name: Mapped[Optional[String]] = mapped_column(String, default=None)
    description: Mapped[Optional[String]] = mapped_column(String, default=None)
    dataset_variable_name: Mapped[Optional[String]] = mapped_column(String, default=None)
    units: Mapped[Optional[String]] = mapped_column(String, default=None)


class Variable(Base, VariableMixIn):
    __tablename__ = "variable"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    name: Mapped[Optional[String]] = mapped_column(String, default=None)
    standard_name: Mapped[Optional[String]] = mapped_column(String, default=None)
    description: Mapped[Optional[String]] = mapped_column(String, default=None)
    dataset_variable_name: Mapped[Optional[String]] = mapped_column(String, default=None)
    units: Mapped[Optional[String]] = mapped_column(String, default=None)
    metadata_document_id: Mapped[Optional[PG_UUID]] = mapped_column(PG_UUID, ForeignKey("metadata_document.id"), default=None)
    metadata_document: Mapped[Optional["MetadataDocument"]] = relationship("MetadataDocument", back_populates="variables", foreign_keys=[metadata_document_id], default=None)
    variable_type: Mapped[String] = mapped_column(String, default=None)
    __mapper_args__ = {
        "polymorphic_on": "variable_type",
        "polymorphic_identity": "base"
    }


class TaVariable(Variable):
    __tablename__ = "ta_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    cellType: Mapped[Optional[String]] = mapped_column(String, default=None)
    curveFitting: Mapped[Optional[String]] = mapped_column(String, default=None)
    blankCorrection: Mapped[Optional[String]] = mapped_column(String, default=None)
    __mapper_args__ = {
        "polymorphic_identity": "ta_variable"
    }


class PhVariable(Variable):
    __tablename__ = "ph_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    phScale: Mapped[Optional[String]] = mapped_column(String, default=None)
    measurement_temperature: Mapped[Optional[String]] = mapped_column(String, default=None)
    temperature_correction_method: Mapped[Optional[String]] = mapped_column(String, default=None)
    ph_report_temperature: Mapped[Optional[String]] = mapped_column(String, default=None)
    __mapper_args__ = {
        "polymorphic_identity": "ph_variable"
    }


class Co2VariableMixIn():
    gasDetector: Mapped[Optional[String]] = mapped_column(String, default=None)
    waterVaporCorrection: Mapped[Optional[String]] = mapped_column(String, default=None)
    temperatureCorrectionMethod: Mapped[Optional[String]] = mapped_column(String, default=None)
    co2ReportTemperature: Mapped[Optional[String]] = mapped_column(String, default=None)


class Co2Variable(Variable, Co2VariableMixIn):
    __tablename__ = "co2_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    gasDetector: Mapped[Optional[String]] = mapped_column(String, default=None)
    waterVaporCorrection: Mapped[Optional[String]] = mapped_column(String, default=None)
    temperatureCorrectionMethod: Mapped[Optional[String]] = mapped_column(String, default=None)
    co2ReportTemperature: Mapped[Optional[String]] = mapped_column(String, default=None)
    __mapper_args__ = {
        "polymorphic_identity": "co2_variable"
    }


class Co2Autonomous(Co2Variable):
    __tablename__ = "co2_autonomous"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("co2_variable.id"), primary_key=True, default=func.gen_random_uuid())
    locationSeawaterIntake: Mapped[Optional[String]] = mapped_column(String, default=None)
    depthSeawaterIntake: Mapped[Optional[String]] = mapped_column(String, default=None)
    equilibrator: Mapped[Optional[String]] = mapped_column(String, default=None)
    __mapper_args__ = {
        "polymorphic_identity": "co2_autonomous"
    }


class Co2Discrete(Co2Variable):
    __tablename__ = "co2_discrete"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("co2_variable.id"), primary_key=True, default=func.gen_random_uuid())
    storageMethod: Mapped[Optional[String]] = mapped_column(String, default=None)
    seawaterVolume: Mapped[Optional[String]] = mapped_column(String, default=None)
    headspaceVolume: Mapped[Optional[String]] = mapped_column(String, default=None)
    measurementTemperature: Mapped[Optional[String]] = mapped_column(String, default=None)
    __mapper_args__ = {
        "polymorphic_identity": "co2_discrete"
    }


