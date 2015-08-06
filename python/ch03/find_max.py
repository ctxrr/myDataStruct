
def find_max(a):
	maxmem=0
	for i in range(len(a)):
		if a[i]>maxmem:
			maxmem=a[i]
	return maxmem

if __name__ == '__main__':
	a=[1,3,5,2,-1]
	print find_max(a)