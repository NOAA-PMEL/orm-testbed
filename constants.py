import os
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

import dataclasses
import datetime

UPLOAD_DIRECTORY = "../mount/submissions"
ARCHIVE_DIRECTORY = "../mount/archive"
BAG_DIRECTORY = "../mount/bags"
TAR_DIRECTORY = "../mount/tar"

submissions_table = "submission"
files_table = "file"
connection_string = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:docker@127.0.0.1:5432"
)


# Create a SQLAlchemy engine object. This object initiates a connection pool
# so we create it once here and import into app.py.

# This was the default Dash setting. I changed it to use a pool. May have implications we need to study.
#
# `poolclass=NullPool` prevents the Engine from using any connection more than once. You'll find more info here:
# https://docs.sqlalchemy.org/en/14/core/pooling.html#using-connection-pools-with-multiprocessing-or-os-fork
#
#
# This set of connection parameters seems to work.  I have had no stale connection issues since using this set of parameters
# https://stackoverflow.com/questions/67872936/fastapi-psycopg2-operationalerror-server-closed-the-connection-unexpectedly
#
postgres_engine = create_engine(
    connection_string,
    pool_pre_ping=True,
    pool_recycle=3600,  # this line might not be needed
    connect_args={
        "keepalives": 1,
        "keepalives_idle": 30,
        "keepalives_interval": 10,
        "keepalives_count": 5,
    },
)