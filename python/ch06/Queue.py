from abc import ABCMeta,abstractmethod

class Queue(object):
    __metaclass__ = ABCMeta
    """Abstract base class representing a Queue structure."""

    # ---------- abstract methods that concrete subclass must support ----------
    @abstractmethod
    def enqueue(self,e):
        """Add element e to the back of the queue"""

    @abstractmethod
    def dequeue(self):
        """Remove and return the element at the end of the queue
        Raise Empty exception if the queue is empty
        """

    @abstractmethod
    def first(self):
        """Return(but do not remove) the first element of the queue
        Raise Empty exception if the queue is empty
        """

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the stack."""

    # ---------- concrete methods implemented in this class ----------
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0


