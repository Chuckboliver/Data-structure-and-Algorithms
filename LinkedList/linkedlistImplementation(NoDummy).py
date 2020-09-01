class List:
    class Node :
        def __init__(self,data = None,next = None):
            self.data =data
            self.next =None
        def __str__(self):
            return str(self.data)
    def __init__(self,head = None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else :
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
                self.tail = t
    def __str__(self):
        s = "Linked data : "
        p = self.head
        while p != None:
            s += str(p.data)+" "
            p = p.next
        return s
    def __len__(self):
        return self.size
    def append(self,data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
        while t.next != None:
            t = t.next
        t.next = p
        self.size += 1
    def nodeAt(self,i):
        p = self.head
        for j in range(i):
            p = p.next
        return p
    def deleteAfter(self,i):
        q = self.nodeAt(i)
        q.next = q.next.next
    def insertAfter(self,data,i):
        p = self.Node(data)
        q = self.nodeAt(i)
        p.next = q.next
        q.next = p
    def isEmpty(self):
        return self.size == 0
    def search(self,data):
        p = self.head
        while p != None:
            if p.data == data:
                return p
            p = p.next
        return None
    def remove(self,data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            p = self.head
            while p.next != None and p.next.data != data:
                p = p.next
            p.next = p.next.next
            self.size -= 1
