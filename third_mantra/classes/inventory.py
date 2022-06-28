from ..types.use_item import UseItem

class Item:
    def __init__(
            self,
            name: str,
            kind: str,
            description: str,
            value: int):
        self.name = name
        self.kind = kind
        self.value = value
        self.description = description

    def use_item(self) -> UseItem|None:
        if self.name == "Potion":
            return {
                "hp": 50,
                "meter": "unit",
                "mp": None
            }
        elif self.name == "High Potion":
            return {
                "hp": 100,
                "meter": "unit",
                "mp": None
            }