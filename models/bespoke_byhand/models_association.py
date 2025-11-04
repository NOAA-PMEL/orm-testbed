from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, and_, Table, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, relationship, Mapped, mapped_column
import uuid
import datetime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from sqlalchemy import func

from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Metadata(Base):
    __tablename__ = "metadata"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())


organization_person_table = Table(
    "organization_person_link",
    Base.metadata,
    Column("organization_id", ForeignKey("organization.id"), primary_key=True),
    Column("person_id", ForeignKey("person.id"), primary_key=True),
)


class Person(Base):
    __tablename__ = "person"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    first_name: Mapped[Optional[String]] = mapped_column(String)
    last_name: Mapped[Optional[String]] = mapped_column(String)
    address: Mapped[Optional[String]] = mapped_column(String)
    PID: Mapped[Optional[String]] = mapped_column(String)
    organizations: Mapped[List["Organization"]] = relationship(
        secondary=organization_person_table, 
        back_populates="people"
    )

class Organization(Base):
    __tablename__ = "organization"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    name: Mapped[Optional[String]] = mapped_column(String)
    description: Mapped[Optional[String]] = mapped_column(String)
    PID: Mapped[Optional[String]] = mapped_column(String)
    people: Mapped[List["Person"]] = relationship(
        secondary=organization_person_table, 
        back_populates="organizations"
    )


class PersonRef(Base):
    __tablename__ = "person_ref"
    
    # --- NEW PRIMARY KEY ---
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    
    # --- FOREIGN KEYS (no longer primary) ---
    metadata_document_id: Mapped[PG_UUID] = mapped_column(ForeignKey("metadata_document.id"))
    person_id: Mapped[PG_UUID] = mapped_column(ForeignKey("person.id"))
    
    # --- Columns for the association ---
    role: Mapped[String] = mapped_column(String) 
    description: Mapped[String] = mapped_column(String)

    # --- Relationships ---
    metadata_document: Mapped["MetadataDocument"] = relationship(
        back_populates="people",
    )
    person: Mapped["Person"] = relationship(lazy="joined")

    # --- NEW: Enforce business logic ---
    __table_args__ = (
        UniqueConstraint("metadata_document_id", "person_id", "role", name="uq_person_document_role"),
    )


class OrganizationRef(Base):
    __tablename__ = "organization_ref"
    
    # --- NEW PRIMARY KEY ---
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())

    # --- FOREIGN KEYS (no longer primary) ---
    metadata_document_id: Mapped[PG_UUID] = mapped_column(ForeignKey("metadata_document.id"))
    organization_id: Mapped[PG_UUID] = mapped_column(ForeignKey("organization.id"))
    
    # --- Columns for the association ---
    role: Mapped[String] = mapped_column(String) 
    description: Mapped[String] = mapped_column(String)

    # --- Relationships ---
    metadata_document: Mapped["MetadataDocument"] = relationship(
        back_populates="organizations",
    )
    organization: Mapped["Organization"] = relationship(lazy="joined") 

    # --- NEW: Enforce business logic ---
    __table_args__ = (
        UniqueConstraint("metadata_document_id", "organization_id", "role", name="uq_organization_document_role"),
    )


class MetadataDocument(Base):
    __tablename__ = "metadata_document"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    submit_time: Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now())
    responsible_party: Mapped[Optional["OrganizationRef"]] = relationship(
        "OrganizationRef",
        primaryjoin=and_(
            id == OrganizationRef.metadata_document_id,
            OrganizationRef.role == 'responsible_party'
        ),
        uselist=False, # <-- Makes this a single object, not a list
        lazy="selectin",
        viewonly=True
    )
    # data_submitter: Mapped["Person"] = relationship(secondary="person_ref")
    data_submitter: Mapped[Optional["PersonRef"]] = relationship(
        "PersonRef",
        primaryjoin=and_(
            id == PersonRef.metadata_document_id,
            PersonRef.role == 'data_submitter'
        ),
        uselist=False, # <-- Makes this a single object, not a list
        lazy="selectin",
        viewonly=True
    )
    researchers: Mapped[List["PersonRef"]] = relationship(
        "PersonRef",
        primaryjoin=and_(
            id == PersonRef.metadata_document_id,
            PersonRef.role == 'researcher'
        ),
        lazy="selectin",
        viewonly=True
    )
   
    people: Mapped[List["PersonRef"]] = relationship(
        "PersonRef",
        back_populates="metadata_document",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
    organizations: Mapped[List["OrganizationRef"]] = relationship("OrganizationRef", back_populates="metadata_document", foreign_keys="OrganizationRef.metadata_document_id")
    
    variables: Mapped[List["Variable"]] = relationship("Variable", back_populates="metadata_document", foreign_keys="Variable.metadata_document_id")

class Variable(Base):
    __tablename__ = "variable"
    id: Mapped[PG_UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=func.gen_random_uuid())
    name: Mapped[Optional[String]] = mapped_column(String)
    standard_name: Mapped[Optional[String]] = mapped_column(String)
    description: Mapped[Optional[String]] = mapped_column(String)
    dataset_variable_name: Mapped[Optional[String]] = mapped_column(String)
    units: Mapped[Optional[String]] = mapped_column(String)
    metadata_document_id: Mapped[Optional[PG_UUID]] = mapped_column(PG_UUID, ForeignKey("metadata_document.id"))
    metadata_document: Mapped[Optional["MetadataDocument"]] = relationship("MetadataDocument", back_populates="variables", foreign_keys=[metadata_document_id])
    variable_type: Mapped[String] = mapped_column(String)
    __mapper_args__ = {
        "polymorphic_on": "variable_type",
        "polymorphic_identity": "base"
    }


class TaVariable(Variable):
    __tablename__ = "ta_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    cellType: Mapped[Optional[String]] = mapped_column(String)
    curveFitting: Mapped[Optional[String]] = mapped_column(String)
    blankCorrection: Mapped[Optional[String]] = mapped_column(String)
    __mapper_args__ = {
        "polymorphic_identity": "ta_variable"
    }


class PhVariable(Variable):
    __tablename__ = "ph_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    phScale: Mapped[Optional[String]] = mapped_column(String)
    measurement_temperature: Mapped[Optional[String]] = mapped_column(String)
    temperature_correction_method: Mapped[Optional[String]] = mapped_column(String)
    ph_report_temperature: Mapped[Optional[String]] = mapped_column(String)
    __mapper_args__ = {
        "polymorphic_identity": "ph_variable"
    }


class Co2Variable(Variable):
    __tablename__ = "co2_variable"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("variable.id"), primary_key=True, default=func.gen_random_uuid())
    gasDetector: Mapped[Optional[String]] = mapped_column(String)
    waterVaporCorrection: Mapped[Optional[String]] = mapped_column(String)
    temperatureCorrectionMethod: Mapped[Optional[String]] = mapped_column(String)
    co2ReportTemperature: Mapped[Optional[String]] = mapped_column(String)
    __mapper_args__ = {
        "polymorphic_identity": "co2_variable"
    }


class Co2Autonomous(Co2Variable):
    __tablename__ = "co2_autonomous"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("co2_variable.id"), primary_key=True, default=func.gen_random_uuid())
    locationSeawaterIntake: Mapped[Optional[String]] = mapped_column(String)
    depthSeawaterIntake: Mapped[Optional[String]] = mapped_column(String)
    equilibrator: Mapped[Optional[String]] = mapped_column(String)
    __mapper_args__ = {
        "polymorphic_identity": "co2_autonomous"
    }


class Co2Discrete(Co2Variable):
    __tablename__ = "co2_discrete"
    id: Mapped[PG_UUID] = mapped_column(ForeignKey("co2_variable.id"), primary_key=True, default=func.gen_random_uuid())
    storageMethod: Mapped[Optional[String]] = mapped_column(String)
    seawaterVolume: Mapped[Optional[String]] = mapped_column(String)
    headspaceVolume: Mapped[Optional[String]] = mapped_column(String)
    measurementTemperature: Mapped[Optional[String]] = mapped_column(String)
    __mapper_args__ = {
        "polymorphic_identity": "co2_discrete"
    }


