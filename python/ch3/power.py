"""2 function.compare the running time of them"""
def power_slow(x,n):
	if n==0:
		return 1
	else:
		return x* power_slow(x,n-1)

def power_fast(x, n):
	"""Compute the value x n for integer n."""
	if n == 0:
		return 1
	else:
		partial = power_fast(x, n // 2) # rely on truncated division
		result = partial*partial
		if n % 2 == 1: # if n odd, include extra factor of x
			result = x
		return result

if __name__ == '__main__':
	print power_slow(3,2)
	print power_fast(3,2)