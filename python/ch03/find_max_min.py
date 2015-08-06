def find_max_min(A):
	n=len(A)
	max=A[0]
	min=A[0]
	cmp_count=0
	for i in range(1,n):
		if A[i]>max:
			max=A[i]
			cmp_count+=1
			# break
		elif A[i]<min:
			min=A[i]
			cmp_count+=1
			# break
	print "max is",max
	print "min is",min
	print "cmp_count is",cmp_count

if __name__ == '__main__':
	testlist=[10,8,100,25,79,1,1024,-10]
	testlist1=[1,2,3,4,5,6,7,8]
	find_max_min(testlist1)
