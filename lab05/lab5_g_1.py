class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.sizes = 0
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        # Code Here
        newNode = Node(item)
        if self.head is None :
            self.head = newNode
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = newNode
        self.sizes += 1
    def addHead(self, item):
        # Code Here
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.sizes += 1
    def search(self, item):
        # Code Here
        t = self.head
        while t is not None:
            if t.value == item:
                return "Found"
            t = t.next
        return "Not Found"
    def index(self, item):
        # Code Here
        t = self.head
        index = 0
        while t is not None:
            if t.value == item:
                return index
            t = t.next
            index += 1
        return -1
    def size(self):
        # Code Here
        return self.sizes
    def pop(self, pos):
        # Code Here
        if pos>self.sizes - 1 or pos < 0:
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
        else :
            t = self.head
            for _ in range(pos-1):
                t = t.next
            
            temp = t.next
            t.next = temp.next
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
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)