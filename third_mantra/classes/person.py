from random import randrange
from ..enums.actions import Action


class Person:
    hp: int
    max_hp: int
    mp: int
    max_mp: int
    attack_low: int
    attack_high: int
    defense: int
    magic: int
    actions: Action
    
    def __init__(
            self, 
            hp: int, 
            mp: int,
            attack: int,
            defense: int,
            magic: int):
        self.attack_high = attack + 10
        self.attack_low = attack + 10
        self.defense = defense
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.magic = magic
        self.actions = [Action.ATTACK, Action.MAGIC]
    
    def generate_damage(self):
        return randrange(self.attack_low, self.attack_high)

