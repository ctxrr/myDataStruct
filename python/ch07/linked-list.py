"""contain 2 class about linkedlist,this module is finished by ctxrr"""

class Node():
    """a node contain a reference to the next node and a reference to its element"""
    def __init__(self,e):
       self.element=e
       self.next=None

    def hasNext(self):
        """if the node has next,return true;else turn false"""
        return self.next!=None

    def getNext(self):
        """get the next node"""
        return self.next


class LinkedList():
    def __init__(self):
        self.head=Node(None)
        #self.tail=Node()
        self.size=0

    def getTail(self):
        """get the end of the list"""
        walknode=self.head
        while True:
            if walknode.hasNext():
                walknode=walknode.getNext()
            else:
                return walknode

    def walk(self):
        """print all the element in linkedlist"""
        walknode=self.head
        while True:
            if walknode.hasNext():
                walknode=walknode.getNext()
                print walknode.element
            else:
                return 0
    def append(self,e):
        """add an new node to the end of linkedlist"""
        newNode=Node(e)
        end=self.getTail()
        end.next=newNode
        self.size+=1

    def ifexist(self,e):
        """show if an element exist in the linkedlist"""
        walknode=self.head
        while True:
            if walknode.hasNext():
                walknode=walknode.getNext()
                if e==walknode.element:
                    return True
            else:
                return False

if __name__ == '__main__':
    ll=LinkedList()
    ll.append(3)
    ll.append("a")
    ll.walk()
    print ll.ifexist(1)
    print ll.size
