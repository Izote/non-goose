from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data.unit import EmicUnit


class Sign:
    """
    This class represents a single Sign.
    """
    def __init__(self, signified: list[EmicUnit],
                 signifier: str = None) -> None:
        """
        Constructs an instance of the Sign class and its attributes.


        :param signified: a list of EmicUnit objects representing the
            elements of the Sign observable in reality.

        :param signifier: a string designation of what the Sign represents.
            Defaults to None, allowing for post-construction assignment.
        """
        self.signified = signified
        self.signifier = signifier

    def __repr__(self) -> str:
        signified = [s.symbol for s in self.signified]
        return f"Sign(signified={signified}, signifier={self.signifier})"
