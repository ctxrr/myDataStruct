#------------Import packet-----------------------------------------------------------------------
from collections import deque

#------------Class Node--------------------------------------------------------------
class Node:
    """Linked representation of a binary tree structure."""
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

#------------Stand alone function--------------------------------------------------------------
def VisitTree_Recursive(root, order):
    if root:
        if order == 'NLR': print(root.data)
        VisitTree_Recursive(root.left, order)
        if order == 'LNR': print(root.data)
        VisitTree_Recursive(root.right, order)
        if order == 'LRN': print(root.data)

def VisitTree(root, order):
    s = []
    while root or s:
        if root:
            if order == 'NLR': print(root.data)
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            if order == 'LNR': print(root.data)
            root = root.right

def VisitTreeLRN(root):
    s = []
    pre = None
    while root or s:
        if root:
            s.append(root)
            root = root.left
        elif s[-1].right != pre:
            root = s[-1].right
            pre = None
        else:
            pre = s.pop()
            print(pre.data)

def VisitTree_LevelOrder(root):
    if not root: return
    q = deque([root])
    while q:
        root = q.popleft()
        print(root.data)
        if root.left: q.append(root.left)
        if root.right: q.append(root.right)

#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    g = Node('G')
    h = Node('H')
    e = Node('E', g, h)
    i = Node('I')
    f = Node('F', None, i)
    c = Node('C', e, f)
    d = Node('D')
    b = Node('B', d)
    a = Node('A', b, c)
    root = a
    VisitTree_Recursive(a,'NLR')
    VisitTree_Recursive(a,'LNR')
    VisitTree_Recursive(a,'LRN')
