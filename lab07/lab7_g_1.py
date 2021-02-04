class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Code Here
        newNode = Node(data)
        fastPtr = self.root
        slowPtr = None
        while fastPtr:
            slowPtr = fastPtr
            if data <fastPtr.data:
                fastPtr = fastPtr.left
            else:
                fastPtr = fastPtr.right
        
        if slowPtr is None:
            slowPtr = newNode
            self.root = slowPtr
        elif data < slowPtr.data:
            slowPtr.left = newNode
        else:
            slowPtr.right = newNode
        return self.root
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)