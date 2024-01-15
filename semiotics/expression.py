from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data.unit import EmicUnit


class Expression:
    """
    Represents any Expression (i.e., the observable elements of a Sign)
    """
    def __init__(self, unit: list[EmicUnit] = None) -> None:
        """
        Constructs an instance of the Expression class and its attributes.

        :param unit: a list of EmicUnit instances, where element order
            corresponds to their real-world sequence. Defaults to None.
        """
        self.unit = unit
        if self.unit is None:
            self.str = None
        else:
            self.str = "".join([u.symbol for u in self.unit])

    def __repr__(self) -> str:
        str_unit = f"'{self.str}'" if self.unit else None

        return f"Expression(str={str_unit})"

    def __getitem__(self, item: str):
        return getattr(self, item)
