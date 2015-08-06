from abc import ABCMeta,abstractmethod

class Deque(object):
    __metaclass__ = ABCMeta
    """Abstract base class representing a Deque structure."""

    # ---------- abstract methods that concrete subclass must support ----------
    @abstractmethod
    def add_first(self,p):
        """Add an element to the front of the deque."""

    @abstractmethod
    def add_last(self):
        """Add an element to the last of the deque."""

    @abstractmethod
    def delete_first(self):
        """Remove an element from the front of the deque."""

    @abstractmethod
    def delete_last(self):
        """Remove an element from the last of the deque."""

    @abstractmethod
    def first(self):
        """Return the first element in deque"""

    @abstractmethod
    def last(self):
        """Return the last element in deque"""

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the stack."""

    # ---------- concrete methods implemented in this class ----------
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0


