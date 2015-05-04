"""This module contains a class named Empty and ArrayQueue"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class ArrayQueue:
    """FIFO Queue implementation using a Python list as underlying storage"""
    QUEUESIZE=8
    def __init__(self):
        """Create an empty queue."""
        self._data = [None]*ArrayQueue.QUEUESIZE
        self._index=0
        self._first=0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._index - self._first

    def is_empty(self):
        """Return True if the queue is empty"""
        return (self._index - self._first)==0

    def enqueue(self,e):
        """Add element e to the back of the queue"""
        if (self._index - self._first) == len(self._data):
            self._resize(2*len(self._data))
        self._data[self._index % len(self._data)]=e
        self._index+=1
        # self._showlog()

    def first(self):
        """Return(but do not remove) the first element of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._first % len(self._data)]

    def dequeue(self):
        """Remove and return the element at the end of the queue
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        if (self._index - self._first) == len(self._data)//4:
            self._resize(len(self._data)//2)
        ret=self._data[self._first % len(self._data)]
        self._data[self._first % len(self._data)]=None
        self._first += 1
        # self._showlog()
        return ret

    def _resize(self,cap):
        """Resize the underlying array into twice size of the privious one
        """
        old = self._data
        # print 'len of old is ',len(old)
        self._data = [None] * cap
        for i in range(self.__len__()):
            self._data[i]=old[(i+self._first) % len(old)]
        self._index=self.__len__()
        self._first=0

    def _showlog(self):
        """Show the current information of the object
        """
        print 'the size of queue is',self.__len__()
        print 'the size of underlying array is',len(self._data)
        print 'the current elements in queue is',
        for i in range(self.__len__()):
            print self._data[(self._first+i) % len(self._data)],
        print ''