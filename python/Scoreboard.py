
'''Definition of class hwarray'''
class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order"""

    def __init__(self,capacity=10):
        self._board=[None]*capacity
        self._n=0

    def __getitem__(self,k):
        return  self.board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self,entry):
        score=entry.get_score()

        good=self._n<len(self._board) or score>self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n +=1
            j=self._n -1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j-=1
            self._board[j]=entry

class GameEntry:
    """Represents one entry of lsit of high scores"""

    def __init__(self,name,score):
        self._name=name
        self._score=score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '{0},{1}'.format(self._name,self._score)


'''Test code from here.....'''
messi=GameEntry('messi',99)
CR7=GameEntry('CR7',95)
xavi=GameEntry('xavi',85)
dadi=GameEntry('dadi',100)
mvp=Scoreboard()

mvp.add(CR7)
mvp.add(xavi)
mvp.add(messi)
mvp.add(dadi)
print str(mvp)
