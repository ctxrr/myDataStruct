def binary_search(data, target, low, high):
	"""Return True if target is found in indicated portion of a Python list.
	The search only considers the portion from data[low] to data[high] inclusive.
	"""
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search(data, target, low, mid - 1)
		else:
			return binary_search(data, target, mid + 1, high)

def binary_search_iterable(data,target):
	"""the old binary_search is tail recursion,so it can be implemented in nonrecursive way"""
	low=0
	high=len(data)-1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False

if __name__ == '__main__':
	testlist=[]
	for i in range(100):
		testlist.append(i)
	print binary_search(testlist,0,0,99)

	print binary_search_iterable(testlist,1)