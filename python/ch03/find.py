"""This module contain a function to show how the Loop Invariants used"""
def find(S, val):
    """Return index j such that S[j] == val, or -1 if no such element."""
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j # a match was found at index j
        j += 1
    return -1

if __name__ == '__main__':
	testlist=[5,12,98,1,34,123,1]
	print find(testlist,1)
