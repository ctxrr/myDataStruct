#coding=utf-8
"""This module contain an advance ADT implemented by _DoublyLinkedBase
"""
#------------Import packet-----------------------------------------------------------------------
from DoublyLinkedList import _DoublyLinkedBase

#------------Class PositionalList----------------------------------------------------------------
class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #-------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__ (self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """"Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__ (self, other):
            """Return True if other does not represent the same location."""
            return not (self == other) # opposite of eq

    #------------------------------- utility method -------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None: # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None # boundary violation
        else:
            return self.Position(self, node) # legitimate position

    #------------------------------- accessors -------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__ (self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        """Generate a backward iteration of the elements of the list."""
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    def showinfo(self):
        """Show the infomation of the current list"""
        print 'PositionalList info:[',
        for i in self:
            print i,
        print ']'

    #------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super(PositionalList,self)._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original) # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.
           Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element # temporarily store old element
        original._element = e # replace with new element
        return old_value # return the old element value

    def move_to_front(self,p):
        """Move the node to the front of the list"""
        old_element=self.delete(p)
        self.add_first(old_element)

    def max(self):
        """find the max element in list"""
        walk=self.first()
        max=self.first()
        while walk!=self.last():
            walk=self.after(walk)
            if walk.element() > max.element():
                max=walk
        print max.element()

    def find(self,e):
        """find if e exist in list"""
        walk=self.first()
        while walk!=self.last():
            if walk.element()==e:
                print 'find succeed'
                return walk
            else : walk=self.after(walk)
        print 'find nothing'
        return None
#------------Stand alone function----------------------------------------------------------------

def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) > 1: # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker) # next item to place
            value = pivot.element()
            if value > marker.element(): # pivot is already sorted
                marker = pivot # pivot becomes new marker
            else: # must relocate pivot
                walk = marker # find leftmost item greater than value
                while walk != L.first( ) and L.before(walk).element( ) > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value) # reinsert value before walk

def max(tlist):
    """Find the max element in the given list"""
    walk=tlist.first()
    max=tlist.first()
    while walk!=tlist.last():
        walk=tlist.after(walk)
        if walk.element() > max.element():
            max=walk
    print max.element()

def max_re(start_position,n,slist):
    """find the max one among the n element start from start_element
       using recursion
    """
    if n==2:
        if start_position.element() > slist.after(start_position).element():
            return start_position.element()
        else:
            return slist.after(start_position).element()
    elif n < 2:
        print 'wrong input'
        return None
    else:
        n-=1
        if start_position.element() > max_re(slist.after(start_position),n,slist):
            return start_position.element()
        else:
            return max_re(slist.after(start_position),n,slist)

#------------Test code-------------------------------------------------------------------------

if __name__ == '__main__':
    #-------------------------- Test code for PositionalList --------------------------
    print "Test for PositionalList.........................."
    a=PositionalList()
    a.add_last(1)
    a.add_first(8)
    a.add_last(24)
    a.add_first(96)
    a.add_last(100)
    a.showinfo()

    #-------------------------- Test code for insertion_sort --------------------------
    print "Test for PositionalList.........................."
    import copy
    m=copy.deepcopy(a)
    insertion_sort(m)
    m.showinfo()

    #-----------R-7.11----------------------------------------------------------------
    print "Test for R-7.11................................"
    print 'find max element (use function)is:',
    max(a)

    #-----------R-7.12----------------------------------------------------------------
    print "Test for R-7.12................................"
    print "find max element (use class method)is:",
    a.max()

    #-----------R-7.13----------------------------------------------------------------
    print "Test for R-7.13................................"
    print "test result of method find:"
    a.find(96)
    a.find(98)

    #-----------R-7.14----------------------------------------------------------------
    print "Test for R-7.14................................"
    x=a.first()
    y=a.after(x)
    z=a.after(y)
    j=a.after(z)
    k=a.last()
    ret=max_re(j,2,a)
    print ret
    a.showinfo()
    #-----------R-7.15----------------------------------------------------------------
    print "Test for R-7.15................................"
    print "forward iter:",
    for i in a:
        print i,
    print ''
    print "backward iter:",
    for i in reversed(a):
        print i,
    print ''
    #-----------R-7.17----------------------------------------------------------------
    print "Test for R-7.17................................"
    n=copy.deepcopy(a)
    print 'old list:',
    n.showinfo()
    n.move_to_front(n.last())
    print 'move the last element to front...'
    print 'new list:',
    n.showinfo()
