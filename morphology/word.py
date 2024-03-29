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
        Constructs A Word class instance.

        :param sounds: A dictionary with uppercase character strings as keys
            and lists of strings representing IPA characters as values.

        :param allow: The maximal allowable syllable in standard format.

        :param length: The Word's desired syllable length.

        :param rng: A numpy.random.Generator instance.

        :param gloss: Meaning of the Word. Defaults to None.
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
