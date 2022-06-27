from typing import Optional
from .text.color import Color
from .text.style import Style


def style_me(
        message: str,
        *, 
        is_header: Optional[bool]=None,
        is_blue: Optional[bool]=None,
        is_succeed: Optional[bool]=None,
        is_warned: Optional[bool]=None,
        is_failed: Optional[bool]=None,
        is_bold: Optional[bool]=None, 
        is_underlined: Optional[bool]=None):
    final_text: str = ''
    end = '\033[0m'

    if is_header:
        final_text += Style.HEADER.value
    if is_bold:
        final_text += Style.BOLD.value
    if is_underlined:
        final_text += Style.UNDERLINE.value
    if is_blue:
        final_text += Color.BLUE
    if is_succeed:
        final_text += Color.GREEN
    if is_warned:
        final_text += Color.YELLOW
    if is_failed:
        final_text += Color.RED
    
    final_text += message
    final_text += end

    return final_text

