import csv
import json
import os

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.engine import Engine


metadata = MetaData()


def local_creds_fh():
    return os.path.join(os.getenv("USERPROFILE"), ".ijp/powstancy.json")


def get_creds(creds_fh: str = None) -> dict:
    if creds_fh is None:
        creds_fh = local_creds_fh()

    with open(creds_fh, "r") as f:
        creds = json.load(f)
        return creds


def get_engine(creds: dict) -> Engine:

    engine = create_engine(
        f"mysql+pymysql://{creds['USER']}:{creds['PASSW']}@{creds['HOST']}:{creds['PORT']}/{creds['DB']}"
    )
    return engine


def reflect_table(table: str, metadata: MetaData, engine: Engine):
    model = Table(table, metadata, autoload_with=engine)
    return model
