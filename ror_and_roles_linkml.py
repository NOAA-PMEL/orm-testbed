from typing import List
from dash.html import Sub
import models.shared
import flask
from flask import jsonify
import os
from pathlib import Path

# from models.metadata import Book, Author, Document, File, Submission, Submitter

from models.linkml.models import (
    Base,
    MetadataRole,
    ResearchOrganization
) 

import constants

import pandas as pd

from sqlalchemy.orm import Session

from pydantic import ValidationError


db = models.shared.db
server = flask.Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:docker@127.0.0.1:5432"
)
server.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
db.init_app(server)

with server.app_context():
    Base.metadata.create_all(bind=constants.postgres_engine)

# book1 = Book(title="A Good Book")
# book2 = Book(title="A Better Book")
# author = Author(name="Joe Blow", books=[book1, book2])

ror = pd.read_csv('../mount/ror/v1.70-2025-08-26-ror-data_schema_v2.csv', low_memory=False)
ror.sort_values(['names.types.ror_display'], inplace=True)

with Session(constants.postgres_engine) as session:
    for index, row  in ror.iterrows():
        rid = row['id']
        display = row['names.types.ror_display']
        session.add(ResearchOrganization(url=rid, display_name=display))

    session.add(MetadataRole(name="Data Submitter"))
    session.add(MetadataRole(name='Investigator'))

    session.commit()

