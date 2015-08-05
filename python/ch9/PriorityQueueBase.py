from ..exceptions import Empty
from abc import ABCMeta,abstractmethod

class PriorityQueueBase(object):
    """Abstract base class for a priority queue."""

    #------------------------------ nested _Item class ------------------------------
    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key    # compare items based on their keys

        def __repr__(self):
            return '({0},{1})'.format(self._key, self._value)

    #------------------------------ public behaviors ------------------------------
    def is_empty(self):                  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0

    @abstractmethod
    def __len__(self):
        """Return the number of items in the priority queue."""

    @abstractmethod
    def add(self, key, value):
        """Add a key-value pair."""

    @abstractmethod
    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """

    @abstractmethod
    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
