class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes = 0
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here
        newNode = Node(item)
        newNode.next = None
        if self.head is None:
            newNode.previous = None
            self.head = newNode
            self.tail = newNode
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = newNode
            newNode.previous = t
            self.tail = newNode
        self.sizes += 1
        #print(f"{self.head.value} {self.tail.value}")
    def addHead(self, item):
        #Code Here
        newNode = Node(item)
        if self.head is None:
            self.tail = newNode
        newNode.next = self.head
        if self.head is not None:
            self.head.previous = newNode
        self.head = newNode
        self.sizes += 1
    def insert(self, pos, item):
        #Code Here
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            if pos > self.sizes-1:
                self.tail.next = newNode
                newNode.previous = self.tail
                self.tail = newNode
            elif pos < -(self.sizes-1):
                self.head.previous = newNode
                newNode.next = self.head
                self.head = newNode
            elif pos >= 0:
                tNode = self.NodeAt(pos)
                if self.head == tNode:
                    self.head = newNode
                newNode.previous = tNode.previous
                tNode.previous = newNode
                if newNode.previous is not None:
                    newNode.previous.next = newNode
                newNode.next = tNode
            else:
                tNode = self.NodeAt(pos)
                if self.tail == tNode:
                    self.tail = newNode
                newNode.next = tNode.next
                tNode.next = newNode
                if newNode.next is not None:
                    newNode.next.previous = newNode
                newNode.previous = tNode
        self.sizes += 1
    def search(self, item):
        #Code Here
        t = self.head
        while t is not None:
            if t.value == item:
                return "Found"
            t = t.next
        return "Not Found"

    def index(self, item):
        #Code Here
        t = self.head
        index = 0
        while t is not None:
            if t.value == item:
                return index
            t = t.next
            index += 1
        return -1
    def size(self):
        #Code Here
        return self.sizes
    def NodeAt(self,pos):
        if self.isEmpty():
            #print("Node empty!")
            return 
        #approach from head
        if pos >= 0:
            #print("Pos pos")
            temp = self.head
            index = 0
            while temp.next is not None and index != pos :
                temp = temp.next
                index += 1
            #print(f"Node {temp.value}")
            return temp
        #appreoach from tail
        else:
            #print("neg pos")
            temp = self.tail
            index = 0
            while temp.previous is not None and index != pos:
                temp = temp.previous
                index -= 1
            #print(f"Node {temp.value}")
            return temp
    def pop(self, pos):
        #Code Here
        if abs(pos) >= self.sizes:
            return "Out of Range"
        popNode = self.NodeAt(pos)
        if self.head is None or self.tail is None:
            return
        if self.head == popNode:
            self.head = popNode.next
            if self.head is not None:
                self.head.previous = None

        elif self.tail == popNode:
            self.tail = popNode.previous
            if self.tail is not None:
                self.tail.next = None
        else:
            popNode.previous.next = popNode.next
            popNode.next.previous = popNode.previous
        self.sizes -= 1
        return "Success"
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())