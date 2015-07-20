from Tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def is_left_leaf(self, p):
        """Return True if Position p is the left leaf of its parent."""
        raise NotImplementedError('must be implemented by subclass')

    def is_right_leaf(self, p):
        """Return True if Position p is the right leaf of its parent."""
        raise NotImplementedError('must be implemented by subclass')

    def add_root(self, e):
        """Add root node"""
        raise NotImplementedError('must be implemented by subclass')

    def add_left(self, p, e):
        """Add left child"""
        raise NotImplementedError('must be implemented by subclass')

    def add_right(self, p, e):
        """Add right child"""
        raise NotImplementedError('must be implemented by subclass')

    def replace(self, p, e):
        """Replace the element stored in p into e"""
        raise NotImplementedError('must be implemented by subclass')

    def delete(self, p):
        """Delete the node p"""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                    # p must be the root
            return None                         # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)         # possibly None
            else:
                return self.left(parent)          # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def preorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def postorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:          # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                               # visit p between its subtrees
        if self.right(p) is not None:         # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def _subtree_preorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        yield p                               # visit p between its subtrees
        if self.left(p) is not None:          # if left child exists, traverse its subtree
            for other in self._subtree_preorder(self.left(p)):
                yield other
        if self.right(p) is not None:         # if right child exists, traverse its subtree
            for other in self._subtree_preorder(self.right(p)):
                yield other

    def _subtree_postorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:          # if left child exists, traverse its subtree
            for other in self._subtree_postorder(self.left(p)):
                yield other
        if self.right(p) is not None:         # if right child exists, traverse its subtree
            for other in self._subtree_postorder(self.right(p)):
                yield other
        yield p                               # visit p between its subtrees

    # override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()                 # make inorder the default
