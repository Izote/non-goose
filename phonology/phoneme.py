from data.unit import EmicUnit
from data.ipa import IPA


class Phoneme(EmicUnit):
    """
    Represents a single Phoneme.
    """
    def __init__(self, symbol: str, variable: tuple[str]) -> None:
        """
        Constructs an instance of the Phoneme class, and its attributes,
        inheriting from the EmicUnit class.

        :param symbol: the IPA symbol representing the Phoneme.
        :param variable: a tuple of variables from the IPA data set to include.
        """
        super().__init__(symbol=symbol)

        data = IPA[IPA.symbol == self.symbol].iloc[0, :]
        for var in variable:
            setattr(self, var, data[var])

        self.category = "consonant" if data.ipa_number < 300 else "vowel"
