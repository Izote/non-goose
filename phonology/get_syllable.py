from __future__ import annotations
from numpy.random import Generator
from .phoneme import Phoneme
from data.ipa import CONSONANT, VOWEL


def get_syllable(allowable: str, rng: Generator):
    structure = []

    i = 0
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
