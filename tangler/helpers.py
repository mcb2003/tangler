"""
Miscellaneous helper functions.
"""

from collections.abc import Iterable # for testing if objects are iterable

def wrap_list(val) -> list:
    """
        Wrap `val' in a list unless it is already iterable.
    """
    if isinstance(val, Iterable):
        return val
    return [val]
