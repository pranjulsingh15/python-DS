# code for tree
import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, val):
        if val < self.data:
            if self.left is None:
                print("value not found", val)
            else:
                self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                print("value not found", val)
            else:
                self.right.findval(val)
        else:
            print("value found")

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    def preOrder(self, root):
        if root:
            print(root.data, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            self.preOrder(root.right)
            self.preOrder(root.left)
            print(root.data, end=" ")

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

    def levelOrder(self):
        l = queue.Queue(maxsize=500)
        if self is not None:
            l.put(self)
            while not l.empty():
                k = l.get()
                print(k.data, end=" ")
                if k.left:
                    l.put(k.left)
                if k.right:
                    l.put(k.right)

    def height(self, root):
        if root is not None:

            leftHeight = self.height(root.left)
            rightHeight = self.height(root.right)
            return max(leftHeight, rightHeight) + 1
        else:
            return -1

    def getlevel(self, root, data, level):
        if root is None:
            return 0
        if root.data == data:
            return level
        downlevel = self.getlevel(root.left, data, level + 1)
        if downlevel != 0:
            return downlevel
        downlevel = self.getlevel(root.right, data, level + 1)
        return downlevel


if __name__ == '__main__':
    root = Node(23)
    root.insert(60)
    root.insert(5)
    root.insert(15)
    root.insert(28)
    root.findval(23)
    root.findval(21)
    root.printTree()
    root.inOrder(root)
    print()
    root.preOrder(root)
    print()
    root.postOrder(root)
    print()
    root.levelOrder()
    print()
    height = root.height(root)
    print("height = ", height)
    print("level =",root.getlevel(root, 28, 1))
