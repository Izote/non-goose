from __future__ import annotations
from .lemma import Lemma
from semiotics.content import Content
from semiotics.expression import Expression
from phonology.get_syllable import get_syllable


def generate_lemma(allowable: str, length: int,
                   content: Content = None) -> Lemma:

    emic_list = get_syllable(allowable)
    if length > 1:
        for _ in range(1, length):
            emic_list = emic_list + get_syllable(allowable)

    expression = Expression(emic_list)

    if content is None:
        content = Content()

    return Lemma(expression=expression, content=content)
