import os

def disk_usage(path):
	"""Return the number of bytes used by a file/folder and any descendents."""
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			childpath = os.path.join(path, filename)
			total += disk_usage(childpath)
	print ('{0:<7}'.format(total), path) #for debug
	return total

if __name__ == '__main__':
	print disk_usage("../")
	# print os.path.getsize("../ch3")
	# print os.path.getsize("./")