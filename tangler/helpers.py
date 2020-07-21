"""
Miscellaneous helper functions.
"""

def wrap_list(val) -> list:
    """
        Wrap `val' in a list unless it is already a list.
    """
    if isinstance(val, list):
        return val
    return [val]
