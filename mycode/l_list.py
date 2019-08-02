class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        if (self.head==None):
            return True
    def printAll(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def atBegining(self,data):
        if(self.isEmpty()):
            print("this is first node")
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode
    def atLast(self,data):
        newnode=node(data)
        temp=self.head
        while(temp.next):
            temp=temp.next
        newnode.next=None
        temp.next=newnode


if __name__=='__main__':

    ll=linkList()
    #ll.head=node(22)
    #ll.isEmpty()
    ll.atBegining(23)
    ll.atBegining(24)
    ll.atBegining(26)
    ll.atLast(25)
    ll.printAll()


