from data.unit import Unit
from data.ipa import IPA


class Phoneme(Unit):
    """
    Represents a single Phoneme.
    """
    def __init__(self, string: str, variable: tuple[str]) -> None:
        """
        Constructs an instance of the Phoneme class, and its attributes,
        inheriting from the EmicUnit class.

        :param string: the IPA symbol representing the Phoneme.
        :param variable: a tuple of variables from the IPA data set to include.
        """
        super().__init__(string=string)

        data = IPA[IPA.string == self.string].iloc[0, :]
        for var in variable:
            setattr(self, var, data[var])

        self.category = "consonant" if data.ipa_number < 300 else "vowel"
