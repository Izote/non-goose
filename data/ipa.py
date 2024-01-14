from __future__ import annotations
from typing import TYPE_CHECKING
from pandas import read_csv
from settings import IPA_FILEPATH, EXCLUDE_MANNER, EXCLUDE_PLACE

if TYPE_CHECKING:
    from pandas import DataFrame


def load_ipa(exclude_manner: list[str] = None,
             exclude_place: list[str] = None) -> DataFrame:
    def parse_voicing(value):
        if isinstance(value, str) and value == "voiced":
            return True
        else:
            return False

    def parse_rounding(value):
        if isinstance(value, str) and value == "rounded":
            return True
        else:
            return False

    data = read_csv(IPA_FILEPATH)

    if isinstance(exclude_manner, list):
        data = data[~ data.manner.isin(exclude_manner)].copy()

    if isinstance(exclude_place, list):
        data = data[~ data.place.isin(exclude_place)].copy()

    data["voiced"] = data.voicing.apply(parse_voicing)
    data["rounded"] = data.voicing.apply(parse_rounding)

    return data


IPA = load_ipa(exclude_manner=EXCLUDE_MANNER, exclude_place=EXCLUDE_PLACE)
