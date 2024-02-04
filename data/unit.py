from inspect import getmembers


class Unit:
    # Allows for fancy-sorting of priority members.
    __SORT_KEY = {"string": 0, "category": 1,
                  "voiced": 2, "place": 3, "manner": 4,
                  "height": 2, "backness": 3, "rounded": 4}

    """Base class representing any kind of Emic unit."""
    def __init__(self, string: str) -> None:
        """
        Construct a Unit instance including its public `string` attribute.

        :param string: a string representation of the unit's meaning.
        """
        self.string = string

    def __repr__(self) -> str:
        output = f"{self.__class__.__name__}(string='{self.string}'"
        members = self.__get_members()

        if len(members) > 0:
            for key, value in members:
                value = f"'{value}'" if isinstance(value, str) else value
                output += f", {key}={value}"

        output += ")"

        return output

    def __getitem__(self, key: str) -> bool | str:
        return getattr(self, key)

    def __get_members(self) -> list[str]:
        """
        Returns list of strings for each public member.

        :return: list[str]
        """
        def sort_members(x):
            member = x[0]
            if member in self.__SORT_KEY.keys():
                return self.__SORT_KEY[member]
            else:
                return ord(member[0])

        members = [m for m in getmembers(self) if
                   (m[0] != "string" and m[0][0] != "_" and m[0][-1] != "_")]
        members.sort(key=sort_members)

        return members
