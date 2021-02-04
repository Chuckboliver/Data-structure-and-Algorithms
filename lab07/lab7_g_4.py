from collections import deque
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
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end = " ")
        self.inorder(node.right)
    def preorder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    def postorder(self,node):
        if node is None:
            return 
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")
    def BFS(self,node):
        queue = deque()
        queue.append(node)
        while queue:
            popNode = queue.popleft()
            if popNode.left:
                queue.append(popNode.left)
            if popNode.right:
                queue.append(popNode.right)
            print(popNode.data,end = " ")
    def display(self):
        print("Preorder : ",end="")
        self.preorder(self.root)
        print("\nInorder : ",end="")
        self.inorder(self.root)
        print("\nPostorder : ",end="")
        self.postorder(self.root)
        print("\nBreadth : ",end="")
        self.BFS(self.root)
T = BST()
inp = input("Enter Input : ").split()
for i in inp:
    root = T.insert(int(i))
T.display()