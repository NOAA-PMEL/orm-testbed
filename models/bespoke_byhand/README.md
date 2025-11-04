These models were constructed by-hand based on previous models. Relationships between the metadata
document and the people and organizations are done by assoication model classes which add descriptions and roles. The relationship between a person and their
organizaitons is done via a regular assoication table to create a many-to-many relationship. Special people like the data submitter and special organizations
like the resonsible party are done via a filter on the assoication between the document and the object using the specific role to pick out the particular 
associations which have that role.

When serializing the model the full definition from the association is included in the output document for all people and organizations except in this example
a special Schema class is used to output the data submitter so that only the object ID of the related organization, the description, and the role are output to show
how one can customize the output using the schema definition.
