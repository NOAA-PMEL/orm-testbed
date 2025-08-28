
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

from pydantic import BaseModel, ConfigDict
from datetime import datetime

Base = declarative_base()
metadata = Base.metadata


class ResearchOrganization(Base):
    __tablename__ = "ResearchOrganization"
    id = Column(Integer(), primary_key=True, nullable=False )
    url = Column(Text())
    display_name = Column(Text())


class OadsMetadata(Base):
    """
    This is the Dataset class, and the root of all the metadata.
    """
    __tablename__ = 'OadsMetadata'

    id = Column(Integer(), primary_key=True, nullable=False )
    title = Column(Text())
    submission_date = Column(DateTime())
    abstract = Column(Text())
    use_limitation = Column(Text())
    purpose = Column(Text())
    data_license = Column(Text())
    Submission_id = Column(Integer(), ForeignKey('Submission.id'))
    
    
    # ManyToMany
    investigators = relationship( "Person", secondary="OadsMetadata_investigators")
    
    
    # ManyToMany
    data_submitters = relationship( "Person", secondary="OadsMetadata_data_submitters")
    
    
    # One-To-Many: OneToAnyMapping(source_class='OadsMetadata', source_slot='related_datasets', mapping_type=None, target_class='RelatedDataset', target_slot='OadsMetadata_id', join_class=None, uses_join_table=None, multivalued=False)
    related_datasets = relationship( "RelatedDataset", foreign_keys="[RelatedDataset.OadsMetadata_id]")
    

    def __repr__(self):
        return f"OadsMetadata(id={self.id},title={self.title},submission_date={self.submission_date},abstract={self.abstract},use_limitation={self.use_limitation},purpose={self.purpose},data_license={self.data_license},Submission_id={self.Submission_id},)"

    
class Submission(Base):
    """
    A submission.
    """
    __tablename__ = 'Submission'

    id = Column(Integer(), primary_key=True, nullable=False )
    submitted_to_ncei = Column(Boolean())
    date_submitted_to_ncei = Column(DateTime())
    created = Column(DateTime())
    modified = Column(DateTime())
    DashboardUser_id = Column(Integer(), ForeignKey('DashboardUser.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Submission', source_slot='oads_metadata', mapping_type=None, target_class='OadsMetadata', target_slot='Submission_id', join_class=None, uses_join_table=None, multivalued=False)
    oads_metadata = relationship( "OadsMetadata", foreign_keys="[OadsMetadata.Submission_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Submission', source_slot='files', mapping_type=None, target_class='File', target_slot='Submission_id', join_class=None, uses_join_table=None, multivalued=False)
    files = relationship( "File", foreign_keys="[File.Submission_id]")
    

    def __repr__(self):
        return f"Submission(id={self.id},submitted_to_ncei={self.submitted_to_ncei},date_submitted_to_ncei={self.date_submitted_to_ncei},created={self.created},modified={self.modified},DashboardUser_id={self.DashboardUser_id},)"



    


class DashboardUser(Base):
    """
    The dashboard user.
    """
    __tablename__ = 'DashboardUser'

    id = Column(Integer(), primary_key=True, nullable=False )
    active = Column(Boolean())
    email = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='DashboardUser', source_slot='submissions', mapping_type=None, target_class='Submission', target_slot='DashboardUser_id', join_class=None, uses_join_table=None, multivalued=False)
    submissions = relationship( "Submission", foreign_keys="[Submission.DashboardUser_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='DashboardUser', source_slot='people', mapping_type=None, target_class='Person', target_slot='DashboardUser_id', join_class=None, uses_join_table=None, multivalued=False)
    people = relationship( "Person", foreign_keys="[Person.DashboardUser_id]")
    

    def __repr__(self):
        return f"DashboardUser(id={self.id},active={self.active},email={self.email},)"



    


class Person(Base):
    """
    A person is a human.
    """
    __tablename__ = 'Person'

    id = Column(Integer(), primary_key=True, nullable=False )
    title = Column(Text())
    first_name = Column(Text(), nullable=False )
    last_name = Column(Text(), nullable=False )
    DashboardUser_id = Column(Integer(), ForeignKey('DashboardUser.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Person', source_slot='contact_information', mapping_type=None, target_class='ContactInformation', target_slot='Person_id', join_class=None, uses_join_table=None, multivalued=False)
    contact_information = relationship( "ContactInformation", foreign_keys="[ContactInformation.Person_id]")
    
    
    # ManyToMany
    metadata_role = relationship( "MetadataRole", secondary="Person_metadata_role")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Person', source_slot='organizations', mapping_type=None, target_class='Organization', target_slot='Person_id', join_class=None, uses_join_table=None, multivalued=False)
    organizations = relationship( "Organization", foreign_keys="[Organization.Person_id]")
    
    
    # ManyToMany
    data_submitter_person = relationship( "OadsMetadata", secondary="Person_data_submitter_person")
    

    def __repr__(self):
        return f"Person(id={self.id},title={self.title},first_name={self.first_name},last_name={self.last_name},DashboardUser_id={self.DashboardUser_id},)"



    


class RelatedDataset(Base):
    """
    The dataset that is related to the entity.
    """
    __tablename__ = 'RelatedDataset'

    id = Column(Integer(), primary_key=True, nullable=False )
    dataset = Column(Text())
    link = Column(Text())
    OadsMetadata_id = Column(Integer(), ForeignKey('OadsMetadata.id'))
    

    def __repr__(self):
        return f"RelatedDataset(id={self.id},dataset={self.dataset},link={self.link},OadsMetadata_id={self.OadsMetadata_id},)"



    


class ContactInformation(Base):
    """
    The contact of information of a thing that is contactable.
    """
    __tablename__ = 'ContactInformation'

    id = Column(Integer(), primary_key=True, nullable=False )
    phone = Column(Text())
    email = Column(Text())
    link = Column(Text())
    Person_id = Column(Integer(), ForeignKey('Person.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ContactInformation', source_slot='address', mapping_type=None, target_class='Address', target_slot='ContactInformation_id', join_class=None, uses_join_table=None, multivalued=False)
    address = relationship( "Address", foreign_keys="[Address.ContactInformation_id]")
    

    def __repr__(self):
        return f"ContactInformation(id={self.id},phone={self.phone},email={self.email},link={self.link},Person_id={self.Person_id},)"



    


class Address(Base):
    """
    The Address information of an entity.
    """
    __tablename__ = 'Address'

    id = Column(Integer(), primary_key=True, nullable=False )
    city = Column(Text())
    administrative_area = Column(Text())
    postal_code = Column(Text())
    country = Column(Text())
    ContactInformation_id = Column(Integer(), ForeignKey('ContactInformation.id'))
    
    
    delivery_points_rel = relationship( "AddressDeliveryPoints" )
    delivery_points = association_proxy("delivery_points_rel", "delivery_points",
                                  creator=lambda x_: AddressDeliveryPoints(delivery_points=x_))
    

    def __repr__(self):
        return f"Address(id={self.id},city={self.city},administrative_area={self.administrative_area},postal_code={self.postal_code},country={self.country},ContactInformation_id={self.ContactInformation_id},)"



    


class MetadataRole(Base):
    """
    The metadata role.
    """
    __tablename__ = 'MetadataRole'

    id = Column(Integer(), primary_key=True, nullable=False )
    name = Column(Text())
    

    def __repr__(self):
        return f"MetadataRole(id={self.id},name={self.name},)"



    


class Organization(Base):
    """
    The organization.
    """
    __tablename__ = 'Organization'

    id = Column(Integer(), primary_key=True, nullable=False )
    name = Column(Text())
    organization_identifier = Column(Text())
    organization_identifier_type = Column(Enum('ror', 'gcmd', name='OrganizationIdentifierTypeEnum'))
    Person_id = Column(Integer(), ForeignKey('Person.id'))
    

    def __repr__(self):
        return f"Organization(id={self.id},name={self.name},organization_identifier={self.organization_identifier},organization_identifier_type={self.organization_identifier_type},Person_id={self.Person_id},)"



    


class File(Base):
    """
    A file.
    """
    __tablename__ = 'File'

    id = Column(Integer(), primary_key=True, nullable=False )
    filename = Column(Text())
    category = Column(Text())
    mime = Column(Text())
    created = Column(DateTime())
    modified = Column(DateTime())
    Submission_id = Column(Integer(), ForeignKey('Submission.id'))
    

    def __repr__(self):
        return f"File(id={self.id},filename={self.filename},category={self.category},mime={self.mime},created={self.created},modified={self.modified},Submission_id={self.Submission_id},)"



    


class OadsMetadataInvestigators(Base):
    """
    
    """
    __tablename__ = 'OadsMetadata_investigators'

    OadsMetadata_id = Column(Integer(), ForeignKey('OadsMetadata.id'), primary_key=True)
    investigators_id = Column(Integer(), ForeignKey('Person.id'), primary_key=True)
    

    def __repr__(self):
        return f"OadsMetadata_investigators(OadsMetadata_id={self.OadsMetadata_id},investigators_id={self.investigators_id},)"



    


class OadsMetadataDataSubmitters(Base):
    """
    
    """
    __tablename__ = 'OadsMetadata_data_submitters'

    OadsMetadata_id = Column(Integer(), ForeignKey('OadsMetadata.id'), primary_key=True)
    data_submitters_id = Column(Integer(), ForeignKey('Person.id'), primary_key=True)
    

    def __repr__(self):
        return f"OadsMetadata_data_submitters(OadsMetadata_id={self.OadsMetadata_id},data_submitters_id={self.data_submitters_id},)"



    


class PersonMetadataRole(Base):
    """
    
    """
    __tablename__ = 'Person_metadata_role'

    Person_id = Column(Integer(), ForeignKey('Person.id'), primary_key=True)
    metadata_role_id = Column(Integer(), ForeignKey('MetadataRole.id'), primary_key=True)
    

    def __repr__(self):
        return f"Person_metadata_role(Person_id={self.Person_id},metadata_role_id={self.metadata_role_id},)"



    


class PersonDataSubmitterPerson(Base):
    """
    
    """
    __tablename__ = 'Person_data_submitter_person'

    Person_id = Column(Integer(), ForeignKey('Person.id'), primary_key=True)
    data_submitter_person_id = Column(Integer(), ForeignKey('OadsMetadata.id'), primary_key=True)
    

    def __repr__(self):
        return f"Person_data_submitter_person(Person_id={self.Person_id},data_submitter_person_id={self.data_submitter_person_id},)"



    


class AddressDeliveryPoints(Base):
    """
    
    """
    __tablename__ = 'Address_delivery_points'

    Address_id = Column(Integer(), ForeignKey('Address.id'), primary_key=True)
    delivery_points = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Address_delivery_points(Address_id={self.Address_id},delivery_points={self.delivery_points},)"



    


