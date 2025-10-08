from models.models import (
    MetadataDocument,
)

from models.pydantic_schemas import (
    MetadataDocumentSchema
)

from sqlalchemy.orm import Session

import constants

with Session(constants.postgres_engine) as session:
    metadata_docs = session.query(MetadataDocument).all()
    for doc in metadata_docs:
        doc_out = MetadataDocumentSchema.model_validate(doc)
        print(
            doc_out.model_dump_json(indent=4, exclude_defaults=True, exclude_none=True)
        )