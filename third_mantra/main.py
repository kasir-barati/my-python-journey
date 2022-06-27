from .classes.person import Person

mageMagic = [
    {"name": "Fire", "cost": 10, "damage": 60},
    {"name": "Thunder", "cost": 10, "damage": 60},
    {"name": "Blizzard", "cost": 10, "damage": 60}
]
mage = Person(460, 65, 60, 34, mageMagic)

print(mage.generate_damage())
print(mage.generate_damage())
print(mage.generate_damage())
print(mage.generate_damage())