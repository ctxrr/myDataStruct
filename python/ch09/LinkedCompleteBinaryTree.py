
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from ch08.LinkedBinaryTree import LinkedBinaryTree
from tools.Exceptions import Empty

#------------Class LinkedCompleteBinaryTree--------------------------------------------------------------
class LinkedCompleteBinaryTree(LinkedBinaryTree):
    """Linked representation of a complete binary tree structure.

       1.Unlike BinaryTree,complete binary tree ADT do not support
         method such as add_root add_left etc. Any call of them will
         raise an NotImplementedError
       2.Instead , LinkedCompleteBinaryTree support 3 new method:
         @'add':to add it to the end of the tree.
         @'remove_last':is the reverse operation of 'add'
         @'last':return the last node in the tree
    """

    def add_root(self, e):
        """Add root node"""
        raise NotImplementedError('Do not support such operation')

    def add_left(self, p, e):
        """Add left child"""
        raise NotImplementedError('Do not support such operation')

    def add_right(self, p, e):
        """Add right child"""
        raise NotImplementedError('Do not support such operation')

    #-------------------------- public method --------------------------
    def __init__(self):
        super(LinkedCompleteBinaryTree,self).__init__()
        self._last = None

    def add(self,e):
        """Add an new node to the end of the tree"""
        if self._last == None:
            self._last = self._add_root(e)
        else:
            return self._add_next(self._last,e)

    def remove_last(self):
        """Remove the node at the end of the tree"""
        old = self._last
        if self._last == self.root():
            self._last = None
        else:
            self._delete_front(self._last)
        self.delete(old)

    def last(self):
        """Return the last node at the tree"""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        return self._last.element()

    #-------------------------- nonpublic mutators --------------------------
    def _add_next(self,p,e):
        if p == self.root():
            self._last = self._add_left(p,e)
        else:
            walk = p
            while walk != self.left(self.parent(walk)):
                walk = self.parent(walk)
                if walk == self.root():
                    while self.left(walk) != None:
                        walk = self.left(walk)
                    self._last = self._add_left(walk,e)
                    return
            if self.sibling(walk) == None:
                p = self.addsibling(walk,e)
                self._last = p
            else:
                walk = self.sibling(walk)
                while self.left(walk) != None:
                    walk = self.left(walk)
                self._last = self._add_left(walk,e)

    def _delete_front(self,p):
        walk = p
        while walk == self.left(self.parent(walk)):
            walk = self.parent(walk)
            if walk == self.root():
                while self.right(walk) != None:
                    walk = self.right(walk)
                self._last = walk
                return
        if self.is_leaf(self.sibling(walk)):
            self._last = self.sibling(walk)
        else:
            walk = self.sibling(walk)
            while self.right(walk) != None:
                walk = self.right(walk)
            self._last = walk

#------------ Test code--------------------------------------------------------------
if __name__ == '__main__':
    t = LinkedCompleteBinaryTree()
    for i in range(16):
        t.add(i)
    t.breadthfirsttraversal()
    print t.last()

    t.remove_last()
    t.breadthfirsttraversal()
    print t.last()

    t.remove_last()
    t.breadthfirsttraversal()
    print t.last()

    t.remove_last()
    t.breadthfirsttraversal()
    print t.last()

    t.add(17)
    t.breadthfirsttraversal()
    print t.last()
    for i in range(13):
        t.remove_last()
    t.breadthfirsttraversal()
    t.remove_last()
    t.breadthfirsttraversal()


