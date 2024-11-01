from random import randrange
from typing import Literal


class Spell:
    def __init__(
            self,
            name: str,
            cost: int,
            damage: int,
            kind: Literal["black", "white"]) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage
        self.kind = kind

    def generate_damage(self) -> int:
        # DBC check person's mp
        magic_spell_damage_low = self.damage - 5
        magic_spell_damage_high = self.damage + 5
        
        return randrange(magic_spell_damage_low, magic_spell_damage_high)

    def heal(self) -> int:
        return self.damage