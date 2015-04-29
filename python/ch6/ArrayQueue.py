"""This module contains a class named Empty and ArrayQueue"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayQueue:
    """FIFO Queue implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty queue."""
        self._data = []
        self._index=0

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._data)-self._index

    def is_empty(self):
        """Return True if the queue is empty"""
        return (len(self._data)-self._index)==0

    def enqueue(self,e):
        """Add element e to the back of the queue"""
        self._data.append(e)

    def first(self):
        """Return(but do not remove) the first element of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._index]

    def dequeue(self):
        """Remove and return the element at the end of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        self._index += 1
        return self._data[self._index-1]
