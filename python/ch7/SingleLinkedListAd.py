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
#------------Class Empty--------------------------------------------------------------------------
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

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

#------------Subclass------------------------------------------------------------------------------
class LinkedStack(_SingleLinkedBase):
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
        self._del_front()

    def showinfo(self):
        print 'LinkedStack',
        super(LinkedStack,self).showinfo()

class LinkedQueue(_SingleLinkedBase):
    """FIFO queue implementation based on a singly linked list."""

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
           Raise Empty exception if the queue is empty.
        """
        self._del_front()

    def enqueue(self, e):
        """Add an element to the back of queue."""
        self._add_back(e)

    def showinfo(self):
        print 'LinkedQueue',
        super(LinkedQueue,self).showinfo()

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':

    a=_SingleLinkedBase()
    a._add_front(1)
    a._add_front(2)
    a._add_back(3)
    a._add_back(4)
    # a.showinfo()
    import copy
    c=copy.deepcopy(a)
    print '1'
    c.showinfo()
    c.clear()
    c.showinfo()

    b=_SingleLinkedBase()
    b._add_front(5)
    b._add_front(6)
    b._add_back(7)
    b._add_back(8)
    #b.showinfo()

    #-------------------------- Test code for LinkedStack --------------------------
    print "Test for LinkedStack.........................."
    ls=LinkedStack()
    ls.push(1)
    ls.push(2)
    ls.push('a')
    ls.push(3)
    ls.pop()
    ls.showinfo()
    print ls.first()

    #-------------------------- Test code for LinkedQueue --------------------------
    print "Test for LinkedQueue.........................."
    lq=LinkedQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.dequeue()
    lq.enqueue('a')
    lq.showinfo()
    print lq.first()

    #-----------R-7.1----------------------------------------------------------------
    print "Test for R-7.1................................"
    second_to_last(a)
    second_to_last(b)

    #-----------R-7.2----------------------------------------------------------------
    print "Test for R-7.2................................"
    a_add_b=a
    for i in b:
        a_add_b._add_back(i)
    a_add_b.showinfo()

    #-----------R-7.3----------------------------------------------------------------
    print "Test for R-7.3................................"
    count=recursive_count(a_add_b._header)
    count_of_header_trailer=2
    print "the count of node in list exclude header and trailer is",(count-count_of_header_trailer)

