from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from supabase import Client


def query(client: Client, table: str,
          select: str = None, where: tuple = None,
          insert: dict = None) -> list | None:
    """
    Execute one of several basic queries against the desired database table.

    :param client: currently a supabase Client.
    :param table:  the name of the target database table.
    :param select: string selecting columns in 'a' or 'a, b' format.
    :param where: (x, y) tuple setting a WHERE x = y clause.
    :param insert: a dictionary of row-level data in column, value pairs.

    :return: SELECT statement results as a list of dictionaries or None.
    """
    key = "concept"
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
