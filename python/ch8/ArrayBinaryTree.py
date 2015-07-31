
#------------Import packet-----------------------------------------------------------------------
from BinaryTree import BinaryTree
import copy

#------------Class Arraybinarytree--------------------------------------------------------------
class ArrayBinaryTree(BinaryTree):
    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_index', '_valid' # streamline memory usage

        def __init__(self, element, index, valid = True):
            self._element = element
            self._index = index
            self._valid = valid
    #-------------------------- nested Position class --------------------------
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def index(self):
            """Return the index stored at this Position."""
            return self._node._index

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
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #-------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._array = []
        self._size = 0

    #-------------------------- public accessors --------------------------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        if len(self):
            return self._make_position(self._array[0])
        else:
            return None

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        node = self._validate(p)
        node_index = node._index
        return self._make_position(self._array[(node_index-1)/2])

    def num_children(self, p):
        """Return the number of children that Position p has."""
        count = 0
        if self.left(p):
            count += 1
        if self.right(p):
            count += 1
        return count

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        node = self._validate(p)
        left_index = node._index*2+1
        if self.index_valid(left_index)==1:
            return self._make_position(self._array[left_index])
        else:
            return None

    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        node = self._validate(p)
        right_index = node._index*2+2
        if self.index_valid(right_index)==1:
            return self._make_position(self._array[right_index])
        else:
            return None

    def is_left_leaf(self, p):
        """Return True if Position p is the left leaf of its parent."""
        pass

    def is_right_leaf(self, p):
        """Return True if Position p is the right leaf of its parent."""
        pass

    def add_root(self, e):
        """Add root node"""
        if self.root():
            raise ValueError('Root exists')
        else:
            node = self._Node(e,0)
            self._array.append(node)
            self._size += 1
            return self._make_position(node)

    def add_left(self, p, e):
        """Add left child"""
        node = self._validate(p)
        left_index = node._index*2+1
        ret = self.index_valid(left_index)
        if ret:
            raise ValueError('Left child exists')

        elif ret == 0:
            for i in range(len(self._array),left_index):
                self._array.append(self._Node(None,i,False))
            self._array.append(self._Node(e,left_index))
        else:                                   #ret == -1
            self._array[left_index]._element = e
            self._array[left_index]._valid = True
        self._size += 1
        return self._make_position(self._array[left_index])

    def add_right(self, p, e):
        """Add right child"""
        node = self._validate(p)
        right_index = node._index*2+2
        ret = self.index_valid(right_index)
        if ret:
            raise ValueError('Right child exists')

        elif ret == 0:
            for i in range(len(self._array),right_index):
                self._array.append(self._Node(None,i,False))
            self._array.append(self._Node(e,right_index))
        else:                                   #ret == -1
            self._array[right_index]._element = e
            self._array[right_index]._valid = True
        self._size += 1
        return self._make_position(self._array[right_index])

    def replace(self, p, e):
        """Replace the element stored in p into e"""
        pass

    def delete(self, p):
        """Delete the node p"""
        pass

    # --------------------- additional public methods ---------------------
    def index_valid(self,index):
        """Test if the index is valid"""
        if index >= len(self._array):
            return 0
        if not self._array[index]._valid:
            return -1
        return 1

    def pretraversal(self):
        """Show the infomation of the current tree in preorder traversal"""
        print 'Preorder traversal :[',
        for i in self.preorder():
            print i.element(),
        print ']'

    def intraversal(self):
        """Show the infomation of the current tree in inorder traversal"""
        print 'Inorder traversal  :[',
        for i in self.inorder():
            print i.element(),
        print ']'

    def posttraversal(self):
        """Show the infomation of the current tree in postorder traversal"""
        print 'Postorder traversal:[',
        for i in self.postorder():
            print i.element(),
        print ']'

    def breadthfirsttraversal(self):
        """Show the infomation of the current tree in breadthfirst traversal"""
        print 'BinaryTree traversal in breadth first order:[',
        for i in self.breadthfirst():
            print i.element(),
        print ']'

#------------Stand alone function--------------------------------------------------------------

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    T = ArrayBinaryTree()

    r0 = T.add_root(0)
    r1 = T.add_left(r0,1)
    r2 = T.add_right(r0,2)
    r3 = T.add_left(r1,3)
    r4 = T.add_right(r1,4)
    r5 = T.add_left(r2,5)
    r6 = T.add_right(r2,6)
    r7 = T.add_left(r3,7)
    r8 = T.add_right(r3,8)
    r10 = T.add_right(r4,10)
    r13 = T.add_left(r6,13)
    r14 = T.add_right(r6,14)
    r17 = T.add_left(r8,17)
    r27 = T.add_left(r13,27)
    r28 = T.add_right(r13,28)
    r29 = T.add_left(r14,29)
    r30 = T.add_right(r14,30)
    print ''

    t1 = copy.deepcopy(T)
    t1.pretraversal()
    t1.intraversal()
    t1.posttraversal()

