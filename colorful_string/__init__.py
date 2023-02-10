"""Colorful text"""
from sys import modules
from . import colors, utils
from .colors import *
from .utils import *

__all__ = colors.__all__ + utils.__all__ # type: ignore

<<<<<<< HEAD
modules["colorful_string.Style"] = colors.Style
modules["colorful_string.Background"] = colors.Background
modules["colorful_string.Foreground"] = colors.Foreground

__version__ = "0.0.3"
=======
__version__ = "0.1.1"
>>>>>>> ed516ebbe915394f801426a00466ef536324f381

# Now you can do the usual stuff.
