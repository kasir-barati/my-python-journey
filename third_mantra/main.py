from .classes.person import Person
# from .types.magic import Magic
from .classes.spell import Spell
from .classes.style_me import style_me
from .enums.actions import Action


def main():
    fire = Spell("Fire", 10, 60, "black")
    thunder = Spell("Thunder", 10, 80, "black")
    blizzard = Spell("Blizzard", 10, 70, "black")
    heal = Spell("Heal", 5, 120, "white")
    cure = Spell("Cure", 15, 340, "white")
    magics: list[Spell] = [
        fire,
        thunder,
        blizzard,
        heal,
        cure
    ]
    player = Person("Kasir", 460, 65, 60, 34, magics)
    wizard = Person("Sun", 1200, 61, 67, 74, magics)


    initial_app_message = style_me("An enemy attacks!", is_failed=True, is_bold=True)
    print(initial_app_message)


    while True:
        player_generated_damage = do_attack_or_magic(player)
        if player_generated_damage:
            wizard.take_damage(player_generated_damage)

        wizard_generated_damage = do_attack_or_magic(wizard)
        if wizard_generated_damage:
            player.take_damage(wizard_generated_damage)

        print_player_and_enemy_status(player, wizard)
        print("\n\r------------------------\n\r")

        if is_battle_over([player, wizard]):
            break

    print_player_and_enemy_status(player, wizard)


def is_battle_over(fighters: list[Person]):
    for fighter in fighters:
        if fighter.get_hp() == 0:
            message = style_me(
                f"{fighter.name} is dead",
                is_failed=True,
                is_bold=True
            )
            print(message)

            return True;
    
    return False;


def do_attack_or_magic(person: Person) -> int|None:
    person.choose_action()
    chose_action_message = style_me(f"Make your move {person.name}: ", is_blue=True)
    chosen_action = input(chose_action_message)
    chosen_action = int(chosen_action)
            
    if chosen_action == Action.ATTACK.value:
        return person.generate_damage(action=Action.ATTACK)
    elif chosen_action == Action.MAGIC.value:
        person.choose_magic()
        chose_your_spell_message = style_me("Chose your spell: ", is_succeed=True)
        chosen_spell = input(chose_your_spell_message)
        chosen_spell = int(chosen_spell) - 1
        
        maximum_valid_magic_index = len(person.magics)
        assert chosen_spell in range(0, maximum_valid_magic_index), "Chosen magic is invalid!"

        return person.generate_damage(
            action=Action.MAGIC, 
            magic_index=chosen_spell
        )
    else:
        raise Exception("Your choice was out of range")
    

def print_player_and_enemy_status(player: Person, enemy: Person):
    current_wizard_hp = enemy.get_hp()
    current_wizard_mp = enemy.get_mp()
    current_player_hp = player.get_hp()
    current_player_mp = player.get_mp()
    wizard_hp_message = style_me(
        f"Wizard status: hp = {current_wizard_hp}, mp = {current_wizard_mp}",
        is_failed=True
    )
    player_hp_message = style_me(
        f"Your status: hp = {current_player_hp}, mp = {current_player_mp}",
        is_succeed=True
    )
    
    print(wizard_hp_message + '. ' + player_hp_message)


main()

