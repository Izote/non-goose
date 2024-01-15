class Content:
    def __init__(self, gloss: str = None,
                 data: dict[str, str | int | bool] = None) -> None:
        self.gloss = gloss
        self.data = data

    def __repr__(self) -> str:
        return f"Content(gloss={self.gloss}, data={self.data})"

    def __getitem__(self, item: str) -> str | int | bool:
        if item == "gloss":
            return self.gloss
        else:
            return self.data[item]
