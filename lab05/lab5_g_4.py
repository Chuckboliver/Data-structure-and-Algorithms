class Node:
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.data)

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def nodeAt(self,pos):
        if pos > self.size - 1 or self.isEmpty():
            return
        temp = self.head
        for _ in range(pos):
            temp = temp.next
        return temp
    def insertBefore(self,pos,data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            tNode = self.nodeAt(pos)
            if self.head == tNode:
                self.head = newNode
            newNode.prev = tNode.prev
            tNode.prev = newNode
            if newNode.prev is not None:
                newNode.prev.next = newNode
            newNode.next = tNode
            self.size += 1
    def insertAfter(self,pos,data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            tNode = self.nodeAt(pos)
            if self.tail == tNode:
                self.tail = newNode
            newNode.next = tNode.next
            tNode.next = newNode
            newNode.prev = tNode
            if newNode.next is not None:
                newNode.next.prev = newNode
        self.size += 1
    def remove(self,data):
        if self.isEmpty():
            return
        temp = self.head
        while temp is not None:
            if temp.data == data:
                if self.head == temp:
                    self.head = temp.next
                    if self.head is not None:
                        self.head.prev = None
                elif self.tail == temp:
                    self.tail = temp.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
                self.size -= 1
                return
            temp = temp.next
    def removeAt(self,pos):
        tNode = self.nodeAt(pos)
        if self.isEmpty() or tNode is None:
            return
        if self.head == tNode:
            self.head = tNode.next
            if self.head is not None:
                self.head.prev = None
        elif self.tail == tNode:
            self.tail = tNode.prev
            if self.tail is not None:
                self.tail.next = None
        else:
            tNode.next.prev = tNode.prev
            tNode.prev.next = tNode.next
        self.size -= 1
    def index(self,item):
        t = self.head
        index = 0
        while t is not None:
            if t.data == item:
                return index
            t = t.next
            index += 1
        return None
    def __str__(self):
        s = ""
        t = self.head
        while t is not None:
            s += str(t.data)+" "
            t = t.next
        return s
queries = input("Enter Input : ").split(",")
line = DLL()
line.insertAfter(0,"|")
for q in queries:
    cmd,*arg = q.split()
    curpos = line.index("|")
    if cmd == "I":
        line.insertBefore(curpos,*arg)
    elif cmd == "L":
        if curpos > 0 :
            line.remove("|")
            line.insertBefore(curpos-1,"|")
    elif cmd == "R":
        if curpos < len(line) - 1:
            line.remove("|")
            line.insertAfter(curpos,"|")
    elif cmd == "D":
        line.removeAt(curpos+1)
    elif cmd == "B":
        if curpos != 0:
            line.removeAt(curpos-1)
print(line)