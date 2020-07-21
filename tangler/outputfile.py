"""
Contains the OutputFile class, representing a file whos contents will be tangled
code from an input document.
"""

from os import linesep
from typing import List, FrozenSet

class OutputFile:
    """
        Represents a file whos contents will be tangled code
        from an input document.
    """
    def __init__(self, name: str, classes: List[str]):
        """
            Create a new file instance.
            Note that the actual file handler is lazy-loaded,
            to prevent it being opened when there is
            nothing to write to that file.
            """
        self.name: str = name
        # This is a frozenset to make it hashable
        self.classes: FrozenSet[str] = frozenset(classes)

        self.file = None # lazy-loaded

    def __del__(self):
        """
            Cleanup the object by closing the file handler (if any)
        """
        if self.file:
            self.file.close()

    def write(self, text: str):
        """
            Write text to the file, instanciating the handler if required.
        """
        try:
            self.file.write(text + linesep)
        except AttributeError: # Handler is None
            self.file = open(self.name, 'w')
            self.file.write(text + linesep)

    def matches(self, classes: List[str]) -> bool:
        """
            Determine whether a list of classes matches this file.
            Returns: True if the file's designated classes are a
                     subset of the passed classes, else False.
        """
        return self.classes.issubset(classes)
