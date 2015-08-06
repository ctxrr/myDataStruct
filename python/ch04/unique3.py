def unique(S, start, stop):
	"""Return True if there are no duplicate elements in slice S[start:stop]."""
	if stop - start <= 1: return True
	elif not unique(S, start, stop-1): return False
	elif not unique(S, start+1, stop): return False
	else: return S[start] != S[stop-1]

if __name__ == '__main__':
	testlist=[]
	for i in range(10):
		testlist.append(i)
	# testlist[5]=1
	print unique(testlist,0,9)