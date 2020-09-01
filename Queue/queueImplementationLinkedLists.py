class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
class Queue :
    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front == None
    def enQueue(self,item):
        temp = Node(item)
        if self.rear == None:
            self.front=self.rear=temp
            return
        self.rear.next = temp
        self.rear = temp
    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear=None
    def __str__(self):
        q = ""
        temp = self.front
        while temp.next!=None:
            q+=str(temp.data)+" "
            temp = temp.next
        q+=str(temp.data)
        return q
q1 = Queue()
[q1.enQueue(i) for i in range(1,101,2)]
print(q1)
