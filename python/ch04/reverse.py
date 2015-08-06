def reverse(S,start=None,stop=None):
	"""reverse the list S by using recursive way"""
	
	if start < stop - 1:
		S[start],S[stop] = S[stop],S[start]
		reverse(S,start+1,stop-1)

def reverse_iterative(S):
	"""Reverse elements in sequence S."""
	start, stop = 0, len(S)
	while start < stop - 1:
		S[start], S[stop-1] = S[stop-1], S[start]
		start, stop = start + 1, stop - 1

if __name__ == '__main__':
	testlist=[]
	for i in range(10):
		testlist.append(i)
	print testlist
	reverse(testlist,0,9)
	print testlist

	print '--------------------------------'
	testlist1=[]
	for i in range(10):
		testlist1.append(i)
	print testlist1
	reverse_iterative(testlist1)
	print testlist1