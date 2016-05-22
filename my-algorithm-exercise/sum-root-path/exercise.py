import sys
sys.path.append('lib')
from LinkedBinaryTree import LinkedBinaryTree

# Desception: calculate the sum of all the path in a binary tree
# return: return a 2-element array.
#   a[0]: storage current sum of node
#   a[1]: storage current number of the leaves of node

def cal_path_sum(T, p, n):
    if (p is None):
        return [0, 0]
    else:
        if T.num_children(p) is not 0:
            left = cal_path_sum(T, T.left(p), n+1)
            right = cal_path_sum(T, T.right(p), n+1)
            return [left[0] + right[0] + (left[1] + right[1]) * (p.element() * (10 ** n)),
                    left[1] + right[1]]
        else:
            return [p.element() * (10 ** n), 1]


#------------Test code-------------------------------------------------------------------------
if __name__ == '__main__':
    #-------------------------- Init a tree for further use --------------------
    T = LinkedBinaryTree()
    r0 = T.add_root(1)
    r1 = T.add_left(r0,2)
    r2 = T.add_right(r0,3)
    r3 = T.add_left(r1,4)
    r4 = T.add_right(r1,5)
    r5 = T.add_left(r2,6)
    r6 = T.add_right(r2,7)
    r7 = T.add_left(r3,8)
    r8 = T.add_right(r3,9)
    r9 = T.add_left(r4,10)
    r10 = T.add_right(r4,11)
    print ''
    T.pretraversal()
    T.posttraversal()
    m = cal_path_sum(T, r0, 0)
    print m


