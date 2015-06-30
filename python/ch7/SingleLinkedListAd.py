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

   ### With _SingleLinkedBase,ctxrr implement 3 different ADT:
    1.LinkedStack
    2.LinkedQueue
    3.CircularQueue
"""
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class _SingleLinkedBase:
    """The basic implementation of a single linked list in Header-Trailer model"""

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
        self._header  = self._Node(None,None)
        self._trailer = self._Node(None,None)
        self._header._next = self._trailer
        self._size = 0 # number of Singlelinkedlist elements

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
        start=self._header._next
        print "List Infomation:[",
        for i in range(self._size):
            print start._element,
            start=start._next
        print "]"

    def _add_front(self,e):
        """Add an element after the header node"""
        new_node = self._Node(e,self._header._next)
        self._header._next = new_node
        self._size+=1

    def _add_back(self,e):
        """Add an element in front of the trailer node"""
        new_trailer = self._Node(None,None)
        self._trailer._next = new_trailer
        self._trailer._element = e
        self._trailer = new_trailer
        self._size+=1

    def _del_front(self):
        """Remove the element after the header node"""
        if self.is_empty():
            raise Empty('List is empty')
        del_node = self._header._next
        self._header._next = del_node._next
        del_node._next = None
        del_node._element = None
        self._size-=1

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

def second_to_last(slist):
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
    else :
        return 1

if __name__ == '__main__':
    a=_SingleLinkedBase()
    a._add_front(1)
    a._add_front(2)
    a._add_back(3)
    a._add_back(4)
    a.showinfo()
    b=_SingleLinkedBase()
    b._add_front(5)
    b._add_front(6)
    b._add_back(7)
    b._add_back(8)
    b.showinfo()
#-----------R-7.1------------------------------
    second_to_last(a)
    second_to_last(b)
#-----------R-7.2------------------------------
    a_add_b=a
    for i in b:
        a_add_b._add_back(i)
    a_add_b.showinfo()
#-----------R-7.3------------------------------
    count=recursive_count(a_add_b._header)
    count_of_header_trailer=2
    print "the count of node in list exclude header and trailer is",(count-count_of_header_trailer)
