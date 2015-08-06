#coding=utf-8
"""
    ### This module implements a favorites list ADT FavoritesList supported by Sorted list which
        implemented by PositionalList ADT.
    ### It also re-implemented a new class FavoritesListMTF in a different way based on
        move-to-front heuristic
"""

#------------Import packet-----------------------------------------------------------------------
from PositionalList import PositionalList

#------------Class Favoriteslist-----------------------------------------------------------------
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

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        for i in self._data:
            yield i

    def __reversed__(self):
        """Generate a backward iteration of the elements of the list."""
        for i in reversed(self._data):
            yield i

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

    def clear(self):
        """Clean the list into empty"""
        self._data = PositionalList() # will be list of Item instances

    def reset_count(self):
        """Reset the count of element in list leaving the order unchanged"""
        for i in self:
            i._count = 0

    def showinfo(self):
        """Show the infomation of the current list"""
        print 'Favoriteslist info:[',
        for i in self:
            print '(',i._value,',',i._count,')',
        print ']'

    def showelement(self):
        """Show the element of the current list"""
        print 'Favoriteslist elements:[',
        for i in self:
            print i._value,
        print ']'
#------------Class FavoriteslistMTF-----------------------------------------------------------
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

#------------Class FavoriteslistMTFAd-----------------------------------------------------------
class FavorateListMTFAd(FavoritesListMTF):
    """Subclass of FavoritesListMTF,but the elements that have not been
       accessed in the most resent n accesses are automatically purged
       from the list.
    """

    #------------------------------ nested Item class ------------------------------
    class _Item:
        __slots__ ='_value','_count'# streamline memory usage
        def __init__ (self, e):
            self._value = e # the user s element
            self._count = 0 # access count initially zero
            self._accessnum = 0

    def __init__ (self,maxnum):
        """Create an empty list of favorites."""
        self._data = PositionalList() # will be list of Item instances
        self._accessnum = 0
        self._max = maxnum

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        self._accessnum += 1
        p = self._find_position(e) # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e)) # if new, place at end
        p.element()._count += 1 # always increment count
        p.element()._accessnum = self._accessnum
        self._move_up(p) # consider moving forward
        if self._data.last().element()._accessnum == (self._accessnum - self._max) :
            self._data.delete(self._data.last())

    def showinfo(self):
        """Show the infomation of the current list"""
        print 'Favoriteslist info:[',
        for i in self:
            print '(',i._value,',',i._count,',',i._accessnum,')',
        print ']'

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':

    #-------------------------- Test code for Favoriteslist ----------------------
    print "test for FavoritesList........................"
    a=FavoritesList()
    a.access('a')
    a.access('a')
    a.access('b')
    a.access('b')
    a.access('a')
    a.access('c')
    for i in a.top(3):
        print i,
    print ''
    print ''

    #-------------------------- Test code for FavoriteslistMTF --------------------
    print "test for FavoritesListMTF......................"
    b=FavoritesListMTF()
    b.access('a')
    b.access('a')
    b.access('b')
    b.access('b')
    b.access('a')
    b.access('c')
    for i in b.top(3):
        print i,
    print ''
    print ''

    #-----------R-7.20-----------------------------------------------------------------
    print "Test for R-7.20..............................."
    c=FavoritesListMTF()
    c.access(1)
    c.access(2)
    c.access(3)
    c.access(4)
    c.access(5)
    c.access(6)
    import copy
    m=copy.deepcopy(c)
    templist=list()
    print 'old list:',
    m.showelement()

    for i in m:
        templist.append(i._value)

    for i in templist:
        m.access(i) # i is at the top of the list,so access it will spend O(1) time

    print 'new list:',
    m.showelement()
    print ''

    #-----------R-7.21-----------------------------------------------------------------
    print "Test for R-7.21..............................."
    n=copy.deepcopy(c)
    templist1=list()
    print 'old list:',
    n.showelement()

    for i in reversed(n):#reversed() will not change the sequence of list
        templist1.append(i._value)

    for i in templist1:
        n.access(i) # i is at the end of the list,so access it will spend O(n) time

    print 'new list:',
    n.showelement()
    print ''

    #-----------R-7.22-----------------------------------------------------------------
    print "Test for R-7.22.............................."
    p=copy.deepcopy(c)
    print 'old list:',
    p.showelement()

    p.clear()
    print 'new list:',
    p.showelement()
    print ''

    #-----------R-7.23-----------------------------------------------------------------
    print "Test for R-7.23.............................."
    q=copy.deepcopy(c)
    print 'old list:',
    q.showinfo()

    q.reset_count()
    print 'new list:',
    q.showinfo()
    print ''

    #-----------C-7.40-----------------------------------------------------------------
    print "Test for C-7.40.............................."
    mmm = FavorateListMTFAd(8)
    for i in range(10):
        mmm.access(i)
    mmm.showinfo()
    mmm.access(9)
    mmm.showinfo()
    mmm.access(9)
    mmm.showinfo()
    mmm.access(9)
    mmm.showinfo()
    print ''

