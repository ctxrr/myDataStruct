
#------------Import packet-----------------------------------------------------------------------
from Tree import Tree
import copy

class LinkedTree(Tree):
    """Linked representation of a general tree structure."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_children' # streamline memory usage

        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

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

    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node


    # --------------------- additional public methods ---------------------
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

    def get_child(self,p,index):
        if index>self.num_children(p):
            print 'index out of range'
            return
        node = self._validate(p)
        return self._make_position(node._children[index])

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

def indentedparenthetic(T,p,size):
    """Print parenthesized representation of subtree of T rooted at p."""
    print 2*size*' '+str(p.element()),
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            if first_time:
                print '('
            else:
                print ''
            first_time = False
            indentedparenthetic(T,c,size+1) # recur on child
        print ''
        print 2*size*' '+')',

def isomorphic_tree(T1,T2,p1,p2):
    """Test whether T1 and T2 are isomorphic"""
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

def element_height(T,p):
    """print the element at position p and the height of p"""
    if T.is_leaf(p):
        print (p.element(),0),
        return 0
    else:
        height= 1+max(element_height(T,i) for i in T.children(p))
        print (p.element(),height),
        return height

def element_depth(T,p,depth=0):
    """print the element at position p and the depth of p"""
    print (p.element(),depth),
    if not T.is_leaf(p):
        for i in T.children(p):
            element_depth(T,i,depth+1)

def path_length(T,p,depth=0,result=0):
    """Caculate the path length of a binarytree"""
    result += depth
    #for debug
    #print (p.element(),depth,result),
    for i in T.children(p):
        result = path_length(T,i,depth+1,result)

    return result

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------- Init a tree for further use --------------------
    T = LinkedTree()
    r0 = T.add_root(0)
    r1 = T.add_child(1,r0)
    r2 = T.add_child(2,r0)
    r3 = T.add_child(3,r0)
    r4 = T.add_child(4,r1)
    r5 = T.add_child(5,r1)
    r6 = T.add_child(6,r1)
    r7 = T.add_child(7,r2)
    r8 = T.add_child(8,r2)
    r9 = T.add_child(9,r3)
    r10 = T.add_child(10,r5)
    r11 = T.add_child(11,r5)
    r12 = T.add_child(12,r7)
    r13 = T.add_child(13,r9)
    r14 = T.add_child(14,r9)
    r15 = T.add_child(15,r9)
    r16 = T.add_child(16,r13)

    #-------------------------- Test code for 3 different way of traversal --------------------
    print "Test for different traversal way.........................."
    T.pretraversal()
    T.posttraversal()
    T.breadthfirsttraversal()

    #-------------------------- Test code for traversal of table of contents --------------------
    print "Test for print table of contents.........................."
    t2 = LinkedTree()
    t2n0 = t2.add_root('Paper')
    t2n1 = t2.add_child('Title',t2n0)
    t2n2 = t2.add_child('Abstract',t2n0)
    t2n3 = t2.add_child('1.1',t2n2)
    t2n4 = t2.add_child('1.2',t2n2)
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

    #-----------C-8.35----------------------------------------------------------------
    print "Test for C-8.35................................"
    # init two isomorphic tree for test
    tree35a = LinkedTree()
    t35a0 = tree35a.add_root(0)
    t35a1 = tree35a.add_child(1,t35a0)
    t35a2 = tree35a.add_child(2,t35a0)
    t35a3 = tree35a.add_child(3,t35a0)
    t35a4 = tree35a.add_child(4,t35a1)
    t35a5 = tree35a.add_child(5,t35a1)

    tree35b = LinkedTree()
    t35b0 = tree35b.add_root(0)
    t35b0 = tree35b.add_root(0)
    t35b1 = tree35b.add_child(1,t35b0)
    t35b2 = tree35b.add_child(2,t35b0)
    t35b3 = tree35b.add_child(3,t35b0)
    t35b4 = tree35b.add_child(4,t35b1)
    t35b5 = tree35b.add_child(5,t35b1)

    # test result
    print 'Result of isomorphic:',isomorphic_tree(tree35a,tree35b,t35a0,t35b0)
    print ''

    #-----------C-8.44----------------------------------------------------------------
    print "Test for C-8.44................................"
    tree44 = copy.deepcopy(T)
    t44n0 = tree44.root()
    element_height(tree44,t44n0)
    print ''
    t44n3 = tree44.get_child(t44n0,2)
    element_height(tree44,t44n3)
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
    print ''

    #-----------C-8.56----------------------------------------------------------------
    print "Test for C-8.56................................"
    indentedparenthetic(t2,t2n0,0)
    print ''
    print ''


