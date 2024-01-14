from inspect import getmembers


class EmicUnit:
    __SORT_KEY = {"symbol": 0, "category": 1,
                  "voiced": 2, "place": 3, "manner": 4,
                  "height": 2, "backness": 3, "rounded": 4}

    """Base class representing any kind of Emic unit."""
    def __init__(self, symbol: str) -> None:
        """
        Construct an EmicUnit instance including its public `symbol` attribute.

        :param symbol: a string representation of the instance as an emic unit.
        """
        self.symbol = symbol

    def __repr__(self) -> str:
        output = f"{self.__class__.__name__}(symbol='{self.symbol}'"
        members = self.__get_members()

        if len(members) > 0:
            for key, value in members:
                value = f"'{value}'" if isinstance(value, str) else value
                output += f", {key}={value}"

        output += ")"

        return output

    def __getitem__(self, key: str) -> bool | str:
        return getattr(self, key)

    def __get_members(self) -> list:
        members = [m for m in getmembers(self) if
                   (m[0] != "symbol" and m[0][0] != "_" and m[0][-1] != "_")]
        members.sort(key=lambda x: self.__SORT_KEY[x[0]])

        return members
