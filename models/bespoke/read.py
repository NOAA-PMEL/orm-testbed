import json
import pprint
from models.models import (
    MetadataDocument,
    OrganizationRef,
    PersonRef,
)

from models.pydantic_schemas import (
    MetadataDocumentSchema,
    OrganizationRefSchema,
    PersonRefSchema
)

from sqlalchemy.orm import Session

import constants

with Session(constants.postgres_engine) as session:
    metadata_docs = session.query(MetadataDocument).all()
    for doc in metadata_docs:
        org_ref_id = doc.responsible_party_id
        org_ref = session.get(OrganizationRef, org_ref_id)
        org_ref_out = OrganizationRefSchema.model_validate(org_ref)
        org_ref_dict = json.loads(org_ref_out.model_dump_json(exclude_defaults=True, exclude_none=True))

        data_submitter_id = doc.data_submitter_id
        data_sub_ref = session.get(PersonRef, data_submitter_id)
        data_sub_out = PersonRefSchema.model_validate(data_sub_ref)
        data_ref_dict = json.loads(data_sub_out.model_dump_json(exclude_defaults=True, exclude_none=True))

        doc_out = MetadataDocumentSchema.model_validate(doc)
        doc_dict = json.loads(doc_out.model_dump_json(exclude_defaults=True, exclude_none=True))
        doc_dict['responsible_party_organization_ref'] = org_ref_dict
        doc_dict['data_submitter_ref'] = data_ref_dict
        
        print(
            json.dumps(doc_dict, indent=4)
        )
        
       
        