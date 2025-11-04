import json
import pprint
from models.models_association import (
    MetadataDocument,
)

from models.g_pydantic import (
    MetadataDocumentSchema,
)

from sqlalchemy.orm import Session

import constants

with Session(constants.postgres_engine) as session:
    metadata_docs = session.query(MetadataDocument).all()
    for doc in metadata_docs:

        doc_out = MetadataDocumentSchema.model_validate(doc)
        
        print(
            doc_out.model_dump_json(exclude_defaults=True, exclude_none=True, indent=4)
        )
        
       
        