
#------------Import packet-----------------------------------------------------------------------

#------------Class LinkedBinaryTree--------------------------------------------------------------
class EulerTour(object):
    """Abstract base class for performing Euler tour of a tree.

    _hook_previsit and _hook_postvisit may be overridden by subclasses.
    """
    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])    # start the recursion

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.

        p        Position of current node being visited
        d        depth of p in the tree
        path     list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)                       # "pre visit" p
        results = []
        path.append(0)          # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))  # recur on child's subtree
            path[-1] += 1         # increment index
        path.pop()              # remove extraneous index from end of path
        answer = self._hook_postvisit(p, d, path, results)    # "post visit" p
        return answer

    def _hook_previsit(self, p, d, path):
        """Visit Position p, before the tour of its children.

        p        Position of current position being visited
        d        depth of p in the tree
        path     list of indices of children on path from root to p
        """
        pass

    def _hook_postvisit(self, p, d, path, results):
        """Visit Position p, after the tour of its children.

        p        Position of current position being visited
        d        depth of p in the tree
        path     list of indices of children on path from root to p
        results  is a list of values returned by _hook_postvisit(c)
                for each child c of p.
        """
        pass

#------------Class Preorderprintindentedtour--------------------------------------------------------------
class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print 2*d*' ' + str(p.element())

#------------Class Preorderprintindentedlabeledtour--------------------------------------------------------------
class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)    # labels are one-indexed
        print 2*d*' ' + label, p.element()

#------------Class Parenthesizetour--------------------------------------------------------------
class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:                  # p follows a sibling
            print', ',                      # so preface with comma
        print p.element(),                 # then print element
        if not self.tree().is_leaf(p):             # if p has children
            print ' (',                      # print opening parenthesis

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):             # if p has children
            print ')',                       # print closing parenthesis

#------------Class Diskspacetour--------------------------------------------------------------
class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        """we simply add space associated with p to that of its subtrees"""
        return p.element().space() + sum(results)

#------------Class Binaryeulertour--------------------------------------------------------------
class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional _hook_invisit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """
    def _tour(self, p, d, path):
        results = [None, None]          # will update with results of recursions
        self._hook_previsit(p, d, path)                  # "pre visit" for p
        if self._tree.left(p) is not None:               # consider left child
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)                   # "in visit" for p
        if self._tree.right(p) is not None:              # consider right child
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)    # "post visit" p
        return answer

    def _hook_invisit(self, p, d, path):
        """Visit Position p, between tour of its left and right subtrees."""
        pass

#------------Class BinaryLayout--------------------------------------------------------------
class BinaryLayout(BinaryEulerTour):
    """Class for computing (x,y) coordinates for each node of a binary tree."""
    def __init__(self, tree):
        super(BinaryLayout,self).__init__(tree)           # must call the parent constructor
        self._count = 0                  # initialize count of processed nodes

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)    # x-coordinate serialized by count
        p.element().setY(d)              # y-coordinate is depth
        self._count += 1                 # advance count of processed nodes

#------------test code--------------------------------------------------------------
if __name__ == '__main__':
    #------------Import packet-----------------------------------------------------------------------
    from LinkedBinaryTree import LinkedBinaryTree
    from ArrayBinaryTree import ArrayBinaryTree
    from copy import deepcopy

    #-------------------------- Init a linked binary tree for further use --------------------
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

    #-------------------------- test the usage of euler tour traversal --------------------
    #print "Test 1................................"
    #t1 = PreorderPrintIndentedTour(T)
    #t1.execute()
    print "Test 2................................"
    t2 = PreorderPrintIndentedLabeledTour(T)
    t2.execute()
    #print "Test 3................................"
    #t3 = ParenthesizeTour(T)
    #t3.execute()
    print ''
    #print "Test 4................................"
    #t4 = DiskSpaceTour(T)
    #t4.execute()
    #print "Test 5................................"
    #t5 = BinaryEulerTour(T)
    #t5.execute()
    #print "Test 6................................"
    #t6 = BinaryLayout(T)
    #t6.execute()

    #-----------R-8.17----------------------------------------------------------------
    print "Test for R-8.17................................"
    # definition of class
    class ShowLevel(EulerTour):
        def _hook_previsit(self, p, d, path):
            pass

        def _hook_postvisit(self, p, d, path, results):
            pass
    # test code
    tree17 = ArrayBinaryTree()
    t17n0 = tree17.add_root(0)
    t17n1 = tree17.add_left(t17n0,1)
    t17n2 = tree17.add_right(t17n0,2)
    t17n3 = tree17.add_left(t17n1,3)
    t17n4 = tree17.add_right(t17n1,4)
    t17n5 = tree17.add_left(t17n2,5)
    t17n6 = tree17.add_right(t17n2,6)
    t17n7 = tree17.add_left(t17n3,7)
    t17n8 = tree17.add_right(t17n3,8)
    t17n10 = tree17.add_right(t17n4,10)
    t17n13 = tree17.add_left(t17n6,13)
    t17n14 = tree17.add_right(t17n6,14)
    t17n17 = tree17.add_left(t17n8,17)
    t17n27 = tree17.add_left(t17n13,27)
    t17n28 = tree17.add_right(t17n13,28)
    t17n29 = tree17.add_left(t17n14,29)
    t17n30 = tree17.add_right(t17n14,30)
    print ''
    tree17b = ShowLevel(tree17)
    tree17b.execute()

    #-----------R-8.29----------------------------------------------------------------
    print "Test for R-8.29................................"

    # definition of class
    class CalDescendant(EulerTour):
        def _hook_postvisit(self, p, d, path, results):
            num = 0
            for i in results:
                num +=i
            print (p.element(),num+1),
            return num+1
    # test code
    tree29a = deepcopy(T)
    tree29b = CalDescendant(tree29a)
    tree29b.execute()
    print ''

    #-----------C-8.47----------------------------------------------------------------
    print "Test for C-8.47................................"
    # definition of class
    class ShowBalance(EulerTour):
        def _hook_postvisit(self, p, d, path, results):
            if self._tree.is_leaf(p):
                subheight = (0,0)
            else:
                subheight = results
            height = max(subheight)+1
            if len(results)==1:
                factor = subheight[0]
            else:
                factor = subheight[0] - subheight[1]
            print (p.element(),factor),
            return height
    # test code
    tree47a = deepcopy(T)
    tree47b = ShowBalance(tree47a)
    tree47b.execute()
    print ''
