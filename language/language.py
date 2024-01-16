from numpy.random import default_rng
from morphology import Lemma
from semiotics import Content, Expression
from phonology import Phoneme
from data.ipa import CONSONANT, VOWEL


class Language:
    """
    Represents a single Language.
    """
    def __init__(self, allowable: str,
                 inventory: dict[str, list[str]] | tuple[int, int] = None,
                 seed: int = None) -> None:
        """
        Construct an instance of the Language class and its attributes.

        :param allowable: the maximal allowable syllable.

        :param inventory: either a sound inventory as a dictionary of format
            {"C": ["p", ...], "V": ["a", ...]} or a tuple of integers
            representing the number of consonants, vowels.

        :param seed: an integer used to seed randomization.
        """
        if seed is None:
            self.__seed = default_rng().integers(0, 10000)
        else:
            self.__seed = seed

        self.__rng = default_rng(self.__seed)
        self.allowable = allowable

        if isinstance(inventory, tuple):
            inventory = {"C": list(self.__rng.choice(CONSONANT, inventory[0])),
                         "V": list(self.__rng.choice(VOWEL, inventory[1]))}
        elif isinstance(inventory, dict):
            pass
        else:
            raise TypeError("`inventory` must be a dict or tuple")

        self.__inventory = inventory
        self.group = inventory
        self.group_type = {"C": "C", "V": "V"}

        self.lexicon = []

    def __repr__(self) -> str:
        return f"Language(seed={self.__seed})"

    def __get_syllable(self) -> list[Phoneme]:
        """
        Returns a random syllable as a list of Phoneme class instances.

        :return: list[Phoneme]
        """
        i = 0

        structure = []
        while i < len(self.allowable):
            char = self.allowable[i]
            if char != "(":
                structure.append(char)
                i += 1
            else:
                if self.__rng.choice([True, False]):
                    structure.append(self.allowable[i + 1])
                i += 3

        syllable = []
        for alias in structure:
            if self.group_type[alias] == "C":
                symbol = self.__rng.choice(self.group[alias])
                variable = ("voiced", "place", "manner")
            else:
                symbol = self.__rng.choice(self.group[alias])
                variable = ("height", "backness", "rounded")

            syllable.append(Phoneme(symbol, variable))

        return syllable

    @property
    def inventory(self) -> dict[str, str]:
        return self.__inventory

    def new_lemma(self, length: int = 1, content: Content = None,
                  save: bool = False) -> Lemma:
        """
        Create a new Lemma using the Language's parameterization.

        :param length: syllable length for the output.

        :param content: a Content instance if available.
            Defaults to an empty Content instance.

        :param save: whether to store the result in the `lexicon` attribute.

        :return: Lemma
        """
        emic = self.__get_syllable()
        if length > 1:
            for _ in range(1, length):
                emic = emic + ["."] + self.__get_syllable()

        string = "".join([e if isinstance(e, str) else e.symbol for e in emic])
        emic = list(filter(lambda x: x != ".", emic))

        expression = Expression(unit=emic, string=string)

        if content is None:
            content = Content()

        lemma = Lemma(expression=expression, content=content)

        if save:
            self.lexicon.append(lemma)

        return lemma

    def add_group(self, alias: str, series: list[str],
                  series_type: str) -> None:
        """
        Add a group of sounds under a new (case-sensitive) label.

        :param alias: a single-character alias for the series.
        :param series: a list of IPA characters.
        :param series_type: whether the series consists of "C" or "V" sounds.
        :return:
        """
        if len(alias) != 1 or len(series_type) != 1:
            msg = "`label` and `series_type` must be single character strings"
            raise ValueError(msg)
        else:
            self.group[alias] = series
            self.group_type[alias] = series_type

    def drop_group(self, alias: str) -> None:
        if len(alias) != 1:
            raise ValueError("`label` must be a single character string")
        else:
            del self.group[alias]
            del self.group_type[alias]
