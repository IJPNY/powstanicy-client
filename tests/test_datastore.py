import os

import pytest
from sqlalchemy.engine import Engine

from powstancy_client.datastore import local_creds_fh, get_creds, get_engine


@pytest.mark.local
def test_dev_local_creds_fh_exists():
    creds_fh = local_creds_fh()
    assert os.path.isfile(creds_fh)


def test_get_creds_provided(mock_creds_file):
    creds = get_creds(mock_creds_file)
    assert isinstance(creds, dict)


def test_get_creds_local():
    creds = get_creds()
    assert isinstance(creds, dict)


def test_get_engine(mock_creds_file):
    creds = get_creds(mock_creds_file)
    engine = get_engine(creds)
    assert isinstance(engine, Engine)
