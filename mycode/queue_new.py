class Queue:
    def __init__(self):
        self.queue=[]
    def addtoqueue(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    def remove(self):
        if len(self.queue)>0:
            self.queue.pop()
        else:
            print("empty queue")
    def printqueue(self):
        print(self.queue)
if __name__=='__main__':
    q=Queue()
    q.addtoqueue(25)
    q.addtoqueue(55)
    q.addtoqueue(99)
    q.printqueue()
    q.remove()
    q.printqueue()
