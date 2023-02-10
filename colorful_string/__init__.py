"""Colorful text"""
from sys import modules
from . import colors, utils
from .colors import *
from .utils import *

__all__ = colors.__all__ + utils.__all__ # type: ignore

modules["colorful_string.Style"] = colors.Style # type: ignore
modules["colorful_string.Background"] = colors.Background # type: ignore
modules["colorful_string.Foreground"] = colors.Foreground # type: ignore

__version__ = "0.1.2"

# Now you can do the usual stuff.
