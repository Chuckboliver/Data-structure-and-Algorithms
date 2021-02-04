class Queue :
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
        def __str__(self):
            return str(self.data)
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
    def isEmpty(self):
        return self.front == None
    def enQueue(self,item):
        temp = self.Node(item)
        print(f"Add {item} index is {self.size}")
        if self.rear == None:
            self.front=self.rear=temp
            self.size += 1
            return
        self.rear.next = temp
        self.rear = temp
        self.size += 1
    def deQueue(self):
        if self.isEmpty():
            print("-1")
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear=None
        self.size -= 1
        print(f"Pop {temp} size in queue is {self.size}")
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        q = "Number in Queue is :  "
        l=[]
        temp = self.front
        while temp!=None:
            l.append(temp.data)
            temp = temp.next
        return q+str(l)
    def __len__(self) :
        return self.size

w = input("Enter Input : ").split(",")
q = Queue()
d = {"E":q.enQueue,"D":q.deQueue}
for i in w:
    c,*item = i.split()
    d[c](*item) if len(item)==1 else d[c]()
print(q)

