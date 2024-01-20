from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data.unit import EmicUnit


class Expression:
    """
    Represents any Expression (i.e., the observable elements of a Sign)
    """
    def __init__(self, unit: list[EmicUnit] = None,
                 string: str = None) -> None:
        """
        Constructs an instance of the Expression class and its attributes.

        :param unit: a list of EmicUnit instances, where element order
            corresponds to their real-world sequence. Defaults to None.

        :param string: an optional string for use as the `string` attribute.
        """
        self.unit = unit

        if self.unit is None:
            self.string = None
        else:
            if string is None:
                self.string = "".join([u.symbol for u in self.unit])
            else:
                self.string = string

    def __repr__(self) -> str:
        str_unit = f"'{self.string}'" if self.unit else None
        return f"Expression(string={str_unit})"

    def __getitem__(self, item: str) -> str | list:
        return getattr(self, item)
