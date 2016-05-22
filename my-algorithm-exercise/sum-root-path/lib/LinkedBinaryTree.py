
#------------Import packet-----------------------------------------------------------------------
from BinaryTree import BinaryTree

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
            for p in self._subtree_preorder(self.root()):
                yield p

    # --------------------- additional public methods ---------------------
    def swap(self,p,q):
        """Swap the node p and q"""
        return self._swap(p,q)

    def is_left_leaf(self, p):
        """Return True if Position p is the left leaf of its parent."""
        return self.is_leaf(p) and p==self.left(self.parent(p))

    def is_right_leaf(self, p):
        """Return True if Position p is the right leaf of its parent."""
        return self.is_leaf(p) and p==self.right(self.parent(p))

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

    def delete_subtree(self,p):
        """Delete the subtrees of node p"""
        return self._delete_subtree(p)

    def attach(self,p,t1,t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        return self._attach(p,t1,t2)

    def is_balance(self,p):
        return -2 < self.balance_factor(p) < 2

    def balance_factor(self,p):
        """Return the balance factor of posion p"""
        return self.height(self.left(p)) - self.height(self.right(p))

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
        # TBC
        pass

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
    if not p:
        return 0
    else:
        if T.num_children(p)==0:
            return 0
        else:
            return value + sumIPL(T,T.left(p),value+1) + sumIPL(T,T.right(p),value+1)

def sumEPL(T,p,value):
    """Caculate the external path length of T"""
    if not p:
        return 0
    else:
        if T.num_children(p)==0:
            return value
        else:
            return sumEPL(T,T.left(p),value+1) + sumEPL(T,T.right(p),value+1)

def numIN(T,p):
    """Caculate the internal node number of T"""
    if not p:
        return 0
    else:
        if T.num_children(p)==0:
            return 0
        else:
            return 1 + numIN(T,T.left(p)) + numIN(T,T.right(p))

def numEN(T,p):
    """Caculate the external node number of T"""
    if not p:
        return 0
    else:
        if T.num_children(p)==0:
            return 1
        else:
            return numEN(T,T.left(p)) + numEN(T,T.right(p))

def clonetree(T,p):
    """Clone a proper tree and return the new tree"""
    if T.is_leaf(p):
        tree = LinkedBinaryTree()
        tree.add_root(p.element())
        return tree
    else:
        tree = LinkedBinaryTree()
        r0 = tree.add_root(p.element())
        tree.attach(r0,clonetree(T,T.left(p)),clonetree(T,T.right(p)))
        return tree

def clonetree2(T,p,T0,p0):
    """Clone a binary tree(not necessarily proper)"""
    if T.is_root(p):
        p0 = T0.add_root(p.element())
    if T.left(p) is not None:
        T0.add_left(p0,T.left(p).element())
        clonetree2(T,T.left(p),T0,T0.left(p0))
    if T.right(p) is not None:
        T0.add_right(p0,T.right(p).element())
        clonetree2(T,T.right(p),T0,T0.right(p0))

def convert_to_proper(impropertree,set_element):
    """Convert an improper tree into proper
       The old order will not change,new element will be set into 'set_element'
    """
    singlecount = 0
    for i in impropertree.inorder():
        if impropertree.left(i) == None and impropertree.right(i) != None:
            impropertree.add_left(i,set_element)
            singlecount += 1
        elif impropertree.right(i) == None and impropertree.left(i) != None:
            impropertree.add_right(i,set_element)
            singlecount += 1
    return singlecount

def reflection_tree(p):
    if p == None:
        return p
    temp = reflection_tree(p._left)
    p._left = reflection_tree(p._right)
    p._right = temp
    return p

def roman_traversal(T,p,roman_factor):
    """a.Desception:print out all the roman position in Tree T rooted at position p
        b.Return:roman_traversal returns a tuple which has 3 member:
            1.num_node is the descendant's number of p
            2.result is whether p is roman or not
            3.ret is whether p is the position that I want,which means p itself is not roman
            but all its descendants are roman
        c.Parameter:
            roman_factor is the factor that user should give in user-code
    """
    if not p:
        return (0,True,True)
    else:
        if T.num_children(p)==0:
            # for debug
            #print p.element(),True,False
            return (1,True,False)
        else:
            left_result  = roman_traversal(T,T.left(p),roman_factor)
            right_result = roman_traversal(T,T.right(p),roman_factor)
            num_node = left_result[0] + right_result[0] + 1
            result = (-1*roman_factor-1) < (left_result[0] - right_result[0]) < roman_factor+1
            ret = (not left_result[2]) and (not right_result[2]) and (not result)
            # for debug
            #print p.element(),result,ret
            if ret:
                print p.element()
            return (num_node,result,ret)

def findLCA(T,p,q):
    """Find the lowest common ancestor of p and q
        Suppose the depth of p and q is dp and dq.
        the running time of findLCA is O(dp*dq) which is much smaller than O(n2)
    """
    walk_p = p
    while walk_p:
        walk_q = q #set walk_q into initial state
        while walk_q:
            if walk_p == walk_q:
                return walk_p
            else:
                walk_q = T.parent(walk_q)
        walk_p = T.parent(walk_p)

def distance(T,p,q):
    """Caculate the distance between p and q"""
    lca = findLCA(T,p,q)
    return T.depth(p)+T.depth(q)-2*T.depth(lca)

def diameter(T,p):
    """Caculate the diameter of a tree.
       The diameter of a tree (sometimes called the width) is the number
           of nodes on the longest path between two leaves in the tree.
       Run in O(n^2), not efficient!
    """
    if p == None:
        return 0
    rootDiameter  = T.height(T.left(p)) + T.height(T.right(p)) + 1
    leftDiameter  = diameter(T,T.left(p))
    rightDiameter = diameter(T,T.right(p))

    return max(rootDiameter,leftDiameter,rightDiameter)

def diameterOpt(T,p):
    """Caculate the diameter of a tree.
       The diameter of a tree (sometimes called the width) is the number
           of nodes on the longest path between two leaves in the tree.
       Use a variable currentNode:to save the max node number from current
           node to the bottom.currentNode is greater than T.height(p) at 1.
           For example,the currentNode of any leaf is 1.
       Run in O(n), efficient!
    """
    result = [0,0]
    if p == None:
        return result #return (0,0) if p is None
    leftResult = diameterOpt(T,T.left(p));
    rightResult = diameterOpt(T,T.right(p));
    currentNode = max(leftResult[1], rightResult[1]) + 1;
    rootDiameter = leftResult[1] + rightResult[1] + 1;
    leftDiameter = leftResult[0];
    rightDiameter = rightResult[0];
    result[0] = max(rootDiameter,leftDiameter, rightDiameter)
    result[1] = currentNode
    return result
