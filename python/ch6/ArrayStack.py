"""This module contains a class named Empty and ArrayStack"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class Full(Exception):
    """Error attempting to access an element from an full container"""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self,maxlen=None):
        """Create an empty stack."""
        self._data = []
        self._maxlen=maxlen

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data)==0

    def push(self,e):
        """Add element e to the top of the stack"""
        if self._maxlen!=None:
            if len(self._data)==self._maxlen:
                raise Full('The stack is full')
        self._data.append(e)

    def top(self):
        """Return(but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Remove and return the element from the pop of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
