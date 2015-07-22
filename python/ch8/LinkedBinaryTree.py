
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

    def swap(self,p,q):
        """Swap the node p and q"""
        return self._swap(p,q)

    def delete(self, p):
        """Delete the node p"""
        return self._delete(p)

    def delete_subtree(self,p):
        """Delete the subtrees of node p"""
        return self._delete_subtree(p)

    #-------------------------- override accessors methods -----------------
    def positions(self):
        """Generate an iteration of the tree's positions."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
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

    def pretraversal(self):
        """Show the infomation of the current tree in preorder traversal"""
        print 'BinaryTree traversal in preorder :[',
        for i in self.preorder():
            print i.element(),
        print ']'

    def intraversal(self):
        """Show the infomation of the current tree in inorder traversal"""
        print 'BinaryTree traversal in inorder  :[',
        for i in self.inorder():
            print i.element(),
        print ']'

    def posttraversal(self):
        """Show the infomation of the current tree in postorder traversal"""
        print 'BinaryTree traversal in postorder:[',
        for i in self.postorder():
            print i.element(),
        print ']'

    def breadthfirsttraversal(self):
        """Show the infomation of the current tree in breadthfirst traversal"""
        print 'BinaryTree traversal in breadth first order:[',
        for i in self.breadthfirst():
            print i.element(),
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

    def _swap(self,p,q):
        """Swap the node p and q"""
        nodep = self._validate(p)
        nodeq = self._validate(q)
        parent_p = self._validate(self.parent(p))
        left_p = self._validate(self.left(p))
        right_p = self._validate(self.right(p))
        parent_q = self._validate(self.parent(q))
        left_q = self._validate(self.left(q))
        right_q = self._validate(self.right(q))

        p._parent = parent_q
        q._parent = parent_p
        p._left = left_q
        p._right = right_q
        q._left = left_p
        q._right = right_p

        if parent_p:
            if nodep == parent_p._left:
                parent_p._left = nodeq
            else:
                parent_p._right = nodeq

        if parent_q:
            if nodeq == parent_q._left:
                parent_q._left = nodep
            else:
                parent_q._right = nodep

        if left_p:
            left_p._parent = nodeq

        if right_p:
            right_p._parent = nodeq

        if left_q:
            left_q._parent = nodep

        if right_q:
            right_q._parent = nodep
        #pass

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

    def _delete_subtree(self,p):
        """Delete the subtrees of node at Position p.

        Return the number of element that had been deleted.
        """
        rmsize = 0
        node = self._validate(p)
        #for i in self.preorder(p):
        for i in self._subtree_postorder(p):
            rmsize += 1
        rmsize -= 1
        node._left = None
        node._right = None
        self._size -= rmsize
        return rmsize

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
    print 2*d*' ' + str(p.element()) # use depth for indentation
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

def parenthesize(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print p.element(), # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep ='(' if first_time else ',' # determine proper separator
            print sep,
            first_time = False # any future passes will not be the first
            parenthesize(T, c) # recur on child
        print ')', # include closing parenthesis

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

def sumIPL(T,p,value):
    """Caculate the internal path length of T"""
    if T.num_children(p)==0:
        return 0
    else:
        return (value + (sumIPL(T,T.left(p),value+1) if T.left(p) else 0) + (sumIPL(T,T.right(p),value+1) if T.right(p) else 0))

def sumEPL(T,p,value):
    """Caculate the external path length of T"""
    if T.num_children(p)==0:
        return value
    else:
        return (sumEPL(T,T.left(p),value+1) if T.left(p) else 0) + (sumEPL(T,T.right(p),value+1) if T.right(p) else 0)

def numIN(T,p):
    """Caculate the internal node number of T"""
    if T.num_children(p)==0:
        return 0
    else:
        return 1 + (numIN(T,T.left(p)) if T.left(p) else 0) + (numIN(T,T.right(p)) if T.right(p) else 0)

def numEN(T,p):
    """Caculate the external node number of T"""
    if T.num_children(p)==0:
        return 1
    else:
        return (numEN(T,T.left(p)) if T.left(p) else 0) + (numEN(T,T.right(p)) if T.right(p) else 0)

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------- Init a tree for further use --------------------
    T = LinkedBinaryTree()
    r0 = T.add_root(0)
    r1 = T.add_left(r0,1)
    r2 = T.add_right(r0,2)
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
    t1.pretraversal()
    t1.intraversal()
    t1.posttraversal()
    t1.breadthfirsttraversal()
    print ''

    #-------------------------- Test code for traversal of table of contents --------------------
    print "Test for print table of contents.........................."
    t2 = LinkedBinaryTree()
    t2n0 = t2.add_root('Paper')
    t2n1 = t2.add_left(t2n0,'Title')
    t2n2 = t2.add_right(t2n0,'Abstract')
    t2n3 = t2.add_left(t2n2,'1.1')
    t2n4 = t2.add_right(t2n2,'1.2')
    # tradition way,waste of time
    for i in t2.preorder():
        print(2*t2.depth(i)*' '+str(i.element()))
    # more efficient way
    preorder_indent(t2,t2n0,0)

    path=[2,3]
    preorder_label(t2,t2n0,0,path)
    print ''

    parenthesize(t2,t2n0)
    print ''
    print ''

    #-----------R-8.5----------------------------------------------------------------
    print "Test for R-8.5................................"
    tree5 = copy.deepcopy(T)
    leftcount = 0
    rightcount = 0
    for i in tree5.inorder():
        if tree5.is_left_leaf(i):
            leftcount += 1
        if tree5.is_right_leaf(i):
            rightcount += 1
    print 'left is:',leftcount,'.','right is:',rightcount
    print ''

    #-----------R-8.6----------------------------------------------------------------
    print "Test for R-8.6................................"
    tree6 = copy.deepcopy(T)

    singlecount = 0
    for i in tree6.inorder():
        if tree6.left(i) == None and tree6.right(i) != None:
            tree6.add_left(i,'Orz')
            singlecount += 1
        elif tree6.right(i) == None and tree6.left(i) != None:
            tree6.add_right(i,'Orz')
            singlecount += 1
    print 'use proper tree represent improper tree: add addtional',singlecount,'nodes'
    tree6.pretraversal()
    print ''

    #-----------R-8.13----------------------------------------------------------------
    print "Test for R-8.13................................"
    tree13 = LinkedBinaryTree()
    t13n0 = tree13.add_root('*')
    t13n1 = tree13.add_left(t13n0,'+')
    t13n2 = tree13.add_right(t13n0,'-')
    t13n3 = tree13.add_left(t13n1,2)
    t13n4 = tree13.add_right(t13n1,1)
    t13n5 = tree13.add_left(t13n2,5)
    t13n6 = tree13.add_right(t13n2,2)
    print 'expression info:',
    tree13.intraversal()
    print ''
    print 'result is:',arithmetic_expression(tree13,t13n0)
    print ''

    #-----------R-8.20----------------------------------------------------------------
    print "Test for R-8.20................................"
    tree20 = LinkedBinaryTree()
    t20n0 = tree20.add_root('E')
    t20n1 = tree20.add_left(t20n0,'X')
    t20n2 = tree20.add_right(t20n0,'N')
    t20n3 = tree20.add_left(t20n1,'A')
    t20n4 = tree20.add_right(t20n1,'U')
    t20n5 = tree20.add_left(t20n3,'M')
    t20n6 = tree20.add_right(t20n3,'F')
    tree20.pretraversal()
    tree20.intraversal()
    print ''

    #-----------R-8.23----------------------------------------------------------------
    print "Test for R-8.23................................"
    """ It is 'not possible' that the preorder traversal of tta visits
        the nodes in the same order of the postorder traversal of tta.
    """
    tree23 = LinkedBinaryTree()
    t23n0 = tree23.add_root('A')
    t23n1 = tree23.add_left(t23n0,'B')
    t23n2 = tree23.add_left(t23n1,'C')
    t23n3 = tree23.add_left(t23n2,'D')
    t23n4 = tree23.add_left(t23n3,'E')
    tree23.pretraversal()
    tree23.posttraversal()
    print ''

    """ It is 'possible' that the preorder traversal of ttb visits
        the nodes in the reverse order of the postorder traversal of ttb.
    """
    tree23 = LinkedBinaryTree()
    t23n0 = tree23.add_root('A')
    t23n1 = tree23.add_right(t23n0,'B')
    t23n2 = tree23.add_right(t23n1,'C')
    t23n3 = tree23.add_right(t23n2,'D')
    t23n4 = tree23.add_right(t23n3,'E')
    tree23.pretraversal()
    tree23.posttraversal()
    print ''

    #-----------C-8.31----------------------------------------------------------------
    print "Test for C-8.31................................"
    tree31 = copy.deepcopy(T)
    t31n0 = tree31.root()
    print 'the sum of external path length is:',sumEPL(tree31,t31n0,0)
    print 'the sum of internal path length is:',sumIPL(tree31,t31n0,0)
    print 'the sum of external node number is:',numEN(tree31,t31n0)
    print 'the sum of internal node number is:',numIN(tree31,t31n0)
    print ''
    #-----------C-8.35----------------------------------------------------------------
    print "Test for C-8.35................................"

    # definition of isomorphic_tree function
    def isomorphic_tree(T1,T2,p1,p2):
        if T1.is_leaf(p1) and T2.is_leaf(p2):
            return True
        elif T1.num_children(p1) != T2.num_children(p2):
            return False
        else:
            m = T2.children(p2)
            for i in T1.children(p1):
                j=m.next()
                if not isomorphic_tree(T1,T2,i,j):
                    return False
            return True

    # init two isomorphic binarytree for test
    tree35a = LinkedBinaryTree()
    t35a0 = tree35a.add_root(1)
    t35a1 = tree35a.add_left(t35a0,2)
    t35a2 = tree35a.add_right(t35a0,2)
    t35a3 = tree35a.add_left(t35a1,2)
    t35a4 = tree35a.add_right(t35a1,2)
    t35a5 = tree35a.add_left(t35a2,2)
    t35a6 = tree35a.add_right(t35a2,2)
    t35a7 = tree35a.add_left(t35a3,2)

    tree35b = LinkedBinaryTree()
    t35b0 = tree35b.add_root(0)
    t35b1 = tree35b.add_left(t35b0,2)
    t35b2 = tree35b.add_right(t35b0,2)
    t35b3 = tree35b.add_left(t35b1,2)
    t35b4 = tree35b.add_right(t35b1,2)
    t35b5 = tree35b.add_left(t35b2,2)
    t35b6 = tree35b.add_right(t35b2,2)
    t35b7 = tree35b.add_left(t35b3,2)

    # test result
    print 'Result of isomorphic:',isomorphic_tree(tree35a,tree35b,t35a0,t35b0)
    # modify T2 to let T1 and T2 be un-isomorphic
    tree35b.delete(t35b7)
    print 'delete a node from T2....'
    # test result
    print 'Result of isomorphic:',isomorphic_tree(tree35a,tree35b,t35a0,t35b0)
    print ''

    #-----------C-8.38----------------------------------------------------------------
    print "Test for C-8.38................................"
    tree38 = copy.deepcopy(T)
    tree38.pretraversal()
    tree38n0 = tree38.root()
    tree38n1 = tree38.left(tree38n0)
    tree38n2 = tree38.right(tree38n0)
    print 'delete:',tree38.delete_subtree(tree38n2),'nodes'
    tree38.pretraversal()
    print 'delete:',tree38.delete_subtree(tree38n1),'nodes'
    tree38.pretraversal()
    print ''

    #-----------C-8.39----------------------------------------------------------------
    print "Test for C-8.39................................"
    tree39 = copy.deepcopy(T)
    tree39n0 = tree39.root()
    tree39n1 = tree39.left(tree39n0)
    tree39n2 = tree39.right(tree39n0)
    tree39n3 = tree39.left(tree39n1)
    tree39n4 = tree39.right(tree39n1)
    tree39n9 = tree39.right(tree39n4)
    tree39.pretraversal()
    #tree39.swap(tree39n2,tree39n3)
    #tree39.swap(tree39n1,tree39n3)
    #tree39.swap(tree39n1,tree39n9)
    tree39.pretraversal()
    print ''
