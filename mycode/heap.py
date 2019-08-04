class maxheap:

    def __init__(self):
        self.heaparray = []

    def getLeft(self, i):
        return 2 * i + 1

    def getRight(self, i):
        return 2 * i + 2

    def getParent(self, i):
        return int(i - 1 / 2)

    def hasLeft(self, i):
        return self.getLeft(i) < len(self.heaparray)

    def hasRight(self, i):
        return self.getRight(i) < len(self.heaparray)

    def hasParent(self, i):
        return self.getParent(i) >= 0

    def swap(self, i, j):
        self.heaparray[i], self.heaparray[j] = self.heaparray[j], self.heaparray[i]

    # time_complexity=o(logn)
    def insertKey(self, key):
        self.heaparray.append(key)
        self.heapifyUp(len(self.heaparray) - 1)

    def heapifyUp(self, i):
        size = len(self.heaparray)
        while (self.hasParent(i) and self.heaparray[i] > self.heaparray[self.getParent(i)]):
            self.swap(i, self.getParent(i))
            i = self.getParent(i)

    def printHeap(self):
        print(self.heaparray)

    def deleteRoot(self):
        if (len(self.heaparray)) == 0:
            return -1
        lastindex = len(self.heaparray) - 1
        self.swap(0, lastindex)
        root = self.heaparray.pop()
        self.heapifyDown(0)
        return root

    def heapifyDown(self, i):
        while self.hasLeft(i):
            maxelementindex = self.getMaxElementIndex(i)
            if maxelementindex == -1:
                break
            elif self.heaparray[i] < self.heaparray[maxelementindex]:
                self.swap(i, maxelementindex)
                i = maxelementindex
            else:
                break

    def getMaxElementIndex(self, i):
        if (self.hasLeft(i)):
            left_index = self.getLeft(i)
            if (self.hasRight(i)):
                right_index = self.getRight(i)
                if self.heaparray[left_index] > self.heaparray[right_index]:
                    return left_index
                else:
                    return right_index
        else:
            return -1


if __name__ == '__main__':
    h = maxheap()
    h.insertKey(44)
    h.insertKey(45)
    h.insertKey(88)
    h.deleteRoot()
    h.printHeap()
