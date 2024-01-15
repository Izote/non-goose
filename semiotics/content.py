from __future__ import annotations
from typing import Any


class Content:
    """
    Represents any Content (i.e., what a Sign refers to/references).
    """
    def __init__(self, gloss: str = None, data: dict[str, Any] = None) -> None:
        """
        Construct an instance of the Content class and its attributes.

        :param gloss: the subject this instance represents.
        :param data: a dictionary of attributes that quantify the subject.
        """
        self.gloss = gloss
        self.data = data

    def __repr__(self) -> str:
        return f"Content(gloss={self.gloss}, data={self.data})"

    def __getitem__(self, item: str) -> str | int | bool:
        if item == "gloss":
            return self.gloss
        else:
            return self.data[item]
