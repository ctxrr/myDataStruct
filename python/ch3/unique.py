"""This module contain 2 functions about finding out if the element in a sequence is unique or not
   unique1 runs in O(n2) time and unique2 runs in O(nlogn) time so unique2 is better
"""
def unique1(S):
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False # found duplicate pair
    return True # if we reach this, elements were unique

def unique2(S):
    """Return True if there are no duplicate elements in sequence S."""
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False
    return True
