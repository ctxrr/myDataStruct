from abc import ABCMeta,abstractmethod

class Stack(object):
    __metaclass__ = ABCMeta
    """Abstract base class representing a Stack structure."""

    # ---------- abstract methods that concrete subclass must support ----------
    @abstractmethod
    def push(self,p):
        """Add element e to the top of the stack"""

    @abstractmethod
    def pop(self):
        """Remove and return the element from the pop of the stack
        Raise Empty exception if the stack is empty
        """

    @abstractmethod
    def top(self):
        """Return(but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the stack."""

    # ---------- concrete methods implemented in this class ----------
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0


