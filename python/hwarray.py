import ctypes

class hwarray:

    def __init__(self):
        self.size=0
        self.capacity=1
        self.A=self.MakeArray(self.capacity)

    def Size(self):
        return self.size

    def Get(self,n):
        if not (n>=0 and n<self.capacity):
            raise IndexError('invalid index')
        return self.A[n]

    def Append(self,n):
        if self.size==self.capacity:
            self.Rebuild(2*self.capacity)
        self.A[self.size]=n
        self.size+=1

    def Rebuild(self,n):
        B=self.MakeArray(n)
        for i in range(self.size):
            B[i]=self.A[i]
        self.A=B
        self.capacity=n

    def MakeArray(self,c):
        return (c*ctypes.py_object)()


