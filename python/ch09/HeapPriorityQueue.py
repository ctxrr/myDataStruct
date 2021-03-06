
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

    def _upheap_nonrec(self, j):
        """non-public method which can upheap in nonrecursive way"""
        while j > 0:
            parent = self._parent(j)
            if self._data[j] < self._data[parent]:
                self._swap(j, parent)
                j = parent
            else:
                break

    def _downheap_nonrec(self, j):
        """non-public method which can downheap in nonrecursive way"""
        while self._has_left(j):
            left = self._left(j)
            small_child = left               # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                j = small_child
            else:
                break

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

    def heappushpop(self,k,v):
        if self._data[0]._key >= k:
            return (k,v)
        else:
            old = self._data[0]
            self._data[0] = self._Item(k,v)
            self._downheap(0)                            # then fix new root
            return (old._key, old._value)

    def heapreplace(self,k,v):
        old = self._data[0]
        self._data[0] = self._Item(k,v)
        self._downheap(0)                            # then fix new root
        return (old._key, old._value)

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
    #-------------------------- Import -------------- -----------------------
    from copy import deepcopy

    #-------------------------- Prepare Priority Queue-----------------------
    # init priority queue
    PQ = HeapPriorityQueue()
    PQ.add(33,'c')
    PQ.add(11,'a')
    PQ.add(2,'b')
    PQ.add(4,'d')
    PQ.add(5,'c')
    PQ.add(18,'c')
    PQ.add(24,'c')
    PQ.add(-1,'c')
    #PQ.showinfo()

    PQ1 = []
    PQ1.append((33,'c'))
    PQ1.append((11,'a'))
    PQ1.append((2,'b'))
    PQ1.append((4,'d'))
    PQ1.append((14,'f'))
    print PQ1
    PQ3 = BottomUpHeap(PQ1)
    PQ3.showinfo()

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

    #-----------C-9.26---------------------------------------------------------------
    print "Test for C-9.26................................"
    # definition of class
    class UseHeapAsStack():
        def __init__(self):
            self._index = 0
            self._data = HeapPriorityQueue()

        def __len__(self):
            return len(self._data)

        def top(self):
            return self._data.min()[1]

        def push(self,e):
            self._data.add(self._index,e)
            self._index -= 1

        def pop(self):
            return self._data.remove_min()[1]
    # test code
    pq26 = UseHeapAsStack()
    pq26.push(1)
    pq26.push(2)
    pq26.push(3)
    print 'top is:',
    print pq26.top()
    print pq26.pop(),
    print pq26.pop(),
    print pq26.pop(),
    print ''
    print ''

    #-----------C-9.27---------------------------------------------------------------
    print "Test for C-9.27................................"
    # definition of class
    class UseHeapAsQueue():
        def __init__(self):
            self._index = 0
            self._data = HeapPriorityQueue()

        def __len__(self):
            return len(self._data)

        def top(self):
            return self._data.min()[1]

        def enqueue(self,e):
            self._data.add(self._index,e)
            self._index += 1

        def dequeue(self):
            return self._data.remove_min()[1]
    # test code
    pq27 = UseHeapAsQueue()
    pq27.enqueue(1)
    pq27.enqueue(2)
    pq27.enqueue(3)
    print 'top is:',
    print pq27.top()
    print pq27.dequeue(),
    print pq27.dequeue(),
    print pq27.dequeue(),
    print ''
    print ''

    #-----------C-9.30 9.31---------------------------------------------------------------
    print "Test for C-9.30 9.31................................"
    # definition of class
    class HeapPriorityQueueRec(HeapPriorityQueue):
        """A subclass of HeapPriorityQueue but re-implement _upheap and _downheap in
           nonrecursive way.
        """
        # re-implement add and remove_min method to use nonrecursive method
        def add(self, key, value):
            """Add a key-value pair to the priority queue."""
            self._data.append(self._Item(key, value))
            self._upheap_nonrec(len(self._data) - 1)            # upheap newly added position

        def remove_min(self):
            """Remove and return (k,v) tuple with minimum key.

            Raise Empty exception if empty.
            """
            if self.is_empty():
                raise Empty('Priority queue is empty.')
            self._swap(0, len(self._data) - 1)           # put minimum item at the end
            item = self._data.pop()                      # and remove it from the list;
            self._downheap_nonrec(0)                            # then fix new root
            return (item._key, item._value)

    # test code
    pq29 = HeapPriorityQueueRec()
    pq29.add(33,'c')
    pq29.add(11,'a')
    pq29.add(2,'b')
    pq29.add(4,'d')
    pq29.add(14,'c')
    pq29.remove_min()
    pq29.showinfo()
    pq29.add(1,'c')
    pq29.showinfo()
    print ''

    #-----------C-9.35---------------------------------------------------------------
    print "Test for C-9.35................................"
    # definition of compute function
    def compute(pq,j,key):
        if j < len(pq._data) and pq._data[j]._key < key :
            return 1+compute(pq,pq._left(j),key)+compute(pq,pq._right(j),key)
        else:
            return 0

    pq35 = deepcopy(PQ)
    pq35.showinfo()
    print 'The number of entries is:',
    print compute(pq35,0,8)
    print ''

    #-----------C-9.39 9.40---------------------------------------------------------------
    print "Test for C-9.39 9.40................................"
    pq39 = deepcopy(PQ)
    pq39.showinfo()
    print pq39.heappushpop(-2,'m')
    pq39.showinfo()
    print pq39.heappushpop(8,'j')
    pq39.showinfo()
    print pq39.heapreplace(1,'z')
    pq39.showinfo()
