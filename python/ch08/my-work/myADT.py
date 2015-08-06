class myBinaryTree():
    class Node():
        def __init__(self,e):
            self._element = e
            self._left = None
            self._right = None

    class Position():
        def __init__(self,node):
            self._data = node

        def element(self):
            return self._data._element

    def __init__(self):
        self._size = 0
        self._root = None

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in self.recur(self._root):
            yield i._element

    def recur(self,node):
        if node._left:
            for i in self.recur(node._left):
                yield i
        yield node
        if node._right:
            for i in self.recur(node._right):
                yield i

    def have_root(self):
        return self._root != None

    def add_root(self,e):
        if not self.have_root():
            root = self.Node(e)
            pos = self.Position(root)
            self._root = root
            self._size += 1
            return pos

    def add_left(self,p,e):
        node = p._data
        new = self.Node(e)
        pos = self.Position(new)
        node._left = new
        self._size += 1
        return pos

    def add_right(self,p,e):
        node = p._data
        new = self.Node(e)
        pos = self.Position(new)
        node._right = new
        self._size += 1
        return pos

if __name__ == '__main__':
    a = myBinaryTree()
    #print a.have_root()
    A=a.add_root(1)
    #print a.have_root()
    B=a.add_left(A,2)
    C=a.add_right(A,3)
    D=a.add_left(B,4)
    E=a.add_right(B,5)
    F=a.add_right(C,6)
    #print len(a)
    #print a._root._element
    #print a._root._left._element
    for i in a:
        print i,
