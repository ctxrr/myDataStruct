from time import time

a=[10000,100000,1000000,10000000]
def usestr(n):
	start=time()
	str1=''
	for i in range(n):
		str1+='A'
	end=time()
	return end-start

def uselist(n):
	start=time()
	str2=[]
	for i in range(n):
		str2.append('A')
	end=time()
	return end-start

for i in a:
	print "use str:%f," %(usestr(i))

for i in a:
	print "use lis:%f,"  %(uselist(i))
