from numpy.random import default_rng
from morphology import Lemma
from semiotics import Content, Expression
from phonology.get_syllable import get_syllable


class Language:
    def __init__(self, allowable: str,
                 inventory: dict[str, str] | tuple[int, int] = None,
                 seed: int = None) -> None:
        if seed is None:
            self.__seed = default_rng().integers(0, 10000)
        else:
            self.__seed = seed

        self.__rng = default_rng(self.__seed)
        self.allowable = allowable
        self.inventory = inventory

    def __repr__(self) -> str:
        return f"Language(seed={self.__seed})"

    def new_lemma(self, length: int = 1, content: Content = None) -> Lemma:
        emic = get_syllable(self.allowable, self.__rng)
        if length > 1:
            for _ in range(1, length):
                emic = emic + get_syllable(self.allowable, self.__rng)

        expression = Expression(emic)

        if content is None:
            content = Content()

        return Lemma(expression=expression, content=content)
