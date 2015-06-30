#coding=utf-8
"""
    This module implements a favorites list ADT supported by Sorted list which
    implemented by PositionalList ADT.
"""
from PositionalList import PositionalList

class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""

    #------------------------------ nested Item class ------------------------------
    class _Item:
        __slots__ ='_value','_count'# streamline memory usage
        def __init__ (self, e):
            self._value = e # the user s element
            self._count = 0 # access count initially zero

    #------------------------------- nonpublic utilities -------------------------------
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first(): # consider moving...
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count: # must shift forward
                while (walk != self._data.first() and
                        cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p)) # delete/reinsert
    #------------------------------- public methods -------------------------------
    def __init__ (self):
        """Create an empty list of favorites."""
        self._data = PositionalList() # will be list of Item instances

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty."""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e) # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e)) # if new, place at end
        p.element()._count += 1 # always increment count
        self._move_up(p) # consider moving forward

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e) # try to locate existing element
        if p is not None:
            self._data.delete(p) # delete, if found

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element() # element of list is Item
            yield item._value # report user’s element
            walk = self._data.after(walk)

class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""

    # we override move up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p)) # delete/reinsert

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data: # positional lists support iteration
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element()._value # report element to user
            temp.delete(highPos) # remove from temp list

if __name__ == '__main__':
    """test for FavoritesList""" 
    a=FavoritesList()
    a.access('a')
    a.access('a')
    a.access('b')
    a.access('b')
    a.access('a')
    a.access('c')
    for i in a.top(3):
        print i

    """test for FavoritesListMTF"""
    b=FavoritesListMTF()
    b.access('a')
    b.access('a')
    b.access('b')
    b.access('b')
    b.access('a')
    b.access('c')
    for i in b.top(3):
        print i