from random import randrange
from ..enums.actions import Action
from ..types.magic import Magic


class Person:
    def __init__(
            self,
            name: str,
            hp: int, 
            mp: int,
            attack: int,
            defense: int,
            magics: list[Magic]) -> None:
        self.name = name
        self.attack_high = attack + 10
        self.attack_low = attack - 10
        self.defense = defense
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.magics = magics
        self.actions = [Action.ATTACK, Action.MAGIC]
    
    def generate_damage(self) -> int:
        return randrange(self.attack_low, self.attack_high)

    def generate_spell_damage(
            self, 
            magic_spell_index: int) -> int:
        # DBC check person's mp
        magic_spell_damage_low = self.magics[magic_spell_index]["damage"] - 5
        magic_spell_damage_high = self.magics[magic_spell_index]["damage"] + 5
        magic_spell_cost = self.get_spell_cost(magic_spell_index)

        current_mp = self.get_mp();

        if current_mp < magic_spell_cost:
            # I could also just return 0 and do nothing. 
            # But I think error is better.
            raise Exception(f"You're out of mp, {self.name}!") 

        self.reduce_mp(magic_spell_cost)
        
        return randrange(magic_spell_damage_low, magic_spell_damage_high)

    def take_damage(
            self, 
            damage: int) -> int|None:
        if self.hp == 0:
            # TODO: DBC
            # TODO: unit test
            # TODO: Throw error
            return
        
        self.hp -= damage
        
        if self.hp < 0:
            self.hp = 0

        return self.hp
    
    def heal(
            self, 
            hp: int) -> None:
        if self.hp >= hp:
            return
        self.hp += hp

    def get_hp(self) -> int:
        return self.hp
    
    def get_max_hp(self) -> int:
        return self.max_hp
    
    def get_mp(self) -> int:
        return self.mp
    
    def get_max_mp(self) -> int:
        return self.max_mp

    def reduce_mp(self, mp: int) -> None: 
        self.mp -= mp
    
    def get_spell_name(
            self,
            magic_spell_index: int) -> str:
        return  self.magics[magic_spell_index]["name"]

    def get_spell_cost(
            self,
            magic_spell_index: int) -> int:
        return  self.magics[magic_spell_index]["cost"]

    def choose_action(self) -> None:
        # actions_length = len(self.actions)
        # indexes = range(1, actions_length)

        # print("Actions: ")

        # for index, action in zip(indexes, self.actions):
        #     print(f"{index}: {action.name}")
        print("Actions: ")

        for action in self.actions:
            print(f"{action.value}: {action.name}")

    def choose_magic(self) -> None:
        magic_length = len(self.magics)

        print("Magics: ")

        for index in range(0, magic_length):
            spell_name = self.get_spell_name(index)
            spell_cost = self.get_spell_cost(index)

            print(f"{index + 1}: {spell_name}(cost: {spell_cost})")
