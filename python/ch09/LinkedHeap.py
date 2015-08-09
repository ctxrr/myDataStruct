
#------------Import packet-----------------------------------------------------------------------
import sys
sys.path.append('..')
from ch08.LinkedBinaryTree import LinkedBinaryTree

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
                self.addsibling(walk,e)
            else:
                walk = self.sibling(walk)
                while self.left(walk) != None:
                    walk = self.left(walk)
                self._last = self._add_left(walk,e)

    def last(self):
        return self._last.element()

if __name__ == '__main__':
    t = LinkedCompleteBinaryTree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.add(10)
    t.add(11)
    t.add(12)
    t.add(13)
    t.add(14)
    t.breadthfirsttraversal()
    print t.last()

