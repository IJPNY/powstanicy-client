# -*- coding:utf-8 -*-

from contextlib import nullcontext as does_not_raise

from powstancy_client.update_table import update_organizations_row, update_organizations
from powstancy_client.datastore import get_creds, get_engine


@pytest.mark.local
def test_update_organizations_row():
    creds = get_creds()
    engine = get_engine(creds)
    with engine.connect() as conn:

        result = update_organizations_row(
            conn,
            1,
            "Milicja Górnośląska. Oddział Wartowniczy w Sosnowcu",
        )
        assert result == 1


@pytest.mark.local
@pytest.mark.slow
def test_update_organizations():
    with does_not_raise():
        update_organizations("temp/instytucje-new.csv")
