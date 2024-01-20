from __future__ import annotations
from typing import TYPE_CHECKING
from inspect import getmembers
from .content import Content

if TYPE_CHECKING:
    from data.unit import EmicUnit
    from .expression import Expression


class Sign:
    """
    This class represents a single Sign.
    """
    def __init__(self, expression: Expression, content: Content) -> None:
        """
        Constructs an instance of the Sign class and its attributes.


        :param expression: an Expression instance representing the Sign's
            observable elements.

        :param content: a Content instance designating what the Sign refers to.
            Defaults to an empty Content instance for later re-assignment.
        """
        self.expression = expression
        if content is None:
            self.content = Content()
        else:
            self.content = content

        self.__expression_keys = [m[0] for m in getmembers(self.expression) if
                                  m[0][0] != "_" and m[0][-1] != "_"]

        self.__content_keys = [m[0] for m in getmembers(self.content) if
                               m[0][0] != "_" and m[0][-1] != "_"]

    def __repr__(self) -> str:
        return f"Sign(expression={self.expression}, content={self.content})"

    def __getitem__(self, item: str) -> str | int | list[EmicUnit]:
        if item in self.__expression_keys:
            return self.expression[item]
        elif item in self.__content_keys:
            return self.content[item]
        else:
            getattr(self, item)
