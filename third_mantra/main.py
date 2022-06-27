from .classes.person import Person
from .types.magic import Magic

magics: list[Magic] = [
    {"name": "Fire", "cost": 10, "damage": 60},
    {"name": "Thunder", "cost": 10, "damage": 80},
    {"name": "Blizzard", "cost": 10, "damage": 60}
]
mage = Person(460, 65, 60, 34, magics)
wizard = Person(1200, 61, 67, 74, magics)

print(mage.generate_damage())
print(mage.generate_damage())
print(mage.generate_spell_damage(0))
print(mage.generate_spell_damage(1))
print(mage.take_damage(54))
print(mage.take_damage(80))
mage.choose_action()
mage.choose_magic()