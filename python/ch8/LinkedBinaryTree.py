
#------------Import packet-----------------------------------------------------------------------
from BinaryTree import BinaryTree
import copy

#------------Class LinkedBinaryTree--------------------------------------------------------------
class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right' # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

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

    #-------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0
        self._traveral = 'NLR'

    #-------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count

    def is_left_leaf(self, p):
        """Return True if Position p is the left leaf of its parent."""
        return self.is_leaf(p) and p==self.left(self.parent(p))

    def is_right_leaf(self, p):
        """Return True if Position p is the right leaf of its parent."""
        return self.is_leaf(p) and p==self.right(self.parent(p))

    def add_root(self, e):
        """Add root node"""
        return self._add_root(e)

    def add_left(self, p, e):
        """Add left child"""
        return self._add_left(p,e)

    def add_right(self, p, e):
        """Add right child"""
        return self._add_right(p,e)

    def replace(self, p, e):
        """Replace the element stored in p into e"""
        return self._replace(p,e)

    def delete(self, p):
        """Delete the node p"""
        return self._delete(p)

    #-------------------------- override accessors methods -----------------
    def positions(self):
        """Generate an iteration of the tree's positions."""
        if not self.is_empty():
            if self._traveral == 'NLR':
                for p in self._subtree_preorder(self.root()):
                    yield p
            if self._traveral == 'LNR':
                for p in self._subtree_inorder(self.root()):
                    yield p
            if self._traveral == 'LRN':
                for p in self._subtree_postorder(self.root()):
                    yield p

    # --------------------- additional public methods ---------------------
    def addsibling(self,p,e):
        """Add a new Position representing p's sibling if p don't have sibling"""
        if self.sibling(p):
            print 'already have sibling ,operation forbidden!'
            return
        else:
            parent = self.parent(p)
            if p == self.left(parent):
                return self._add_right(parent,e)         # possibly None
            else:
                return self._add_left(parent,e)

    def set_traversal(self,mode):
        """Set the traversal type"""
        if mode == 'NLR' or mode == 'LRN' or mode == 'LNR':
            self._traveral = mode
        else:
            print 'wrong parameter,keep the traversal mode unchanged'

    def showtraversal(self):
        """Show the infomation of the current tree"""
        print 'BinaryTree traversal in way',self._traveral,':[',
        for i in self:
            print i,
        print ']'

    #-------------------------- nonpublic mutators --------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)                  # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)                 # node is its parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent   # child's grandparent becomes parent
        if node is self._root:
            self._root = child             # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node              # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():         # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():         # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None             # set t2 instance to empty
            t2._size = 0

#------------Stand alone function--------------------------------------------------------------
def preorder_indent(T, p, d):
    print(2*d*' ' + str(p.element())) # use depth for indentation
    for c in T.children(p):
        preorder_indent(T, c, d+1)

def preorder_label(T, p, d, path):
    label ='.'.join(str(j) for j in path) # displayed labels are one-indexed
    print 2*d*' '+ label,p.element()
    path.append(1) # path entries are zero-indexed
    for c in T.children(p):
        preorder_label(T, c, d+1, path) # child depth is d+1
        path[-1] += 1
    path.pop()

def arithmetic_expression(T,p):
    """Caculate the result of an arithmetic expression implemented by a BinaryTree"""
    if T.is_leaf(p):
        return p.element()
    else:
        if p.element() =='+':
            return arithmetic_expression(T,T.left(p)) + arithmetic_expression(T,T.right(p))
        if p.element() =='-':
            return arithmetic_expression(T,T.left(p)) - arithmetic_expression(T,T.right(p))
        if p.element() =='*':
            return arithmetic_expression(T,T.left(p)) * arithmetic_expression(T,T.right(p))
        if p.element() =='/':
            return arithmetic_expression(T,T.left(p)) / arithmetic_expression(T,T.right(p))

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------- Init a tree for further use --------------------
    T = LinkedBinaryTree()
    ro = T.add_root(0)
    r1 = T.add_left(ro,1)
    r2 = T.add_right(ro,2)
    r3 = T.add_left(r1,3)
    r4 = T.add_right(r1,4)
    r5 = T.add_left(r2,5)
    r6 = T.add_right(r2,6)
    r7 = T.add_left(r3,7)
    r8 = T.add_right(r3,8)
    r9 = T.add_right(r4,9)
    r10 = T.add_left(r6,10)
    r11 = T.add_right(r6,11)
    r12 = T.add_left(r8,12)
    r13 = T.add_left(r10,13)
    r14 = T.add_right(r11,14)
    print ''

    #-------------------------- Test code for 3 different way of traversal --------------------
    print "Test for different traversal way.........................."
    t1 = copy.deepcopy(T)
    t1.showtraversal()
    t1.set_traversal('LNR')
    t1.showtraversal()
    t1.set_traversal('LRN')
    t1.showtraversal()
    print ''

    #-------------------------- Test code for traversal of table of contents --------------------
    print "Test for print table of contents.........................."
    table = LinkedBinaryTree()
    ta0 = table.add_root('Paper')
    ta1 = table.add_left(ta0,'Title')
    ta2 = table.add_right(ta0,'Abstract')
    ta3 = table.add_left(ta2,'1.1')
    ta4 = table.add_right(ta2,'1.2')
    # tradition way,waste of time
    for i in table.preorder():
        print(2*table.depth(i)*' '+str(i.element()))
    # more efficient way
    preorder_indent(table,ta0,0)

    path=[2,3]
    preorder_label(table,ta0,0,path)
    print ''

    #-----------R-8.5----------------------------------------------------------------
    print "Test for R-8.5................................"
    t2 = copy.deepcopy(T)
    leftcount = 0
    rightcount = 0
    for i in t2.inorder():
        if t2.is_left_leaf(i):
            leftcount += 1
        if t2.is_right_leaf(i):
            rightcount += 1
    print 'left is:',leftcount,'.','right is:',rightcount
    print ''

    #-----------R-8.6----------------------------------------------------------------
    print "Test for R-8.6................................"
    t3 = copy.deepcopy(T)
    tr12 = copy.deepcopy(r12)

    singlecount = 0
    for i in t3.inorder():
        if t3.left(i) == None and t3.right(i) != None:
            t3.add_left(i,'Orz')
            singlecount += 1
        elif t3.right(i) == None and t3.left(i) != None:
            t3.add_right(i,'Orz')
            singlecount += 1
    print 'use proper tree represent improper tree: add addtional',singlecount,'nodes'
    t3.showtraversal()
    print ''

    #-----------R-8.13----------------------------------------------------------------
    print "Test for R-8.13................................"
    arith = LinkedBinaryTree()
    ari0 = arith.add_root('*')
    ari1 = arith.add_left(ari0,'+')
    ari2 = arith.add_right(ari0,'-')
    ari3 = arith.add_left(ari1,2)
    ari4 = arith.add_right(ari1,1)
    ari5 = arith.add_left(ari2,5)
    ari6 = arith.add_right(ari2,2)
    print 'expression info:',
    for i in arith.inorder():
        print i.element(),
    print ''
    print 'result is:',arithmetic_expression(arith,ari0)
    print ''


