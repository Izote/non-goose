from __future__ import annotations
from typing import TYPE_CHECKING
from semiotics.sign import Sign

if TYPE_CHECKING:
    from semiotics.content import Content
    from semiotics.expression import Expression


class Lemma(Sign):
    def __init__(self, expression: Expression, content: Content = None):
        super().__init__(expression=expression, content=content)
