from typing import TypedDict
from typing import Optional
from typing import Literal

class UseItem(TypedDict):
    hp: Optional[int]
    mp: Optional[int]
    meter: Literal["percentage", "unit"]