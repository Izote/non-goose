from __future__ import annotations
from typing import TYPE_CHECKING
from numpy import mean
from .query import query

if TYPE_CHECKING:
    from supabase import Client


def get_score(client: Client, gloss: str) -> int:
    """
    Returns a gloss' score based on its taxonomy properties.

    :param client: Currently, a supabase.Client.
    :param gloss: A linguistic gloss (i.e., word meaning).

    :return: A score used to compare the target to other words/glosses.
    """
    result = query(client, "taxonomy", "gloss",
                   select="*", where=("gloss", gloss))

    data = result[0]
    raw_value = [data[k] for k in data.keys() if k != "gloss"]

    # This is a "working" implementation until I have a better idea.
    return round(10*mean(raw_value))
