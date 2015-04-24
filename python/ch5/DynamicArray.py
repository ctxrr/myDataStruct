import ctypes

class DynamicArray:

    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.MakeArray(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not (0<=k and k<self.n):
            raise IndexError('invalid index')
        return self.A[k]

    def append(self,obj):
        if self.n==self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n]=obj
        self.n+=1

    def pop(self):
        if self.n==0:
            print "can't pop from an empty array"
            return 0
        if self.n==self.capacity/4:
            self._resize(self.capacity/2)
        self.n-=1

    def _resize(self,c):
        B=self.MakeArray(c)
        for k in range(self.n):
            B[k]=self.A[k]
        self.A=B
        self.capacity=c

    def MakeArray(self,c):
        return (c*ctypes.py_object)()

