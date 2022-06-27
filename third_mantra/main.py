from .classes.person import Person
from .types.magic import Magic
from .classes.style_me import style_me
from .enums.actions import Action


def main():
    magics: list[Magic] = [
        {"name": "Fire", "cost": 10, "damage": 60},
        {"name": "Thunder", "cost": 10, "damage": 80},
        {"name": "Blizzard", "cost": 10, "damage": 60}
    ]
    player = Person("Kasir", 460, 65, 60, 34, magics)
    wizard = Person("Sun", 1200, 61, 67, 74, magics)


    initial_app_message = style_me("An enemy attacks!", is_failed=True, is_bold=True)
    print(initial_app_message)


    while True:
        player_generated_damage = do_attack_or_magic(player)
        wizard.take_damage(player_generated_damage)

        wizard_generated_damage = do_attack_or_magic(wizard)
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


def do_attack_or_magic(person: Person) -> int:
    person.choose_action()
    chose_action_message = style_me(f"Make your move {person.name}: ", is_blue=True)
    chosen_action = input(chose_action_message)
    chosen_action = int(chosen_action)
            
    person_generate_damage: int = 0
    if chosen_action == Action.ATTACK.value:
        person_generate_damage = person.generate_damage()
    elif chosen_action == Action.MAGIC.value:
        person.choose_magic()
        chose_your_spell_message = style_me("Chose your spell: ", is_succeed=True)
        chosen_magic_spell = input(chose_your_spell_message)
        chosen_magic_spell = int(chosen_magic_spell) - 1
        
        maximum_valid_magic_index = len(person.magics)
        assert chosen_magic_spell in range(0, maximum_valid_magic_index), "Chosen magic is invalid!"

        person_generate_damage = person.generate_spell_damage(chosen_magic_spell)
    else:
        raise Exception("Your choice was out of range")
    
    return person_generate_damage


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

