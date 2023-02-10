"""Colorful text

You can use anything from here using the package import
>>> from colorful_string import Color
>>> from colorful_string import CallLinks"""

from os import environ
from typing import Callable, Literal, Tuple, Union, Optional
from types import SimpleNamespace
from warnings import warn
from inspect import currentframe, getframeinfo
from ast import parse as _astparse

# TYPINGS
RGB = Union['Color', Tuple[int, int, int]]
ForeBack = Union[Literal['fore'], Literal['back']]
OPTMODULE = Optional[SimpleNamespace]
STYLEFN = Callable[[str, int], str]

# Const
RESET = "\033[0m"

# where do i know this? https://en.wikipedia.org/wiki/ANSI_escape_code
# and this module is only for coloring and styling. It might not perfect but
# it will not use all the ANSI Escape codes.

class UnsupportedTerminal(UserWarning):
    """Current terminal may not support 256 colors."""

class Color:
    """Color"""
    def __init__(self, red: int, green: int, blue: int) -> None:
        for base, num in zip(('red', 'green', 'blue'), (red, green, blue)):
            if num <= -1 or num >= 256:
                raise ValueError(f"Invalid numeric value of {base} -> {num}")
        self._red = red
        self._green = green
        self._blue = blue
        self._arr = (red, green, blue)

    def __iter__(self):
        return iter(self._arr)

    def _update_arr(self):
        self._arr = (self._red, self._green, self._blue)

    def _check(self, base: str, value: int):
        if value <= -1 or value >= 256:
            raise ValueError(f"Invalid numeric value of {base} -> {value}")

    def _update(self, base: str, value: int):
        self._check(base, value)
        self.__dict__[f'_{base}'] = value
        self._update_arr()

    def as_tuple(self):
        """Return as tuple"""
        return self._arr

    def __len__(self):
        return 3

    def __int__(self):
        return int(self.hex, 16)

    @property
    def hex(self):
        """Hex Representation"""
        return f"0x{hex(self.red)[2:]:0>2}{hex(self.green)[2:]:0>2}{hex(self.blue)[2:]:0>2}"

    @property
    def red(self):
        """Red base"""
        return self._red

    @red.setter
    def red(self, value: int):
        """Red base"""
        self._update('red', value)

    @property
    def green(self):
        """Green base"""
        return self._green

    @green.setter
    def green(self, value: int):
        """Green base"""
        self._update('green', value)

    @property
    def blue(self):
        """Blue base"""
        return self._blue

    @blue.setter
    def blue(self, value: int):
        """Blue base"""
        self._update('blue', value)

    def __repr__(self) -> str:
        return f"#{self.hex[2:]}"

if "256color" not in environ.get("TERM", ''):
    TERM = environ.get("TERM", "this")
    if TERM == "":
        TERM = "this"
<<<<<<< HEAD
    warn(f"{TERM} terminal may not support 256 colors.\
Foregrounds.X may works better, but that's your choice.")
=======
    warn(f"{TERM} terminal may not support 256 colors. \
Foregrounds.X may works better, but that's your\
 choice.")
>>>>>>> ed516ebbe915394f801426a00466ef536324f381
    del TERM

def factory(opt: ForeBack, color: RGB, __install: OPTMODULE = None) -> STYLEFN:
    """Create function with background/foregroung color

    Args:
        opt (ForeBack): Fore/Back (use as 'fore' or 'back')
        color (RGB): 3 sized tuple or Color instance

    Raises:
        TypeError: If mismatch.

    Returns:
        Callable(str, int) -> str: Function related with this function summary.
    """
    if not isinstance(color, (tuple, Color)):
        raise TypeError(f"Expected Color | tuple, got {type(color).__name__}")
    colors = color if isinstance(color, Color) else Color(*color)
    code = "\033[38;2;" if opt == 'fore' else "\033[48;2;"

    def wrapper(string: str, __call_depth: int = 0) -> str:
        """Encapsulate string in defined code (the second args will close the encapsulation)"""
        rgb = ";".join((str(a) for a in colors))
        return f"{code}{rgb}m{string}{RESET if __call_depth == 0 else ''}"
    wrapper.__name__ = opt+'ground'
    wrapper.__doc__  = """Encapsulate string in defined code (the second args will \
close the encapsulation) (color id -> {colors!r}""" # type: ignore
    wrapper.colors = colors # type: ignore
    if __install:
        caller = getframeinfo(currentframe().f_back)  # Don't edit this part.
        if caller.code_context is not None:
            try:
                code = _astparse(caller.code_context[caller.index].rstrip().lstrip())
                name = code.body[0].targets[0].id
            except AttributeError: # most likely due to Expr.
                name = wrapper.__name__
            setattr(__install, name, wrapper)
            return wrapper
        setattr(__install, wrapper.__name__, wrapper)
    return wrapper


def _base_factory(name: str, code: str, __install: OPTMODULE = None) -> STYLEFN:
    """Create function as name with its code.

    Args:
        name (str): name of the function
        cpde (str): code of the name.

    Returns:
        Callable(str, int) -> str: Function related with this function summary.
    """

    def wrapper(string: str, __call_depth: int = 0) -> str:
        return f"{code}{string}{RESET if __call_depth == 0 else ''}"
    wrapper.__name__ = name
    wrapper.__doc__ = f"""Encapsulate string in defined code \
(the second args will close the encapsulation) (id -> {code[2:-1]})""" # type: ignore
    if __install:
        caller = getframeinfo(currentframe().f_back)  # Don't edit this part.
        if caller.code_context is not None:
            try:
                code = _astparse(caller.code_context[caller.index].rstrip().lstrip())
                varname = code.body[0].targets[0].id
            except AttributeError: # most likely due to Expr.
                varname = name
            setattr(__install, varname, wrapper)
            return wrapper
        setattr(__install, name, wrapper)

    return wrapper

Background = SimpleNamespace()
Foreground = SimpleNamespace()
Style = SimpleNamespace()


Bold = _base_factory("bold", "\033[1m", Style)
Faint = _base_factory('faint', '\033[2m', Style)
Italic = _base_factory('italic', '\033[3m', Style)
Underline = _base_factory("underline", '\033[4m', Style)
SlowBlink = _base_factory("slow_blink", '\033[5m', Style)
RapidBlink = _base_factory('rapid_blink', '\033[6m', Style)
Invert = _base_factory('invert', '\033[7m', Style)
Hide = _base_factory('hide', '\033[8m', Style)
Strike = _base_factory('strike', '\033[9m', Style)
Default = _base_factory('primary', '\033[10m', Style)
AltFont1 = _base_factory('altfont1', '\033[11m', Style)
AltFont2 = _base_factory('altfont2', '\033[12m', Style)
AltFont3 = _base_factory('altfont3', '\033[13m', Style)
AltFont4 = _base_factory('altfont4', '\033[14m', Style)
AltFont5 = _base_factory('altfont5', '\033[15m', Style)
AltFont6 = _base_factory('altfont6', '\033[16m', Style)
AltFont7 = _base_factory('altfont7', '\033[17m', Style)
AltFont8 = _base_factory('altfont8', '\033[18m', Style)
AltFont9 = _base_factory('altfont9', '\033[19m', Style)
Fraktur = _base_factory('fraktur', '\033[20m', Style)
Two_underline_or_not_bold = _base_factory('2underline-notbold', '\033[21m', Style)
NormalIntensity = _base_factory('normal', '\033[22m', Style)
NeitherItalicNorBlackletter = _base_factory('not_italic_blackletter', '\033[23m', Style) # pylint: disable
NotUnderlined = _base_factory('not_underlined', '\033[24m', Style)
NotBlinking = _base_factory('unblink', '\033[25m', Style)
ProportionalSpacing = _base_factory('proportional-spacing', '\033[26m', Style)
NotReversed = _base_factory('not-reversed', '\033[27m', Style)
Reveal = _base_factory("reveal", '\033[28m', Style)
NotStriked = _base_factory('Unstriked', '\033[29m', Style)
Framed = _base_factory('framed', '\033[51m', Style)
Encircled = _base_factory('encircled', '\033[52m', Style)
Overlined = _base_factory("overlined", '\033[53m', Style)
NotFramed = _base_factory("unframed", "\033[54m", Style)
NotOverlined = _base_factory('NotOverlined', '\033[55m', Style)

_fores = list(range(30, 38))+list(range(90, 98))
_backs = list(range(40, 48))+list(range(100, 108))

for bname, foreg, backg in zip(("Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan",
                               "White", "Gray", "BrightRed", "BrightGreen", "BrightYellow",
                               "BrightBlue", "BrightMagenta", "BrightCyan", "BrightWhite"),
<<<<<<< HEAD
                              list(range(30, 38))+list(range(90, 98)),
                              list(range(40, 48))+list(range(100, 108))):
=======
                               _fores,
                               _backs):
>>>>>>> ed516ebbe915394f801426a00466ef536324f381
    fgname = f"Fore_{bname}"
    bgname = f"Back_{bname}"
    _base_factory(fgname, f"\033[{foreg}m", Foreground)
    _base_factory(bgname, f"\033[{backg}m", Background)

__all__ = ["Color", "factory", "Bold", "Faint", "Italic", "Underline", "SlowBlink", "RapidBlink",
           "Invert", "Hide", "Strike", "Default", "AltFont1", "AltFont2", "AltFont3", "AltFont4",
           "AltFont5", "AltFont6", "AltFont7", "AltFont8", "AltFont9", "Fraktur",
           "Two_underline_or_not_bold", "NormalIntensity", "NeitherItalicNorBlackletter",
           "NotBlinking", "NotUnderlined", "ProportionalSpacing", "NotReversed", "Reveal",
           "NotStriked", "Framed", "Encircled", "Overlined", "NotFramed", "NotOverlined",
           "Background", "Foreground"]
