import json

import pytest


@pytest.fixture
def mock_creds():
    return {"USER": "foo", "PASSW": "bar", "HOST": "spam", "PORT": "3306", "DB": "baz"}


@pytest.fixture
def mock_creds_file(tmpdir, mock_creds):
    fh = tmpdir.join("powstancy.json")
    with open(fh, "w") as f:
        json.dump(mock_creds, f)
    return fh
