from collections import Counter
class Node:
    def __init__(self,data, next = None, prev = None):
        self._data = data
        self._next = next
        self._prev = prev
    def __str__(self) :
        return str(self._data)
class DLL:
    def __init__(self):
        self._head = Node(None)
        self._tail = Node(None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0
    def append(self, data):
        newNode = Node(data)
        newNode._prev = self._tail._prev
        newNode._prev._next = newNode
        newNode._next = self._tail
        self._tail._prev = newNode
        self._size += 1
    def push(self, data):
        newNode = Node(data)
        newNode._next = self._head._next
        newNode._next._prev = newNode
        newNode._prev = self._head
        self._head._next = newNode
        self._size += 1
    def __str__(self):
        s = ""
        temp = self._head._next
        while temp is not self._tail:
            s += str(temp._data)+" "
            temp = temp._next
        return s
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def remove(self, data):
        if self.isEmpty():
            return
        temp = self._head._next
        while temp is not self._tail:
            if temp._data == data:
                temp._prev._next = temp._next
                temp._next._prev = temp._prev
                self._size -= 1
                return
            temp = temp._next 
    def removeAtIndex(self,i):
        if self.isEmpty() or i < 0 or i > self._size-1:
            return
        temp = self._head._next
        for index in range(i):
            temp = temp._next
        temp._prev._next = temp._next
        temp._next._prev = temp._prev
        self._size -= 1
    def insert_1(self, pos, data):
        if pos < 0:
            self.push(data)
            return
        if pos > self._size-1:
            self.append(data)
            return
        newNode = Node(data)
        temp = self._head._next
        for _ in range(pos):
            temp = temp._next
        newNode._next = temp
        newNode._prev = temp._prev
        temp._prev = newNode
        newNode._prev._next = newNode
        self._size += 1
    def insert_2(self,pos,data):
        if pos < 0:
            self.push(data)
            return
        if pos > self._size:
            self.append(data)
            return
        newNode = Node(data)
        temp = self._head
        for _ in range(pos):
            temp = temp._next
        newNode._next = temp._next
        if temp._next is not None:
            temp._next._prev = newNode
        temp._next = newNode
        newNode._prev = temp
        self._size += 1
def compare_linkedlist(l1,l2):
    return Counter(l1.__str__().split()) == Counter(l2.__str__().split())

l1 = DLL()
l2 = DLL()
for i in range(int(input())):
    l1.append(i)
    l2.push(i)
l1.insert_2(99,999)
print(compare_linkedlist(l1,l2))
print(l1)