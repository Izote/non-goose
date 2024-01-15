from data.unit import EmicUnit
from data.ipa import IPA


class Phoneme(EmicUnit):
    def __init__(self, symbol: str, variable: tuple[str]) -> None:
        super().__init__(symbol=symbol)

        data = IPA[IPA.symbol == self.symbol].iloc[0, :]
        for var in variable:
            setattr(self, var, data[var])

        self.category = "consonant" if data.ipa_number < 300 else "vowel"
