class Reclist:

    def __init__(self,e):
        self._element = e
        self._rest = None
        self._size = 0

    def add(self,e):
        if self._rest == None:
            new = Reclist(e)
            self._rest = new
        else:
            self._rest.add(e)

    def __iter__(self):
        walk = self._rest
        while walk != None:
            yield walk._element
            walk = walk._rest


if __name__ == '__main__':
    a=Reclist(None)

    a.add(1)
    a.add(2)
    a.add(3)
    for i in a:
        print i
