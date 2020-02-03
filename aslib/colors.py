"""
colors.py
~~~~~~~~~
"""
from enum import Enum, unique
from typing import Tuple

@unique
class Color(Enum):
    """Colors used in AgroSuccess visualisations."""
    BLUE = '#0074d9'
    RED = '#ff4136'
    GREY = '#333333'
    VIOLET = '#bfbfff'
    YELLOW = '#ffdc00'
    LIGHT_BLUE = '#7fdbff'
    GREEN = '#2ecc40'
    LIGHT_PURPLE = '#b10dc9'
    ORANGE = '#ff851b'
    DARK_PURPLE = '#85144b'

    def __init__(self, hex_code: str) -> None:
        self._hex_code = hex_code

    @property
    def hex_code(self) -> str:
        """Hex color code, as used in HTML."""
        return self._hex_code

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """RGB representation of color."""
        return hex_to_rgb(self.hex_code)


def hex_to_rgb(h: str) -> Tuple[int, int, int]:
    """Convert hex string, `h` to an RGB tuple."""
    return tuple(int(h[1:][i:i+2], 16) for i in (0, 2, 4))
