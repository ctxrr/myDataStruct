
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from LinkedCompleteBinaryTree import LinkedCompleteBinaryTree
from tools.Exceptions import Empty

#------------Class LinkedHeap--------------------------------------------------------------
class LinkedHeap(LinkedCompleteBinaryTree):

    def add(self,k,v):
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


    def _upheap(self,p):
        parent = self.parent(p)
        if parent and p._node._element[0]<parent._node._element[0]:
            self._swap(p, parent)
            self._upheap(parent)             # recur at position of parent

    def _swap(self, p, q):
        """Swap the elements at position p and q."""
        p._node._element,q._node._element = q._node._element,p._node._element

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


#------------ Test code--------------------------------------------------------------
if __name__ == '__main__':
    m = LinkedHeap()
    m.add(1,'a')
    m.add(2,'b')
    m.add(3,'c')
    m.add(-1,'d')
    print m.min()
    m.remove_min()
    m.breadthfirsttraversal()
    m.add(9,'a')
    m.breadthfirsttraversal()
    m.remove_min()
    m.breadthfirsttraversal()
    m.remove_min()
    m.breadthfirsttraversal()
    m.remove_min()
    m.breadthfirsttraversal()
    m.remove_min()
    m.breadthfirsttraversal()
