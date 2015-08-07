
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from PriorityQueueBase import PriorityQueueBase
from tools.Exceptions import Empty

#------------Class HeapPriorityQueue--------------------------------------------------------------
class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""

    #------------------------------ nonpublic behaviors ------------------------------
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)     # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)    # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)             # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left               # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)    # recur at position of small child

    #------------------------------ public behaviors ------------------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)            # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)           # put minimum item at the end
        item = self._data.pop()                      # and remove it from the list;
        self._downheap(0)                            # then fix new root
        return (item._key, item._value)

    def showinfo(self):
        print '[',
        for i in self._data:
            print i,
        print ']'

#------------Class HeapPriorityQueue--------------------------------------------------------------
class BottomUpHeap(HeapPriorityQueue): # base class defines _Item

    def __init__ (self, contents=()):
        """Create a new priority queue.
        By default, queue will be empty. If contents is given, it should be as an
        iterable sequence of (k,v) tuples specifying the initial contents.
        """
        self._data = [ self._Item(k,v) for k,v in contents ] # empty by default
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1) # start at PARENT of last leaf
        for j in range(start, -1, -1): # going to and including the root
            self._downheap(j)

#------------Class MaxOrientHeap --------------------------------------------------------------
class MaxOrientHeap(HeapPriorityQueue): # base class defines _Item
    """A max-oriented priority queue implemented with a binary heap.
         1.MaxOrientHeap is inherrited from HeapPriorityQueue,but modify the
           method of _upheap and _downheap.
         2.The old method min and remove_min will inherrited from super class
           but it should not exist in MaxOrientHeap class so any call of them
           will raise an NotImplementedError
         3.Add 2 new method:max and remove_max which almost work the same as
           min and remove_min
    """

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)             # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left               # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    small_child = right
            if self._data[small_child] > self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)    # recur at position of small child


    def max(self):
        """Return but do not remove (k,v) tuple with maximum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_max(self):
        """Remove and return (k,v) tuple with maximum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)           # put maximum item at the end
        item = self._data.pop()                      # and remove it from the list;
        self._downheap(0)                            # then fix new root
        return (item._key, item._value)

    def min(self):
        raise NotImplementedError('Not support in this class any more')

    def remove_min(self):
        raise NotImplementedError('Not support in this class any more')

#------------Stand alone function--------------------------------------------------------------
def pq_sort(C):
    """Sort a collection of elements stored in a positional list."""
    n = len(C)
    P = HeapPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element) # use element as key and value
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v) # store smallest remaining element in C

#------------ Test code--------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------- Prepare Priority Queue-----------------------
    # init priority queue
    PQ = HeapPriorityQueue()
    PQ.add(33,'c')
    PQ.add(11,'a')
    PQ.add(2,'b')
    PQ.add(4,'d')
    PQ.add(14,'c')
    #PQ.showinfo()

    PQ1 = BottomUpHeap()
    PQ1.add(33,'c')
    PQ1.add(11,'a')
    PQ1.add(2,'b')
    PQ1.add(4,'d')
    PQ1.add(14,'c')
    #PQ1.showinfo()

    PQ2 = MaxOrientHeap()
    PQ2.add(33,'c')
    PQ2.add(11,'a')
    PQ2.add(2,'b')
    PQ2.add(4,'d')
    PQ2.add(14,'c')
    #PQ2.showinfo()

    #-------------------------- Test code for function pq_sort --------------------
    print "Test for function pq_sort....................."
    from ch07.PositionalList import PositionalList
    a = PositionalList()
    a.add_first(7)
    a.add_first(2)
    a.add_first(9)
    a.add_first(5)
    a.add_first(4)
    print 'Before:',
    a.showinfo()
    pq_sort(a)
    print 'After:',
    a.showinfo()
    print ''

    #-----------R-9.4----------------------------------------------------------------
    print "Test for R-9.4................................"
    """ use list to implement time stamp as a key in priority queue
        so you don't need to convert the type of time stamp into int
    """
    p4 = HeapPriorityQueue()
    p4.add([20,20,00],'CN001')
    p4.add([10,20,00],'US001')
    p4.add([19,10,00],'JP001')
    p4.add([8,20,00],'CN002')
    p4.add([8,19,00],'US002')
    # for debug
    #for i in p4._data:
        #print i._value,
    print 'Next Flight is:',p4.min()[1]
    print ''

    #-----------R-9.13---------------------------------------------------------------
    #Illustrate the execution of the in-place heap-sort algorithm on the following
    #input sequence: (2, 5, 16, 4, 10, 23, 39, 18, 26, 15).
    """
    Step 1:
       a.(2, 5, 16, 4, 10, 23, 39, 18, 26, 15).
       b.(5, 16, 4, 10, 23, 39, 18, 26, 15, 2).
       c.(16, 4, 10, 23, 39, 18, 26, 15, 2, 5).
       d.(4, 10, 23, 39, 18, 26, 15, 2, 5, 16).
       e.(10, 23, 39, 18, 26, 15, 2, 4, 16, 5).
       f.(23, 39, 18, 26, 15, 2, 4, 16, 5, 10).
       g.(39, 18, 26, 15, 2, 4, 16, 5, 10, 23).
       h.(18, 26, 15, 2, 4, 16, 5, 10, 23, 39).
       i.(26, 15, 2, 4, 16, 5, 10, 23, 39, 18).
       j.(15, 2, 4, 16, 5, 10, 23, 39, 18, 26).
       k.(2, 4, 16, 5, 10, 23, 39, 18, 26, 15).
    Step 2:
       l.(4, 5, 16, 15, 10, 23, 39, 18, 26, 2).
       m.(5, 10, 16, 26, 15, 23, 39, 18, 2, 4).
       n.(10, 15, 16, 26, 18, 23, 39, 2, 4, 5).
       o.(15, 18, 16, 26, 39, 23, 2, 4, 5, 10).
       p.(16, 18, 23, 26, 39, 2, 4, 5, 10, 15).
       q.(18, 26, 23, 39, 2, 4, 5, 10, 15, 16).
       r.(23, 26, 39, 2, 4, 5, 10, 15, 16, 18).
       s.(26, 39, 2, 4, 5, 10, 15, 16, 18, 23).
       t.(39, 2, 4, 5, 10, 15, 16, 18, 23, 26).
       u.(2, 4, 5, 10, 15, 16, 18, 23, 26, 39).
    """

