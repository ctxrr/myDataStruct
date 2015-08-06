class Node():
    def __init__(self,e,left=None,right=None):
        self.element = e
        self.left = left
        self.right = right

def traversal(node,mode):
    if node:
        if mode == 'NLR':print node.element,
        traversal(node.left,mode)
        if mode == 'LNR':print node.element,
        traversal(node.right,mode)
        if mode == 'LRN':print node.element,

def traversal_norec(node,mode):
    s = []
    while node or s:
        if node:
            s.append(node)
            if mode == 'NLR':print node.element,
            node = node.left
        else:
            node = s.pop()
            if mode == 'LNR':print node.element,
            node = node.right
if __name__ == '__main__':
    h = Node(8)
    i = Node(9)
    j = Node(10)
    d = Node(4)
    e = Node(5,h,i)
    f = Node(5,None,j)
    g = Node(7)
    b = Node(2,d,e)
    c = Node(3,f,g)
    a = Node(1,b,c)

    traversal(a,'NLR')
    print ''
    traversal(a,'LNR')
    print ''
    traversal(a,'LRN')
    print ''
    traversal_norec(a,'NLR')
    print ''
    traversal_norec(a,'LNR')
    print ''
