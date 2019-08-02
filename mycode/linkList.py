class daynames:
    def __init__(self,data):
        self.data=data
        self.next=None

class llist:
    def __init__(self):
        self.head=None

    def printAll(self):
        temp=self.head
        while(temp != None):
            print(temp.data)
            temp=temp.next

    def atBeginning(self,dataVal):
        NewNode=daynames(dataVal)
        NewNode.next=self.head
        self.head=NewNode

    def atLast(self,dataVal):
        NewNode=daynames(dataVal)
        temp=self.head
        while(temp.next != None):
            temp=temp.next
        temp.next=NewNode
        NewNode.next=None
    def inBetween(self):
        NewNode = daynames(dataVal)
        temp = self.head

    def deleteNode(selfs):



l=llist()
#l.head=daynames("sun")
e1=daynames("mon")
e2=daynames("tues")
#l.head.next=e1
l.head=e1

e1.next=e2
e2.next=None
l.atBeginning("sun")
l.atLast("hello")
l.atBeginning("jj")
l.atLast("kk")
l.printAll()
