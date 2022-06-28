from typing import Optional
from random import randrange
from ..types.use_item import UseItem
from ..classes.inventory import Item
from ..enums.actions import Action
# from ..types.magic import Magic
from .spell import Spell
from .style_me import style_me


class Person:
    def __init__(
            self,
            name: str,
            hp: int, 
            mp: int,
            attack: int,
            defense: int,
            # magics: list[Magic]
            magics: list[Spell],
            items: list[Item]) -> None:
        self.name = name
        self.attack_high = attack + 10
        self.attack_low = attack - 10
        self.defense = defense
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.magics = magics
        self.actions = [Action.ATTACK, Action.MAGIC, Action.ITEM]
        self.items = items
        
    def use_item(self, item_index: int) -> UseItem:
        return self.items[item_index].use_item()

    def do_magic(self, magic_index: int) -> int|None:
        magic_spell_cost = self.magics[magic_index].cost
        current_mp = self.get_mp()
        if current_mp < magic_spell_cost:
            # I could also just return 0 and do nothing. 
            # But I think error is better.
            raise Exception(f"You're out of mp, {self.name}!")             

        magic_spell_kind = self.magics[magic_index].kind
        
        if magic_spell_kind not in ["black", "white"]:
            raise Exception("Unexpected magic kind.")

        self.reduce_mp(magic_spell_cost)

        if magic_spell_kind == "black":
            return self.magics[magic_index].generate_damage()

        if magic_spell_kind == "white":
            increased_hp = self.magics[magic_index].heal()
            self.heal(increased_hp)
            return

    def generate_attack_damage(self) -> int|None:
        return randrange(self.attack_low, self.attack_high)

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
            hp: int|str) -> None:
        # Wrong usage 
        # if type(hp) == int:
        if type(hp) is int:
            self.hp += hp
        if hp == "full" or self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def increase_mp(
            self,
            mp: int|str):
        if type(mp) is int:
            self.mp += mp
        if mp == "full" or self.mp > self.max_mp:
            self.mp = self.max_mp

    def get_magic_options(self) -> list[int]: 
        maximum_valid_magic_index = len(self.magics)
        return list(range(1, maximum_valid_magic_index))

    def get_item_options(self) -> list[int]:
        maximum_valid_item_index = len(self.items)
        return list(range(1, maximum_valid_item_index))

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

    def choose_action(self) -> None:
        # actions_length = len(self.actions)
        # indexes = range(1, actions_length)

        # print("Actions: ")

        # for index, action in zip(indexes, self.actions):
        #     print(f"{index}: {action.name}")
        print(style_me("Actions: ", is_succeed=True))

        for action in self.actions:
            print(f"\t{action.value}: {action.name}")

    def choose_magic(self) -> None:
        magic_length = len(self.magics)

        print(style_me("Magics: ", is_blue=True))

        for index in range(0, magic_length):
            spell_name = self.magics[index].name
            spell_cost = self.magics[index].cost

            print(f"\t{index + 1}: {spell_name}(cost: {spell_cost})")

    def choose_item(self) -> None:
        items_length = len(self.items)

        print(style_me("Items: ", is_failed=True))

        for index in range(0, items_length):
            # self.items[index].__dir__() interchangeable 
            # with dir(self.items[index])
            print(f"\t{index + 1}: {vars(self.items[index])}")

