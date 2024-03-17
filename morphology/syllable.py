from __future__ import annotations
from typing import TYPE_CHECKING
from string import ascii_uppercase

if TYPE_CHECKING:
    from numpy.random import Generator


class Syllable:
    """
    Represents a single Syllable.
    """
    def __init__(self, sounds: dict, allow: str, rng: Generator) -> None:
        """
        Constructs a Syllable class instance.

        :param sounds: a dictionary with uppercase character strings as keys
            and lists of strings representing IPA characters as values.

        :param allow: the maximal allowable syllable in standard format.

        :param rng: a numpy.random.Generator instance.
        """
        self.__structure = self.__get_pattern(allow, rng)
        self.__string = self.__get_string(sounds, rng)

    def __repr__(self) -> str:
        output = "Syllable(str='{}', structure='{}')"

        return output.format(self.__string, self.__structure)

    def __str__(self) -> str:
        return self.__string

    @property
    def structure(self) -> str:
        return self.__structure

    @property
    def string(self) -> str:
        return self.__string

    def __get_pattern(self, allow: str, rng: Generator) -> str:
        """
        Return a morphology pattern for word generation.

        :param allow: the maximal allowable syllable in standard format.

        :param rng: a numpy.random.Generator instance.

        :return: an allowable morphology structure as a string.
        """
        key = []
        required = []
        pattern = []

        for i in range(len(allow)):
            if allow[i] in ascii_uppercase:
                key.append(allow[i])
                if 0 < i and allow[i - 1] == "(":
                    required.append(False)
                else:
                    required.append(True)

        for i in range(len(required)):
            if required[i]:
                pattern.append(key[i])
            else:
                if rng.choice([0, 1]) == 1:
                    pattern.append(key[i])

        return "".join(pattern)

    def __get_string(self, sounds: dict, rng: Generator) -> str:
        """
        Return a string of IPA characters based on chosen morphology structure.

        :param sounds: a dictionary with uppercase character strings as keys
            and lists of strings representing IPA characters as values.

        :param rng: a numpy.random.Generator instance.

        :return: a string of IPA characters.
        """
        string = [rng.choice(sounds[s]) for s in self.__structure]
        string = "".join(string)

        return string
