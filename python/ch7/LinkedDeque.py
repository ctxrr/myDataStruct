#coding=utf-8
"""this module implements a deque by double linked list by DSAP"""

from DoublyLinkedBase import _DoublyLinkedBase

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class LinkedDeque(_DoublyLinkedBase): # note the use of inheritance
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element # real item just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next) # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next) # use inherited method

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev) # use inherited method

    def showinfo(self):
        """Show the infomation of the Deque"""
        current=self._header._next
        print 'Deque info:[',
        for i in range(self._size):
            print current._element,
            current=current._next
        print ']'

if __name__ == '__main__':
    test=LinkedDeque()
    test.insert_first(1)
    test.insert_first(2)
    test.insert_last(3)
    test.insert_last(4)
    test.delete_last()
    test.showinfo()
