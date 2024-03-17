from __future__ import annotations
from typing import TYPE_CHECKING
from .syllable import Syllable

if TYPE_CHECKING:
    from numpy.random import Generator


class Word:
    """
    Represents a single Word.
    """
    def __init__(self, sounds: dict, allow: str, length: int,
                 rng: Generator, gloss: str = None) -> None:
        """
        Constructs a Word class instance.

        :param sounds: a dictionary with uppercase character strings as keys
            and lists of strings representing IPA characters as values.

        :param allow: the maximal allowable syllable in standard format.

        :param length: the Word's desired syllable length.

        :param rng: a numpy.random.Generator instance.

        :param gloss: meaning of the word. Defaults to None.
        """
        syllable = [Syllable(sounds, allow, rng) for _ in range(length)]
        self.string = ".".join([s.string for s in syllable])
        self.gloss = gloss

    def __len__(self) -> int:
        return self.string.count(".")

    def __repr__(self) -> str:
        if self.gloss:
            return f"Word(string='{self.string}', gloss='{self.gloss}')"
        else:
            return f"Word(string='{self.string}', gloss={self.gloss})"

    def __str__(self) -> str:
        return self.string
