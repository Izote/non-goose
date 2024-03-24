from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from supabase import Client


def query(client: Client, table: str,
          select: str | list = None,
          insert: dict = None,
          where: tuple = None):
    """
    Execute a query against a given table.

    :param client: A `supabase.Client` instance.
    :param table: ...
    :param select: A string "*" or string/list of columns may be passed.
    :param insert: A dictionary of column, value pairs.
    :param where: A tuple of format ("x", "=", "y").

    :return: query result set as ...
    """
    q = client.table(table)

    if isinstance(select, list) or isinstance(select, str):
        if insert:
            return ValueError("`insert` must be None if `select` is provided.")
        q = q.select(select if isinstance(select, str) else ", ".join(select))

    if isinstance(insert, dict):
        if select:
            return ValueError("`select` must be None if `insert` is provided.")
        q = q.insert(insert)

    if isinstance(where, tuple):
        if where[1] == "=":
            q = q.eq(where[0], where[2])
        else:
            raise NotImplementedError

    return q.execute()
