"""Contain two function about generating fibonacci array"""

from time import time

def bad_fibonacci(n):
	"""Return the nth Fibonacci number."""
	if n <= 1:
		return n
	else:
		return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def good_fibonacci(n):
	"""Return pair of Fibonacci numbers, F(n) and F(n-1)."""
	if n <= 1:
		return (n,0)
	else:
		(a, b) = good_fibonacci(n-1)
		return (a+b, a)

if __name__ == '__main__':
	start_bad=time()
	print bad_fibonacci(35)
	end_bad=time()
	print "Bad time:",(end_bad-start_bad),'s'

	start_good=time()
	print good_fibonacci(35)
	end_good=time()	
	print "Good time:",(end_good-start_good),'s'