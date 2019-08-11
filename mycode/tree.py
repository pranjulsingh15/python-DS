#code for tree
import queue
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if(self.data):
            if(data<self.data):
                if(self.left==None):
                    self.left=node(data)
                else:
                    self.left.insert(data)
            if (data > self.data):
                if (self.right == None):
                    self.right=node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def findVal(self,val):
        if (val<self.data):
            if(self.left==None):
                print("value not found",val)
            else:
                self.left.findVal(val)
        elif(val>self.data):
            if(self.right==None):
                print("value not found",val)
            else:
                self.right.findVal(val)
        else:
            print("value found")

    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    def preOrder(self,root):
        if root:
            print(root.data,end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self,root):
        if root:
            self.preOrder(root.right)
            self.preOrder(root.left)
            print(root.data,end=" ")

    def printTree(self):
        if(self.left):
            self.left.printTree()
        print(self.data),
        if(self.right):
            self.right.printTree()

    def levelOrder(self):
        l=queue.Queue(maxsize=500)
        if(self!=None):
            l.put(self)
            while(l.empty()==False):
                k=l.get()
                print(k.data,end=" ")
                if(k.left):
                    l.put(k.left)
                if(k.right):
                    l.put(k.right)

if __name__=='__main__':
    root=node(23)
    root.insert(60)
    root.insert(5)
    root.insert(15)
    root.insert(28)
    root.findVal(23)
    root.findVal(21)
    root.printTree()
    root.inOrder(root)
    print()
    root.preOrder(root)
    print()
    root.postOrder(root)
    print()
    root.levelOrder()

