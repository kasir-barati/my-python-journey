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
        self.attack_low = attack - 10
        self.defense = defense
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.magic = magic
        self.actions = [Action.ATTACK, Action.MAGIC]
    
    def generate_damage(self):
        return randrange(self.attack_low, self.attack_high)

    def generate_spell_damage(self, magic_spell_index: int):
        magic_spell_damage_low = self.magic[magic_spell_index]["damage"] - 5
        magic_spell_damage_high = self.magic[magic_spell_index]["damage"] + 5
        
        return randrange(magic_spell_damage_low, magic_spell_damage_high)

    def take_damage(self, damage: int):
        if self.hp == 0:
            # TODO: DBC
            # TODO: unit test
            # TODO: Throw error
            return
        
        self.hp -= damage
        
        if self.hp < 0:
            self.hp = 0

        return self.hp

