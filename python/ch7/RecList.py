"""This module contain a recursive implementation of single linked list class Reclist
"""
#------------Class Empty--------------------------------------------------------------------------
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

#------------Class Reclist------------------------------------------------------------------------
class Reclist:

    def __init__(self,e):
        """Create an Reclist."""
        self._element = e
        self._rest = None
        self._size = 0

    def __len__ (self):
        """Return the number of elements in the Reclist."""
        return self._size

    def is_empty(self):
        """Return True if the SingleLinkedList is empty."""
        return self._size == 0

    def _add(self,e):
        """Add element e at the end of the list."""
        if self._rest == None:
            new = Reclist(e)
            self._rest = new
        else:
            self._rest._add(e)

    def push(self,e):
        """Add element e to the top of the stack."""
        self._add(e)
        self._size += 1

    def _remove(self):
        """Remove the last element of the list."""
        if self._rest._rest ==None:
            old = self._rest._element
            self._rest = None
            return old
        else:
            return self._rest._remove()

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
           Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('List is empty')
        self._size -= 1
        return self._remove()

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        walk = self._rest
        while walk != None:
            yield walk._element
            walk = walk._rest

    def showinfo(self):
        """Show the infomation of the current list"""
        print 'Info:[',
        for i in self:
            print i,
        print ']'
        print 'size is',self._size

#------------Test code-------------------------------------------------------------------------

if __name__ == '__main__':

    #-----------C-7.27----------------------------------------------------------------
    print "Test for C-7.27................................"
    a=Reclist(None)
    a.push(1)
    a.push(2)
    a.push(3)
    print a.pop()
    print a.pop()
    a.push(4)
    a.showinfo()
