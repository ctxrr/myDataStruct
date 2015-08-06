# coding:utf-8
"""This module contain the basic implementation of class _SingleLinkedBase which
   is improved by using Header-Trailer model instead of Head-Tail model.

   ### Head-Tail model have a lot of disadvantage,for example you have to do more job
       when you insert a new element into a singlelinkedlist base on head-tail model.

   ### But in Header-Trailer model,the header node and trailer node is always exist no matter
       the list is empty or not.So it is much more easy for user to write code and make
       less mistake.

   ### It is recommended to use Header-Trailer model all the times.Both in single list and
       double list.

   ### With _SingleLinkedBase,ctxrr re-implement 2 different ADT:
       1.LinkedStack
       2.LinkedQueue
       But there is some problem in the implementation of CircularQueue ADT,so you have to use the
       traditional head-tail model to implement it!
"""
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from ch06.Stack import Stack
from ch06.Queue import Queue
from ch06.Deque import Deque
from tools.Exceptions import Empty

#------------Class _SingleLinkedBase--------------------------------------------------------------
class _SingleLinkedBase(object):
    """The basic implementation of a single linked list in Header-Trailer model"""

    #-------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ ='_element','_next'# streamline memory usage

        def __init__(self,element,next):
            self._element = element
            self._next = next

    #------------------------- public methods -------------------------------
    def __init__ (self):
        """Create an SingleLinkedList."""
        self._header  = self._Node(None,None)
        self._trailer = self._Node(None,None)
        self._header._next = self._trailer
        self._size = 0

    def __len__ (self):
        """Return the number of elements in the SingleLinkedList."""
        return self._size

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        ptr = self._header._next
        while ptr != self._trailer:
            yield ptr._element
            ptr = ptr._next

    def is_empty(self):
        """Return True if the SingleLinkedList is empty."""
        return self._size == 0

    def showinfo(self):
        """Show the infomation of current object"""
        print "List:[",
        for i in self:
            print i,
        print "]"

    def _add_front(self,e):
        """Add an element after the header node"""
        new_node = self._Node(e,self._header._next)
        self._header._next = new_node
        self._size += 1

    def _add_back(self,e):
        """Add an element in front of the trailer node"""
        new_trailer = self._Node(None,None)
        self._trailer._next = new_trailer
        self._trailer._element = e
        self._trailer = new_trailer
        self._size += 1

    def _del_front(self):
        """Remove the element after the header node"""
        if self.is_empty():
            raise Empty('List is empty')
        del_node = self._header._next
        self._header._next = del_node._next
        element = del_node._element
        del_node._next = None
        del_node._element = None
        self._size -= 1
        return element #record the element

    def _del_back(self):
        """Remove the element before the trailer node"""
        if self.is_empty():
            raise Empty('List is empty')
        ptr=self._header
        while ptr._next._next!=self._trailer:
            ptr=ptr._next
        old = ptr._next
        ptr._next = self._trailer
        old._element = old._next = None
        self._size -=1

    def first(self):
        """Show the first element in the list"""
        if self.is_empty():
            raise Empty('List is empty')
        return self._header._next._element

    def last(self):
        """Show the last element in the list"""
        if self.is_empty():
            raise Empty('List is empty')
        ptr=self._header._next
        while ptr._next!=self._trailer:
            ptr=ptr._next
        return ptr._element

    def clear(self):
        """Clean the list into empty"""
        while self._size:
            self._del_front()

#------------Stand alone function-----------------------------------------------------------------
def second_to_last(slist):
    """Find the second_to_last element in a single linked list"""
    if len(slist) < 2:
        raise Empty("doesn't have enough element")
    ptr=slist._header._next
    while ptr._next._next!=slist._trailer:
        ptr=ptr._next
    print 'the second to last element is:',ptr._element

def recursive_count(node):
    """Use recursive way to count the number of node in list"""
    if node._next != None:
        return recursive_count(node._next)+1
    else:
        return 1

def reverse_iter(slist):
    """Reverse a single list iteratively
       p and q are used for reverse;
       r is used for record the rest of the list
    """
    p=slist._header._next
    q=p._next
    p._next=slist._trailer
    while q != slist._trailer:
        r=q._next
        q._next=p #reverse the _next pointer
        p=q
        q=r
    slist._header._next=p

def reverse_recur(walk,slist):
    """Reverse a single list recursively
    """
    if walk._next == slist._trailer:
        slist._header._next=walk
        return
    reverse_recur(walk._next,slist)
    walk._next._next=walk
    walk._next=slist._trailer

#------------Subclass------------------------------------------------------------------------------
class LinkedStack(_SingleLinkedBase,Stack):
    """LIFO Stack implementation based on a singly linked list."""

    def push(self, e):
        """Add element e to the top of the stack."""
        self._add_front(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
           Raise Empty exception if the stack is empty.
        """
        self.first()

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
           Raise Empty exception if the stack is empty.
        """
        return self._del_front()

    def showinfo(self):
        print 'LinkedStack',
        super(LinkedStack,self).showinfo()

class LinkedQueue(_SingleLinkedBase,Queue):
    """FIFO queue implementation based on a singly linked list."""

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
           Raise Empty exception if the queue is empty.
        """
        return self._del_front()

    def enqueue(self, e):
        """Add an element to the back of queue."""
        self._add_back(e)

    def showinfo(self):
        print 'LinkedQueue',
        super(LinkedQueue,self).showinfo()

class LeakyStack(LinkedStack):
    """LeakyStack works almost the same as LinkedStack.
       But the difference between them is:LeakyStack has a additional member:_capacity.
       This means when an LeakyStack instance is created,it has a max capacity,when trying
       to do push operation in an full LeakyStack list,the last one will be removed
    """
    def __init__ (self,capacity):
        """Create an SingleLinkedList."""
        self._header  = self._Node(None,None)
        self._trailer = self._Node(None,None)
        self._header._next = self._trailer
        self._size = 0
        self._capacity = capacity

    def push(self, e):
        """Add element e to the top of the stack."""
        if self._size ==self._capacity:
            self._del_back()
        self._add_front(e)

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------- Prepare some list to use-----------------------
    print "Prepare list a................................"
    a=_SingleLinkedBase()
    a._add_back(1)
    a._add_back(2)
    a._add_back(3)
    a._add_back(4)
    a._add_back(5)
    a.showinfo()
    print ''

    print "Prepare list b................................"
    b=_SingleLinkedBase()
    b._add_front(6)
    b._add_back(7)
    b._add_back(8)
    b._add_back(9)
    b._add_back(10)
    b.showinfo()
    print ''

    #-------------------------- Test code for LinkedStack --------------------------
    print "Test for LinkedStack.........................."
    ls=LinkedStack()
    ls.push(1)
    ls.push(2)
    ls.push('a')
    ls.push(3)
    ls.pop()
    ls.showinfo()
    print 'first element is',ls.first()
    print ''

    #-------------------------- Test code for LinkedQueue --------------------------
    print "Test for LinkedQueue.........................."
    lq=LinkedQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.dequeue()
    lq.enqueue('a')
    lq.showinfo()
    print ''

    #-----------R-7.1----------------------------------------------------------------
    print "Test for R-7.1................................"
    second_to_last(a)
    second_to_last(b)
    print ''

    #-----------R-7.2----------------------------------------------------------------
    print "Test for R-7.2................................"
    import copy
    a_add_b=copy.deepcopy(a)
    for i in b:
        a_add_b._add_back(i)
    a_add_b.showinfo()
    print ''

    #-----------R-7.3----------------------------------------------------------------
    print "Test for R-7.3................................"
    count=recursive_count(a_add_b._header)
    count_of_header_trailer=2
    print "the count is",(count-count_of_header_trailer)
    print ''

    #-----------C-7.28 and C-7.29----------------------------------------------------
    print "Test for C-7.28 and C-2.29...................."
    print 'going to reverse iteratively......'
    c=copy.deepcopy(a)
    c.showinfo()
    reverse_iter(c)
    c.showinfo()
    print 'going to reverse recursively......'
    d=copy.deepcopy(a)
    d.showinfo()
    reverse_recur(d._header._next,d)
    d.showinfo()

    #-----------C-7.30----------------------------------------------------------------
    print "Test for C-7.30................................"
    z=LeakyStack(5)
    z.push(1)
    z.push(2)
    z.push(3)
    z.push(4)
    z.push(5)
    z.showinfo()
    z.push(6)
    z.showinfo()
    print ''

    #-----------C-7.42----------------------------------------------------------------
    print "Test for C-7.42................................"
    # definition of ScoreBoard class
    class ScoreBoard(_SingleLinkedBase):
        class GameEntry:
            def __init__(self,name,score):
                self._name = name
                self._score = score

        def add(self,name,score):
            e = self.GameEntry(name,score)
            if self.is_empty():
                self._add_front(e)
            else:
                walk = self._header._next
                old = walk
                while walk != self._trailer:
                    if walk._element._score > e._score:
                        old = walk
                        walk = walk._next
                    else:
                        break
                new = self._Node(e,walk)
                old._next = new
                self._size += 1

        def showinfo(self):
            """Show the infomation of current object"""
            print "ScoreBoard:[",
            for i in self:
                print '(',i._name,i._score,')',
            print "]"

    # test code
    scoreboard = ScoreBoard()
    scoreboard.add('messi',100)
    scoreboard.add('CR',98)
    scoreboard.add('wayne',80)
    scoreboard.add('xavi',95)
    scoreboard.showinfo()

    #-----------P-7.45----------------------------------------------------------------
    print "Test for P-7.45................................"
    # definition of SparseArray class
    class SparseArray():
        class _Cell:
            def __init__(self,i,e):
                self._index = i
                self._element = e

        def __init__(self):
            self._data = _SingleLinkedBase()
            self._size = 0

        def __len__(self):
            return len(self._data)

        def is_empty(self):
            return len(self) == 0

        def __setitem__(self,j,e):
            # search in list to find if j already exist
            for i in self._data:
                if i._index == j:
                    i._element = e
                    return
            # j dont't exist in list,so creat a new node
            new = self._Cell(j,e)
            self._data._add_front(new)
            # update the size of instance
            if j > self._size:
                self._size = j

        def __getitem__(self,j):
            # if j is large than size,it means the given index is out of range
            if j > self._size:
                raise IndexError('index out of range!')
                return
            # search in list to find if j exist
            for i in self._data:
                if i._index == j:
                    return i._element
            # j dont't exist in list,so return None
            return None

    # test code
    sp = SparseArray()
    sp[10] = 'a'
    print sp[10]
    sp[11] = 'b'
    print len(sp)
    print sp[1]
    sp[10] = 100
    print sp[10]

