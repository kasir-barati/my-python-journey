from abc import ABC
from abc import abstractmethod
from typing import Optional
from ..types.use_item import UseItem


class Item(ABC):
    def __init__(
            self,
            name: str,
            description: str,
            value: int|str,
            kind: Optional[str]=None):
        self.name = name
        self.kind = kind if kind is not None else ""
        self.value = value
        self.description = description

    @abstractmethod
    def use_item(self) -> UseItem:
        pass


class Potion(Item):
    def __init__(
            self, 
            description: str, 
            value: int|str):
        super().__init__("Potion", description, value, "potion")

    def use_item(self) -> UseItem:
        super().use_item()
        return {
            "hp": self.value,
            "who": "individual",
            "mp": None
        }


class HighPotion(Potion):
    def __init__(
            self, 
            description: str, 
            value: int|str):
        super().__init__(description, value)
        self.name = "High Potion"
    
    def use_item(self) -> UseItem:
        super().use_item()
        return {
            "hp": self.value,
            "who": "individual",
            "mp": None
        }


class SuperPortion(Potion):
    def __init__(
            self,
            description: str,
            value: int|str):
        super().__init__(description, value)
        self.name = "Super potion"
    
    def use_item(self) -> UseItem:
        super().use_item()
        return {
            "hp": self.value,
            "who": "party",
            "mp": None
        }


class Elixir(Item):
    def __init__(
            self,
            description: str,
            value: int|str):
        super().__init__("Elixir", description, value, "elixir")
    
    def use_item(self) -> UseItem:
        super().use_item()
        return {
            "hp": self.value,
            "who": "individual",
            "mp": self.value,
        }


class MegaElixir(Elixir):
    def __init__(
            self,
            description: str,
            value: int|str):
        super().__init__(description, value)
        self.name = "Mega Elixir"
    
    def use_item(self) -> UseItem:
        super().use_item()
        return {
            "hp": self.value,
            "who": "party",
            "mp": self.value,
        }


class Grenade(Item):
    def __init__(
            self, 
            description: str, 
            value: int|str):
        super().__init__("Grenade", description, value, "attack")

    def use_item(self) -> UseItem:
        super().use_item()
        return {
            "hp": self.value,
            "who": "enemy",
            "mp": None,
        }