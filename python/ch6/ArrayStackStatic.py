"""This module contains a class named Empty and ArrayStackStatic"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """Error attempting to access an element from an full container"""
    pass

class ArrayStackStatic:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self,n):
        """Create an empty stack."""
        self._data = [None]*n
        self._n=n
        self._top=0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._n

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._top==0

    def push(self,e):
        """Add element e to the top of the stack"""
        if self._top==(self._n):
            raise Full("Stack is full")
        self._top+=1
        self._data[self._top-1]=e

    def top(self):
        """Return(but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._top-1]

    def pop(self):
        """Remove and return the element from the pop of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        self._top-=1
        return self._data[self._top]
