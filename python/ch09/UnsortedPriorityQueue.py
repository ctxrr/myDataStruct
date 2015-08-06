
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from PriorityQueueBase import PriorityQueueBase
from ch07.PositionalList import PositionalList
from tools.Exceptions import Empty

#------------Class UnsortedPriorityQueue--------------------------------------------------------------
class UnsortedPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with an unsorted list."""

    #----------------------------- nonpublic behavior -----------------------------
    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():               # is_empty inherited from base class
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    #------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def __iter__(self):
        """Generate an iterable"""
        for i in self._data:
            yield i

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

#------------ Test code--------------------------------------------------------------
if __name__ == '__main__':
    PQ = UnsortedPriorityQueue()
    PQ.add(3,'c')
    PQ.add(1,'a')
    PQ.add(2,'b')
    PQ.add(4,'d')
    PQ.showinfo()
    PQ.remove_min()
    PQ.showinfo()
    PQ.remove_min()
    PQ.showinfo()

