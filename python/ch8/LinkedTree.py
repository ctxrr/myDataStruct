
#------------Import packet-----------------------------------------------------------------------
from Tree import Tree

class LinkedTree(Tree):
    """Linked representation of a general tree structure."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        #__slots__ = '_element', '_parent', '_children' # streamline memory usage

        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

    #-------------------------- nested Position class --------------------------
    class Position(Tree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    #------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #-------------------------- general tree constructor --------------------------
    def __init__(self):
        self._root = None
        self._size = 0

    #-------------------------- public accessors --------------------------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        """Return the number of children that Position p has."""
        node = self._validate(p)
        return len(node._children)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        node = self._validate(p)
        for i in node._children:
            yield self._make_position(i)

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def add_root(self,e):
        new = self._Node(e)
        self._root = new
        self._size += 1
        return self._make_position(self._root)

    def add_child(self,e,p):
        node = self._validate(p)
        new = self._Node(e,node)
        node._children.append(new)
        self._size += 1
        return self._make_position(new)

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    T = LinkedTree()
    r0 = T.add_root(0)
    r1 = T.add_child(1,r0)
    r2 = T.add_child(2,r0)
    r3 = T.add_child(3,r0)
    r4 = T.add_child(4,r1)
    r5 = T.add_child(5,r2)
    #print T.height(r3)
    #print T.depth(r1)
    for i in T:
        print i,
    print ''

    for i in T.postorder():
        print i.element(),
    print ''

    for i in T.preorder():
        print i.element(),
    print ''

    for i in T.breadthfirst():
        print i.element(),
