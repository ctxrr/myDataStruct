#coding=utf-8
"""this module contain:
    1.A DoublyLinkedBase class given by DSAP
    2.Some usage of DoublyLinkedBase class such as stack queue and deque.
"""
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__='_element','_prev','_next'# streamline memory

        def __init__ (self, element, prev, next): # initialize node’s fields
            self._element = element # user’s element
            self._prev = prev # previous node reference
            self._next = next # next node reference

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
        current = self._header._next
        print 'Show info:[',
        for i in range(self._size):
            print current._element,
            current=current._next
        print ']'

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

if __name__ == '__main__':

    """test for stack"""
    print 'test program for stack.............'
    teststack=DoublyLinkedStack()
    a=teststack
    a.pop(1)
    a.pop('a')
    a.pop(100)
    a.showinfo()
    print ' '

    """test for queue"""
    print 'test program for queue.............'
    testqueue=DoublyLinkedQueue()
    b=testqueue
    b.enqueue(1)
    b.enqueue('a')
    b.enqueue(100)
    b.showinfo()
    print ' '

    """test for deque"""
    print 'test program for deque.............'
    testdeque=DoublyLinkedDeque()
    c=testdeque
    c.add_last(1)
    c.add_first('a')
    c.add_first(100)
    c.showinfo()
    print ' '