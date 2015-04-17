import ctypes

'''Definition of class hwarray'''
class hwarray:
    'array by hw'
    def __init__(self):
        self.size=0
        self.capacity=1
        self.A=self.MakeArray(self.capacity)

    def Size(self):
        return self.size

    def __getitem__(self,num):
        return self.Get(num)

    '''print the array'''
    def Show(self):
        print 'Current array is:',
        print '[',
        for i in range(self.size):
            if i != self.size-1:
                print self.A[i],
                print ',',
            else:
                print self.A[i],
        print ']'
        print 'Size is:',
        print self.size
        print 'Capacity is:',
        print self.capacity

    def Get(self,num):
        '''Attention:the largest number you can get is capacity-1\
           this means that if an array's capacity is 8,you can only\
           get A[7]!'''
        if not (num>=0 and num<self.capacity):
            raise IndexError('invalid index')
        return self.A[num]

    def Add(self,obj):
        if self.size==self.capacity:
            self.Rebuild(2*self.capacity)
        self.A[self.size]=obj
        self.size+=1

    def Find(self,obj):
        findinfo=0
        for i in range(self.size):
            if self.A[i]==obj:
                findinfo+=1
                print "Find No %d element! Index is %d" %(findinfo,i)  
        if findinfo==0:
            print 'value not found'    

    '''found the obj in array and delete it if exist'''
    def Del(self,obj):
        for i in range(self.size):
            if self.A[i]==obj:
                for j in range(i,self.size-1):
                    self.A[j]=self.A[j+1]
                self.A[self.size-1]=None
                self.size-=1
                return
        raise ValueError('value not found')    

    def Ins(self,num,obj):
        if num>self.size or num<0:
            raise IndexError("invalid index : You can't insert outside")

        if self.size==self.capacity:
            self.Rebuild(2*self.capacity)

        for i in range(self.size-1,num-1,-1):
            self.A[i+1]=self.A[i]
        self.A[num]=obj
        self.size+=1

    def Rebuild(self,number):
        B=self.MakeArray(number)
        for i in range(self.size):
            B[i]=self.A[i]
        self.A=B
        self.capacity=number

    def MakeArray(self,number):
        return (number*ctypes.py_object)()

'''Test code from here.....'''
a=hwarray()
a.Add(100)
a.Add(200)
a.Add(300)
a.Add(100)
a.Show()
a.Find(100)
print a[1]