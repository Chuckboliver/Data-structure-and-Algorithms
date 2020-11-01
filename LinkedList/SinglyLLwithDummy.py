class Node:
    def __init__(self,data,next=None) :
        self._data = data
        self._next = next
    def __str__(self):
        return str(self._data)
class SLL:
    def __init__(self):
        self._head = Node(None)
        self._size = 0
    def append(self,data):
        newNode = Node(data)
        temp = self._head
        while temp._next is not None:
            temp = temp._next
        temp._next = newNode
        self._size += 1
    def push(self,data):
        newNode = Node(data)
        newNode._next = self._head._next
        self._head._next = newNode
        self._size += 1
    def insert(self,pos,data):
        if pos > self._size:
            self.append(data)
            return
        if  pos < 0:
            self.push(data)
            return
        newNode = Node(data)
        temp = self._head
        for i in range(pos):
            temp = temp._next
        newNode._next = temp._next
        temp._next = newNode
        self._size += 1
    def remove(self,data):
        if self.isEmpty():
            return
        temp = self._head
        while temp._next is not None:
            if temp._next._data == data:
                temp._next = temp._next._next
                self._size -= 1
                return 
            temp = temp._next
    def removeIndex(self,pos):
        if self.isEmpty() or pos > self._size - 1 or pos < 0:
            return
        temp = self._head
        for i in range(pos):
            temp = temp._next
        temp._next = temp._next._next
        self._size -= 1
    def isEmpty(self):
        return self._size == 0  
    def __len__(self):
        return self._size
    def __str__(self):
        s = ""
        temp = self._head._next
        while temp is not None:
            s += str(temp._data) + " "
            temp = temp._next
        return s
l = SLL()
l2 = SLL()
for i in range(int(input())):
    l.append(i)
    l2.push(i)
l.insert(2,99)
l.remove(0)
l.remove(99)
l.removeIndex(3)
print(l)
print(l2)