""" This module contain a very common usage of algorithm:find sum.
    Assuming that we have a nondecreasing list,findSum will return a
    list contain all the possible combination of elements which sum
    equals to V
"""
def findSum(L,V):
	i=0
	j=len(L)-1
	ret = list()
	while L[i] < L[j]:
		if (L[i] + L[j]) > V:
			j -= 1
		elif (L[i] + L[j]) < V :
			i += 1
		else:
			ret.append((L[i],L[j]))
			i += 1
	if len(ret) !=0:
		return ret
	else:
		return None

if __name__ == '__main__' :
	Li=[1,2,3,4,5,6]
	print findSum(Li,100)
	print findSum(Li,7)
