from random import choice, randint
from .phoneme import Phoneme
from data.ipa import CONSONANT, VOWEL


def get_syllable(allowable: str):
    structure = []

    i = 0
    while i < len(allowable):
        char = allowable[i]
        if char != "(":
            structure.append(char)
            i += 1
        else:
            if randint(0, 1) == 1:
                structure.append(allowable[i + 1])
            i += 3

    syllable = []
    for s in structure:
        if s == "C":
            symbol = choice(CONSONANT)
            variable = ("voiced", "place", "manner")
        else:
            symbol = choice(VOWEL)
            variable = ("height", "backness", "rounded")

        syllable.append(Phoneme(symbol, variable))

    return syllable
