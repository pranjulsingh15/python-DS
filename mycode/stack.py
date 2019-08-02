class stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def remove(self):
        size = len(self.stack)
        if (size <= 0):
            print("stack empty")
        else:
            self.stack.pop()

    def printAll(self):
        print(self.stack)

    def maximum(self):
        print(max(self.stack))

if __name__=='__main__':

    n = int(input())
    astack = stack()
    for i in range(n):
        q = input().split(" ")
        if (int(q[0]) == 1):
            astack.add(int(q[1]))
        if (int(q[0]) == 2):
            astack.remove()
        if (int(q[0]) == 3):
            astack.maximum()




