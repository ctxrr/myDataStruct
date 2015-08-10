
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from LinkedCompleteBinaryTree import LinkedCompleteBinaryTree
from tools.Exceptions import Empty

#------------Class LinkedHeap--------------------------------------------------------------
class LinkedHeap(LinkedCompleteBinaryTree):
    """A min-oriented priority queue implemented with a linked-based binary heap."""

    #-------------------------- public method --------------------------
    def add(self,k,v):
        """Add a key-value pair to the priority queue."""
        super(LinkedHeap,self).add((k,v))
        self._upheap(self._last)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        return self.root().element()[1]

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(self._last,self.root())
        self.remove_last()
        self._downheap(self.root())                            # then fix new root

    #-------------------------- nonpublic mutators --------------------------
    def _swap(self, p, q):
        """Swap the elements at position p and q."""
        p._node._element,q._node._element = q._node._element,p._node._element

    def _upheap(self,p):
        parent = self.parent(p)
        if parent and p._node._element[0]<parent._node._element[0]:
            self._swap(p, parent)
            self._upheap(parent)             # recur at position of parent

    def _downheap(self, p):
        if p:
            left = self.left(p)               # although right may be smaller
            right = self.right(p)
            if left:
                small_child = left               # although right may be smaller
                if right:
                    if right._node._element[0] < left._node._element[0]:
                        small_child = right
                if small_child._node._element[0] < p._node._element[0]:
                    self._swap(p, small_child)
                    self._downheap(small_child)    # recur at position of small child

#------------ Test code--------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------- Prepare Priority Queue-----------------------
    PQ = LinkedHeap()
    PQ.add(1,'a')
    PQ.add(2,'b')
    PQ.add(3,'c')
    PQ.add(-1,'d')
    print ''

    #-----------C-9.32---------------------------------------------------------------
    print "Test for C-9.32................................"
    PQ.remove_min()
    PQ.breadthfirsttraversal()
    PQ.add(9,'a')
    PQ.breadthfirsttraversal()
    PQ.remove_min()
    PQ.breadthfirsttraversal()
    PQ.remove_min()
    PQ.breadthfirsttraversal()
    PQ.remove_min()
    PQ.breadthfirsttraversal()
    print ''


