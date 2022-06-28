from typing import TypedDict
from typing import Optional
from typing import Literal

class UseItem(TypedDict):
    hp: Optional[int|str]
    mp: Optional[int|str]
    who: Literal["individual", "party", "enemy"]

