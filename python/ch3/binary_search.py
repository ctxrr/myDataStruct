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

if __name__ == '__main__':
	testlist=[]
	for i in range(100):
		testlist.append(i)
	print binary_search(testlist,0,0,99)