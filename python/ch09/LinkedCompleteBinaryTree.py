
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from ch08.LinkedBinaryTree import LinkedBinaryTree

#------------Class LinkedCompleteBinaryTree--------------------------------------------------------------
class LinkedCompleteBinaryTree(LinkedBinaryTree):
    def __init__(self):
        super(LinkedCompleteBinaryTree,self).__init__()
        self._last = None

    def add_root(self, e):
        """Add root node"""
        raise NotImplementedError('Do not support such operation')

    def add_left(self, p, e):
        """Add left child"""
        raise NotImplementedError('Do not support such operation')

    def add_right(self, p, e):
        """Add right child"""
        raise NotImplementedError('Do not support such operation')

    def add(self,e):
        if self._last == None:
            self._last = self._add_root(e)
        else:
            return self._add_next(self._last,e)

    def remove_last(self):
        old = self._last
        if self._last == self.root():
            self._last = None
        else:
            self._delete_front(self._last)
        self.delete(old)

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

    def last(self):
        return self._last.element()

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


