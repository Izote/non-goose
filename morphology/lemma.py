from __future__ import annotations
from typing import TYPE_CHECKING
from semiotics.sign import Sign

if TYPE_CHECKING:
    from semiotics.content import Content
    from semiotics.expression import Expression


class Lemma(Sign):
    """
    Represents a single Lemma.
    """
    def __init__(self, expression: Expression, structure: list,
                 content: Content = None) -> None:
        """
        Construct an instance of the Lemma class, and its attributes,
        inheriting from the Sign class.

        :param expression: an Expression instance.
        :param content: a Content instance. Defaults to None if not provided.
        """
        super().__init__(expression=expression, content=content)

        self.structure = structure

    def __repr__(self) -> str:
        return (f"Lemma(expression={self.expression}, "
                f"structure='{self.structure}', content={self.content})")

