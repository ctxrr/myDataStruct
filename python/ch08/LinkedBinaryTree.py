
#------------Import packet-----------------------------------------------------------------------
from BinaryTree import BinaryTree
from LinkedTree import isomorphic_tree,element_height,element_depth,path_length
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
    r14 = T.add_right(r10,14)
    r15 = T.add_left(r11,15)
    r16 = T.add_right(r11,16)
    print ''

    #-------------------------- Test code for 3 different way of traversal --------------------
    print "Test for different traversal way.........................."
    t1 = copy.deepcopy(T)
    t1.pretraversal()
    t1.intraversal()
    t1.posttraversal()
    t1.breadthfirsttraversal()
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
    print 'Improper tree:'
    tree6.pretraversal()
    print ''

    print 'proper tree represent improper tree: add addtional',convert_to_proper(tree6,'Orz'),'nodes'
    print ''

    print 'Proper tree:'
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
    #print "Test for C-8.39................................"
    #tree39 = copy.deepcopy(T)
    #tree39n0 = tree39.root()
    #tree39n1 = tree39.left(tree39n0)
    #tree39n2 = tree39.right(tree39n0)
    #tree39n3 = tree39.left(tree39n1)
    #tree39n4 = tree39.right(tree39n1)
    #tree39n9 = tree39.right(tree39n4)
    #tree39.pretraversal()
    ##tree39.swap(tree39n2,tree39n3)
    ##tree39.swap(tree39n1,tree39n3)
    ##tree39.swap(tree39n1,tree39n9)
    #tree39.pretraversal()
    #print ''

    #-----------C-8.41----------------------------------------------------------------
    print "Test for C-8.41................................"
    # clonetree can only handle proper tree,so any improper tree will cause an error
    tree41a = copy.deepcopy(T)
    convert_to_proper(tree41a,'Orz')
    print 'Old tree'
    tree41a.pretraversal()
    t41a0 = tree41a.root()
    tree41b = clonetree(tree41a,t41a0)
    print ''

    print 'Use attach to clone new tree'
    tree41b.pretraversal()
    print 'len:',len(tree41b)
    # you can even clone a subtree as long as it is proper!
    T.pretraversal()
    tree41c = clonetree(T,r6)
    print ''

    print 'Clone the subtree of T from node r6:'
    tree41c.pretraversal()
    print 'len:',len(tree41c)
    print ''

    #-----------C-8.42----------------------------------------------------------------
    print "Test for C-8.42................................"
    tree42a = copy.deepcopy(T)
    print 'Old tree'
    tree42a.pretraversal()
    print ''

    print 'Use add_left & add_right to clone new tree'
    t42a0 = tree42a.root()
    tree42b = LinkedBinaryTree()
    clonetree2(tree42a,t42a0,tree42b,None)
    tree42b.pretraversal()
    print 'len:',len(tree42b)
    print ''

    #-----------C-8.44----------------------------------------------------------------
    print "Test for C-8.44................................"
    tree44 = copy.deepcopy(T)
    tree44.pretraversal()
    t44n0 = tree44.root()
    t44n1 = tree44.left(t44n0)
    t44n2 = tree44.right(t44n0)
    element_height(tree44,t44n1)
    print ''
    element_height(tree44,t44n2)
    print ''
    print ''

    #-----------C-8.45----------------------------------------------------------------
    print "Test for C-8.45................................"
    tree45 = copy.deepcopy(T)
    t45n0 = tree45.root()
    element_depth(tree45,t45n0)
    print ''
    print ''

    #-----------C-8.46----------------------------------------------------------------
    print "Test for C-8.46................................"
    tree46 = copy.deepcopy(T)
    t46n0 = tree46.root()
    print 'Use path_length:',path_length(tree46,t46n0)
    print 'Use the sum of external and internal path length:',sumEPL(tree46,t46n0,0),sumIPL(tree46,t46n0,0)
    print ''

    #-----------C-8.47----------------------------------------------------------------
    print "Test for C-8.47................................"
    tree47a = copy.deepcopy(T)
    t47a0 = tree47a.root()
    print tree47a.balance_factor(t47a0)
    print 'is balance:',tree47a.is_balance(t47a0)

    tree47b = copy.deepcopy(tree20)
    t47b0 = tree47b.root()
    print tree47b.balance_factor(t47b0)
    print 'is balance',tree47b.is_balance(t47b0)
    print ''

    #-----------C-8.48----------------------------------------------------------------
    print "Test for C-8.48................................"
    tree48 = copy.deepcopy(T)
    tree48.pretraversal()
    node48 = tree48._validate(tree48.root())
    reflection_tree(node48)
    tree48.posttraversal()
    print ''

    #-----------C-8.50----------------------------------------------------------------
    print "Test for C-8.50................................"
    #T.pretraversal()
    #T.intraversal()
    #T.posttraversal()
    def slow_foo(T,p):
        lock = True
        for i in T.inorder():
            if lock:
                if i == p:
                    lock = False
            else:
                print i.element()
                return
    slow_foo(T,r15)

    def preorder_next(T,p):
        pass
    print ''

    #-----------C-8.51----------------------------------------------------------------
    print "Test for C-8.51................................"
    # define a subclass of LinkedBinaryTree
    class IterTraversal(LinkedBinaryTree):
        # --------------------- define nested iteration class ---------------------
        class Iterclass():
            def __init__(self,n):
                self.node = n
                self.generator = None

            def __iter__(self):
                self.generator = self.iter_preorder(self.node)
                return self

            def next(self):
                return self.generator.next()

            def iter_preorder(self,n):
                yield n                               # visit p between its subtrees
                if n._left is not None:          # if left child exists, traverse its subtree
                    for other in self.iter_preorder(n._left):
                        yield other
                if n._right is not None:         # if right child exists, traverse its subtree
                    for other in self.iter_preorder(n._right):
                        yield other

        # --------------------- override preorder methods ---------------------
        def preorder(self):
            if not self.is_empty():
                return self.Iterclass(self.root()._node)

    # test code
    tree51 = IterTraversal()
    t51n0 = tree51.add_root('A')
    t51n1 = tree51.add_right(t51n0,'B')
    t51n2 = tree51.add_right(t51n1,'C')
    t51n3 = tree51.add_right(t51n2,'D')
    t51n4 = tree51.add_right(t51n3,'E')
    for i in tree51.preorder():
        print i._element,
    print ''
    print ''

    #-----------C-8.57----------------------------------------------------------------
    print "Test for C-8.57................................"
    t57 = copy.deepcopy(T)
    t57n1 = t57.root()
    roman_traversal(t57,t57n1,1)
    print ''

    #-----------C-8.58----------------------------------------------------------------
    print "Test for C-8.58................................"
    print findLCA(T,r5,r13).element()
    print ''

    #-----------C-8.59----------------------------------------------------------------
    print "Test for C-8.59................................"
    print 'Distance:',distance(T,r12,r13)
    print 'Diameter:',diameter(T,r0)
    print 'Diameter:',diameterOpt(T,r0)[0]

    #-----------P-8.66----------------------------------------------------------------
    print "Test for P-8.66................................"
    # define a subclass of LinkedBinaryTree named Linkedbinarytreebeta
    class LinkedBinaryTreeBeta(LinkedBinaryTree):
        # re-implemented some method to suport field '_path'
        class _Node:
            def __init__(self, element, left=None, right=None):
                self._element = element
                self._left = left
                self._right = right

        class Position:
            def __init__(self, container, node,path):
                self._container = container
                self._node = node
                self._path = path

        def _validate(self, p):
            if not isinstance(p, self.Position):
                raise TypeError('p must be proper Position type')
            if p._container is not self:
                raise ValueError('p does not belong to this container')
            return p._node

        def _make_position(self, node,path):
            return self.Position(self, node,path) if node is not None else None

        def _add_root(self, e):
            if self._root is not None:
                raise ValueError('Root exists')
            self._size = 1
            self._root = self._Node(e)
            return self._make_position(self._root,[self._root])

        def _add_left(self, p, e):
            node = self._validate(p)
            if node._left is not None:
                raise ValueError('Left child exists')
            self._size += 1
            node._left = self._Node(e)                  # node is its parent
            return self._make_position(node._left,p._path+[node._left])

        def _add_right(self, p, e):
            node = self._validate(p)
            if node._right is not None:
                raise ValueError('Right child exists')
            self._size += 1
            node._right = self._Node(e)                 # node is its parent
            return self._make_position(node._right,p._path+[node._right])

    # test code
    tree66 = LinkedBinaryTreeBeta()
    t66n0 = tree66.add_root(0)
    t66n1 = tree66.add_left(t66n0,1)
    t66n2 = tree66.add_right(t66n0,2)
    t66n3 = tree66.add_left(t66n1,3)
    t66n4 = tree66.add_right(t66n1,4)
    t66n5 = tree66.add_left(t66n2,5)
    t66n6 = tree66.add_right(t66n2,6)
    t66n7 = tree66.add_left(t66n3,7)
    t66n8 = tree66.add_right(t66n3,8)
    t66n9 = tree66.add_right(t66n4,9)
    t66n10 = tree66.add_left(t66n6,10)
    t66n11 = tree66.add_right(t66n6,11)
    t66n12 = tree66.add_left(t66n8,12)
    t66n13 = tree66.add_left(t66n10,13)
    t66n14 = tree66.add_right(t66n10,14)
    t66n15 = tree66.add_left(t66n11,15)
    t66n16 = tree66.add_right(t66n11,16)

    # test the path
    print 'Show the path of Position:',
    for i in t66n16._path:
        print i._element,
    print ''
    print ''

