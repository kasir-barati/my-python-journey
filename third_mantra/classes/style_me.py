from typing import Optional
from .text.color import Color
from .text.style import Style


def style_me(
        message: str,
        *, 
        is_blue: Optional[bool]=None,
        is_succeed: Optional[bool]=None,
        is_warned: Optional[bool]=None,
        is_failed: Optional[bool]=None,
        is_bold: Optional[bool]=None, 
        is_underlined: Optional[bool]=None,
        is_turquoise: Optional[bool]=None,
        is_purple: Optional[bool]=None):
    final_text: str = ''
    end = '\033[0m'

    if is_bold:
        final_text += Style.BOLD.value
    if is_underlined:
        final_text += Style.UNDERLINE.value

    if is_blue:
        final_text += Color.BLUE
    elif is_succeed:
        final_text += Color.GREEN
    elif is_warned:
        final_text += Color.YELLOW
    elif is_failed:
        final_text += Color.RED
    elif is_turquoise:
        final_text += Color.TURQUOISE
    elif is_purple:
        final_text += Color.PURPLE 
    
    final_text += message
    final_text += end

    return final_text

