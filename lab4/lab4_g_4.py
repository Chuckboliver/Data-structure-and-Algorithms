class Queue:
    class Node:
        def __init__(self,data = None,priority = 0,next = None):
            self.data = data
            self.priority = priority
            self.next = None
        def __str__(self):
            return f"<{self.data} {self.priority}>"
    def __init__(self):
        self.head = self.Node(None,None)
        self.tail = self.head
        self.size = 0
        t = self.head.next
        while t != None:
            self.size += 1
            t = t.next
            self.tail =t     
    def __str__(self):
        s=""
        t =self.head.next
        while t != None:
            s+=str(t.data)+" "
            t=t.next
        return s
    def __len__(self):
        return self.size
    def enqueue(self,data,priority):
        p = self.Node(data,priority )
        t = self.head
        if self.isEmpty():
            self.head.next = p
            self.tail = p
        else:
            while t.next != None and not(t.priority == p.priority and t.next.priority != p.priority):
                t = t.next
            p.next = t.next
            t.next = p
        self.size += 1
        #print(f"Enqueue {data} {priority} {self.size}")
    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        temp = self.head.next
        self.head.next = temp.next
        self.size -= 1
        return temp.data
    def nodeAt(self,i):
        p = self.head
        for j in range(i):
            p = p.next
        return p
    def deleteAfter(self,i):
        q = self.nodeAt(i)
        q.next = q.next.next
        self.size -= 1
    def insertAfter(self,data,i):
        p = self.Node(data)
        q = self.nodeAt(i)
        p.next = q.next
        q.next = p
        self.size += 1
    def isEmpty(self):
        return self.size == 0
    def front(self):
        return self.head.next
    def rear(self):
        return self.tail

employee = dict()
q = Queue()
a,b = input("Enter Input : ").split("/")
for i in a.split(","):
    dept,ids = i.split()
    employee[ids] = dept
#print(employee.items())
for i in b.split(","):
    querie = tuple(i.split())
    if querie[0] == "D":
        print(q.dequeue())
    elif querie[0] == "E":
        q.enqueue(querie[1],employee[querie[1]])
        #print(f"this is queue {q}")
