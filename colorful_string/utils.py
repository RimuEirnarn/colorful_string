"""Utility"""

from typing import Callable, Tuple

Function = Callable[[str, int], str]

class Combination:
    """Set combinations for future cases.

    As example:
    >>> x = Combination(Red, Bold, Italic)
    >>> x("Hello, World")
    # reddish, bold, and italic version of "Hello, World" """
    def __init__(self, *callables: Function):
        self._calls = list(callables)

    def push(self, func: Function):
        """Add function to the most right"""
        self._calls.append(func)

    def pushleft(self, func: Function):
        """Add function to the most left"""
        self._calls.insert(0, func)

    def insert(self, index: int, func: Function):
        """Insert function before index"""
        self._calls.insert(index, func)

    def pop(self, index: int = -1) -> Function:
        """Remove and return function at index (default last).

        Raises IndexError if list is empty or index is out of range."""
        return self._calls.pop(index)

    def remove(self, func: Function):
        """Remove first occurrence of value.

        Raises ValueError if the function is not present."""
        self._calls.remove(func)

    def view(self) -> Tuple[Function, ...]:
        """Return as tuple"""
        return tuple(self._calls)

    def __iter__(self):
        return iter(self._calls)

    def __len__(self):
        return len(self._calls)

    def __call__(self, string: str, __depth_call: int = -1) -> str:
        result = string
        __depth_call = len(self) if __depth_call == -1 else __depth_call
        for i in self:
            result = i(result, __depth_call)
            __depth_call -= 1
            if __depth_call == 0:
                result += "\033[0m"
                break
        return result

    def __repr__(self) -> str:
        return f"""Combination({len(self)} attached)"""

    def __missing__(self, cnt: Function):
        return cnt in self._calls

    def __add__(self, other: Function):
        self.push(other)
        return self

    def __sub__(self, other: Function):
        while other in self:
            self.remove(other)
        return self

CallLinks = Combination

__all__ = ["Combination", "CallLinks"]
