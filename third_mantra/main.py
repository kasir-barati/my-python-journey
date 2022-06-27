from .classes.person import Person

mageMagic = [
    {"name": "Fire", "cost": 10, "damage": 60},
    {"name": "Thunder", "cost": 10, "damage": 80},
    {"name": "Blizzard", "cost": 10, "damage": 60}
]
mage = Person(460, 65, 60, 34, mageMagic)

print(mage.generate_damage())
print(mage.generate_damage())
print(mage.generate_spell_damage(0))
print(mage.generate_spell_damage(1))
print(mage.take_damage(54))
print(mage.take_damage(80))
mage.choose_action()
mage.choose_magic()