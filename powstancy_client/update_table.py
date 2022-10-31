import csv

from sqlalchemy import text
from sqlalchemy.engine import Connection

from powstancy_client.datastore import get_creds, get_engine


def update_organizations_row(
    conn: Connection,
    table_id: int,
    new_value: str,
):
    """
    Updates a row of given id in the 'ijp_dokumenty_instytucje' table.

    Args:
        conn:              `sqlalchemy.engine.Connection` instance
        table_id:          `id` value
        new_value:         new `instytucja` column value

    Returns:
        number of updated rows
    """
    stmt = text(
        "UPDATE ijp_dokumenty_instytucje SET instytucja = :new_value WHERE id=:table_id"
    ).bindparams(
        new_value=new_value,
        table_id=table_id,
    )
    result = conn.execute(stmt)
    return result.rowcount


def update_organizations(src: str, creds_fh: str = None) -> None:
    """
    Reads csv file with updated values for the `instytucje` column of
    the `ijp_dokumentyh_instytucje` table and commits them to the database.

    Args:
        src:                source csv file path
    """

    # open db connection
    creds = get_creds(creds_fh)
    engine = get_engine(creds)

    with engine.connect() as conn:
        with open(src, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip the header
            for i, row in enumerate(reader):
                table_id = int(row[0])
                new_value = row[1].strip()
                if table_id and new_value:
                    row_update_count = update_organizations_row(
                        conn, table_id, new_value
                    )
                else:
                    row_update_count = 0
                    print(f"Skipped empty row {i + 1}: {row}")

                if row_update_count == 1:
                    print(f"Updated row {table_id}")
                else:
                    print(f"Unable to update following row: {row}")
                    break
