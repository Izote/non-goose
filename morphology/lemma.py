from __future__ import annotations
from typing import TYPE_CHECKING
from semiotics.sign import Sign

if TYPE_CHECKING:
    from data.unit import EmicUnit


class Lemma(Sign):
    def __init__(self, expression: list[EmicUnit], content: str = None):
        super().__init__(expression=expression, content=content)
