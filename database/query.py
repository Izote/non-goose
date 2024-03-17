from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from supabase import Client


def query(client: Client, table: str, key: str,
          select: str = None, where: tuple = None,
          insert: dict = None) -> list | None:
    """
    Execute one of several basic queries against the desired database table.

    :param client: Currently, a supabase.Client instance.
    :param table:  The name of the target database table.
    :param key: Primary key on the target table.
    :param select: SELECT statement columns in 'a' or 'a, b' string format.
    :param where: (x, y) tuple setting a WHERE x = y clause.
    :param insert: A dictionary of row-level data in column, value pairs.

    :return: SELECT statement results as a list of dictionaries or None.
    """
    tbl = client.table(table)

    if select and not where:
        response = tbl.select(select).execute()
    elif select and where:
        response = tbl.select(select).eq(where[0], where[1]).execute()
    elif insert:
        response = tbl.select("*").eq(key, insert[key]).execute()
    else:
        raise NotImplementedError("only one SQL statement per query allowed")

    if select:
        return response.data
    else:
        if not response.data:
            tbl.insert(insert).execute()
        else:
            msg = f"'{insert[key]}' row already exists in table '{table}'"

            raise ValueError(msg)
