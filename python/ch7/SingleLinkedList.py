# coding:utf-8
"""This module contain the basic implementation of class _SingleLinkedList
    With _SingleLinkedList , DSAP implement 3 different ADT:
    1.LinkedStack
    2.LinkedQueue
    3.CircularQueue
"""
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class _SingleLinkedList:
    """The basic implementation of a single linked list"""

    #-------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ ='_element','_next'# streamline memory usage

        def __init__(self,element,next):
            self._element = element # reference to user’s element
            self._next = next # reference to next node

    #------------------------------- public methods -------------------------------
    def __init__ (self):
        """Create an SingleLinkedList."""
        self._head = None
        self._tail = None
        self._size = 0 # number of Singlelinkedlist elements

    def __len__ (self):
        """Return the number of elements in the SingleLinkedList."""
        return self._size

    def is_empty(self):
        """Return True if the SingleLinkedList is empty."""
        return self._size == 0

    def showinfo(self):
        """Show the infomation of current object"""
        start=self._head
        print "List Infomation:[",
        for i in range(self._size):
            print start._element,
            start=start._next
        print "]"

class LinkedStack(_SingleLinkedList):
    """LIFO Stack implementation based on a singly linked list."""

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next # bypass the former top node
        self._size -= 1
        return answer

class LinkedQueue(_SingleLinkedList):
    """FIFO queue implementation based on a singly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element # front

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty(): # special case as queue is empty
            self._tail = None # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None) # node will be new tail node
        if self.is_empty():
            self._head = newest # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest # update reference to tail node
        self._size += 1

class CircularQueue(_SingleLinkedList):
    """Circular queue implementation based on a singly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element # front

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._tail._next = self._head
        self._size -= 1
        if self.is_empty(): # special case as queue is empty
            self._tail = None # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None) # node will be new tail node
        if self.is_empty():
            self._head = newest # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest # update reference to tail node
        self._tail._next = self._head
        self._size += 1

    def rotate(self):
        if self._size>0:
            self._tail = self._tail._next
            self._head = self._head._next


if __name__ == '__main__':
    
    #-------------------------- Test code for LinkedStack --------------------------
    print "Test for LinkedStack........."
    ls=LinkedStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.pop()
    ls.showinfo()

    #-------------------------- Test code for LinkedQueue --------------------------
    print "Test for LinkedQueue........."
    lq=LinkedQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.dequeue()
    lq.showinfo()

    #-------------------------- Test code for Circularqueue --------------------------
    print "Test for Circularqueue........."
    cq=CircularQueue()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.showinfo()
    cq.rotate()
    cq.showinfo()
    cq.dequeue()
    cq.showinfo()
