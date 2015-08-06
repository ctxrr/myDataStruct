"""This modual contain 2 functions used to compute the sum of an polinomial"""

def polinomial1(mylist,x):
    """the running time is O(n2)"""
    n=len(mylist)
    total=0
    for i in range(n):
        comp=1
        for j in range(0,i):
            comp*=x
        comp*=mylist[i]
        total+=comp
    return total

def polinomial2(mylist,x):
    """the running time is O(n),which is much more efficient"""
    n=len(mylist)
    total=0
    comp=1
    for i in range(n):
        total+=(mylist[i]*comp)
        comp*=x
    return total



if __name__ == '__main__':
    testlist=[1,2,3,4,7,6]
    print polinomial1(testlist,5)
    print polinomial2(testlist,5)

