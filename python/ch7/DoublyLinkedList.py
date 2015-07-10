#coding=utf-8
"""this module contain a _DoublyLinkedBase class given by DSAP

   ### With _DoublyLinkedBase,DSAP implement 3 ADT:
       1.DoublyLinkedStack
       2.DoublyLinkedQueue
       3.DoublyLinkedDeque
"""
#------------Class Empty--------------------------------------------------------------------------
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

#------------Class _DoublyLinkedBase--------------------------------------------------------------
class _DoublyLinkedBase(object):
    """A base class providing a doubly linked list representation."""

    #-------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__='_element','_prev','_next'# streamline memory

        def __init__ (self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    #------------------------------- public methods -------------------------------
    def __init__ (self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer # trailer is after header
        self._trailer._prev = self._header # header is before trailer
        self._size = 0 # number of elements

    def __len__ (self):
        """Return the number of elements in the list."""
        return self._size

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        walk = self._header._next
        while walk._element != None:
            yield walk._element
            walk = walk._next

    def __reversed__(self):
        """Generate a backward iteration of the elements of the list."""
        walk = self._trailer._prev
        while walk._element !=None:
            yield walk._element
            walk = walk._prev

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor) # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element # record deleted element
        node._prev = node._next = node._element = None # deprecate node
        return element # return deleted element

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("List is empty")
        return self._header._next._element # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("List is empty")
        return self._trailer._prev._element # real item just before trailer

    def showinfo(self):
        """Show the infomation of the current list"""
        print 'List:[',
        for i in self:
            print i,
        print ']'

    def reverse(self):
        # p = self._header._next
        # q = self._header._next._next
        # last = self._trailer
        # p._next = self._trailer
        # self._trailer._prev = p
        # while q._next != last:
        #     r = q._next
        #     q._next = p
        #     p._prev = q
        #     p = q
        #     q = r
        # q._prev = self._header
        # self._header._next = q
        pass

#------------Subclass------------------------------------------------------------------------------
class DoublyLinkedDeque(_DoublyLinkedBase): # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""
    def add_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next) # after header

    def add_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("List is empty")
        return self._delete_node(self._header._next) # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("List is empty")
        return self._delete_node(self._trailer._prev) # use inherited method

    def showinfo(self):
        print 'DoublyLinkedDeque',
        super(DoublyLinkedDeque,self).showinfo()

class DoublyLinkedQueue(_DoublyLinkedBase): # note the use of inheritance
    """Single-ended queue implementation based on a doubly linked list."""
    def enqueue(self, e):
        """Add an element to the back of the queue."""
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

    def dequeue(self):
        """Remove and return the element from the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("List is empty")
        return self._delete_node(self._header._next) # use inherited method

    def showinfo(self):
        print 'DoublyLinkedQueue',
        super(DoublyLinkedQueue,self).showinfo()

class DoublyLinkedStack(_DoublyLinkedBase): # note the use of inheritance
    """Stack implementation based on a doubly linked list."""
    def pop(self, e):
        """Add an element to the front of the stack."""
        self._insert_between(e, self._header, self._header._next) # after header

    def push(self):
        """Remove and return the element from the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("List is empty")
        return self._delete_node(self._header._next) # use inherited method

    def showinfo(self):
        print 'DoublyLinkedStack',
        super(DoublyLinkedStack,self).showinfo()

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':

    #-------------------------- Test code for LinkedStack --------------------------
    print "Test for LinkedStack.........................."
    ds=DoublyLinkedStack()
    ds.pop(1)
    ds.pop('a')
    ds.pop(100)
    ds.showinfo()
    print ' '

    #-------------------------- Test code for LinkedQueue --------------------------
    print "Test for LinkedQueue.........................."
    dq=DoublyLinkedQueue()
    dq.enqueue(1)
    dq.enqueue('a')
    dq.enqueue(100)
    dq.showinfo()
    print ' '

    #-------------------------- Test code for LinkedQueue --------------------------
    print "Test for LinkedQueue.........................."
    dd=DoublyLinkedDeque()
    dd.add_last(1)
    dd.add_first('a')
    dd.add_first(100)
    dd.add_first(10)
    dd.add_first(8)
    dd.showinfo()
    print ' '
    dd.reverse()
    dd.showinfo()
    print ''
    #-----------R-7.8-----------------------------------------------------------------
    print "Test for R-7.8..............................."
    """do has odd number of nodes while de has even"""
    do=DoublyLinkedDeque()
    do.add_first(1)
    do.add_first(2)
    do.add_first(3)
    do.add_first(4)
    do.add_first(5)
    print '1st size is odd:',
    do.showinfo()

    de=DoublyLinkedDeque()
    de.add_first(1)
    de.add_first(2)
    de.add_first(3)
    de.add_first(4)
    de.add_first(5)
    de.add_first(6)
    print '2nd size is even',
    de.showinfo()

    """definition of the function"""
    def find_middle_node(tlist):
        tempheader=tlist._header
        temptrailer=tlist._trailer
        while tempheader!=temptrailer and tempheader._next!=temptrailer:
            tempheader=tempheader._next
            temptrailer=temptrailer._prev
        return tempheader._element

    """test the result of my function"""
    print 'the middle in 1st is',find_middle_node(do)
    print 'the middle in 2nd is',find_middle_node(de)
    print ''

    #-----------R-7.9-----------------------------------------------------------------
    print "Test for R-7.9..............................."
    import copy
    def concatenate_list(m,n):
        """concatenate 2 doubly linked list"""
        templist=copy.copy(m)
        #templist=m
        temptrailer=templist._trailer
        temptrailer._prev._next=n._header._next
        n._header._next._prev=temptrailer._prev

        templist._trailer=n._trailer
        templist._size+=len(n)
        return templist

    """test the result of my function"""
    new_list=DoublyLinkedDeque()
    new_list=concatenate_list(do,de)
    print '1st list:',
    do.showinfo()
    print '2nd list:',
    de.showinfo()
    print 'new list:',
    new_list.showinfo()

