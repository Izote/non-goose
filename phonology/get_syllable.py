from __future__ import annotations
from numpy.random import Generator
from .phoneme import Phoneme
from data.ipa import CONSONANT, VOWEL


def get_syllable(allowable: str, rng: Generator) -> list[Phoneme]:
    """
    Returns a random syllable as a list of Phoneme class instances.

    :param allowable: the maximal allowable syllable in "CV(C)" style format.
    :param rng: a numpy.random.Generator instance used for randomization.

    :return: list[Phoneme]
    """
    i = 0

    structure = []
    while i < len(allowable):
        char = allowable[i]
        if char != "(":
            structure.append(char)
            i += 1
        else:
            if rng.choice([True, False]):
                structure.append(allowable[i + 1])
            i += 3

    syllable = []
    for s in structure:
        if s == "C":
            symbol = rng.choice(CONSONANT)
            variable = ("voiced", "place", "manner")
        else:
            symbol = rng.choice(VOWEL)
            variable = ("height", "backness", "rounded")

        syllable.append(Phoneme(symbol, variable))

    return syllable
