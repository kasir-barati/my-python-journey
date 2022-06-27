from .classes.person import Person
from .types.magic import Magic
from .classes.my_print import my_print


magics: list[Magic] = [
    {"name": "Fire", "cost": 10, "damage": 60},
    {"name": "Thunder", "cost": 10, "damage": 80},
    {"name": "Blizzard", "cost": 10, "damage": 60}
]
mage = Person(460, 65, 60, 34, magics)
wizard = Person(1200, 61, 67, 74, magics)


my_print("An enemy attacks!", is_failed=True, is_bold=True)


# while True:
#     my_print()

