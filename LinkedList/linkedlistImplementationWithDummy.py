class Lists:
    class Node:
        def __init__(self,data = None,next = None):
            self.data = data
            self.next = None
        def __str__(self):
            return str(self.data)
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
    def append(self,data):
        p = self.Node(data)
        # t =self.head
        # while t.next != None:
        #     t = t.next
        # t.next = p
        self.tail.next = p
        self.tail = p
        self.size += 1
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
    def search(self,data):
        p = self.head.next
        while p != None:
            if p.data == data:
                return p
            p = p.next
        return None
    def remove(self,data):
        if self.head.next == None:
            return
        
        p = self.head.next
        while p.next != None and p.next.data != data:
            p = p.next
        p.next = p.next.next
        self.size -= 1
l = Lists()
for i in range(1,100,2):
    l.append(i)
print(l)
print(len(l))
l.remove(5)
print(l)
print(len(l))
l.remove(99)
print(l)
print(len(l))
l.deleteAfter(0)
print(l)
print(len(l))
print(l.tail.data)
l.append(69)
print(l.tail.data)
print(l.head.data)