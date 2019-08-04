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
        l=[]
        if root:
            l=self.inOrder(root.left)
            l.append(root.data)
            l=l+self.inOrder(root.right)
        return l
    def preOrder(self,root):
        l=[]
        if root:
            l.append(root.data)
            l=l+self.preOrder(root.left)
            l=l+self.preOrder(root.right)
        return l
    def postOrder(self,root):
        l=[]
        if root:
            l=self.preOrder(root.right)
            l=l+self.preOrder(root.left)
            l.append(root.data)
        return l
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
    print(root.inOrder(root))
    print(root.preOrder(root))
    print(root.postOrder(root))
    root.levelOrder()

