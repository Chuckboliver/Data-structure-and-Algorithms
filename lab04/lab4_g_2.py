class Queue :
    class Node:
        def __init__(self,data,priority = 0):
            self.data = data
            self.priority = priority
            self.next = None
        def __str__(self):
            return str(self.data)
    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front == None
    def enQueue(self,item,priority):
        temp = self.Node(item,priority)
        if self.rear == None:
            self.front=self.rear=temp
            return
        self.rear.next = temp
        self.rear = temp
    def deQueue(self):
        if self.isEmpty():
            return "Empty"
        temp = self.front
        maxPriority = 0
        maxNode = self.front
        while temp != None :
            if temp.priority > maxPriority:
                maxPriority = temp.priority
                maxNode = temp
            temp = temp.next
        if maxNode == self.front:
            self.front = self.front.next
        else:
            temp = self.front
            while temp!= None and temp.next != maxNode:
                temp = temp.next
            temp.next = temp.next.next
        if self.front == None:
            self.rear=None
        return maxNode.data
    def __str__(self):
        q = ""
        temp = self.front
        while temp!=None:
            q+=str(temp.data)+" "
            temp = temp.next
        return q


psdQueue = Queue()
priorityCheck = {"EN":0, "ES":1}
w = input("Enter Input : ").split(",")
for i in w:
    c,*otaID = i.split()
    if c == "EN" or c == "ES":
        psdQueue.enQueue(*otaID,priorityCheck[c])
    elif c == "D":
        print(psdQueue.deQueue())
    #print(psdQueue)
