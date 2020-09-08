class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.next = next
        self.data = data
        self.prev = prev
    def __str__(self):
        return str(self.data)

class DLL:
    def __init__(self):
        self.head = None
    #push element at head
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head  is not None:
            self.head.prev = newNode
        self.head = newNode
    #insert element
    def insertAfter(self,prev_node,data):
        if prev_node is None:
            return
        newNode = Node(data)
        newNode.next = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node
        if newNode.next is not None:
            newNode.next.prev = newNode
    def append(self,data):
        newNode = Node(data)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
         
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode
        newNode.prev = last
        return 
    def printList(self,node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next
        while last is not None:
            print(last.data)
            last =last.prev


l = DLL()
for i in range(100):
    l.append(i)
l.printList(l.head)