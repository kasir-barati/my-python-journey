from typing import TypedDict
from ..classes.inventory import Item


class PersonItem(TypedDict):
    item: Item
    count: int

