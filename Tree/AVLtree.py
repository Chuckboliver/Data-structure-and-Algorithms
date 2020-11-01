class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def getBalanceFactor(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def LeftRotate(self, root):
        #choose pivot
        y = root.right
        x = y.left

        #rotate
        y.left = root
        root.right = x

        #update height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def RightRotate(self, root):
        y = root.left
        x = y.right

        y.right = root
        root.left = x

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    
    def insert(self, root, key):

        #normal BST insert
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        #update height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        #get Balance factor
        balance = self.getBalanceFactor(root)

        #if unbalanced try out 4 cases
        #Right rotate
        if  balance > 1 and key < root.left.data:
            return  self.RightRotate(root)
        #Left rotate
        if balance < -1 and key > root.right.data:
            return self.LeftRotate(root)

        #RightLeft rotate
        if balance < -1 and key < root.right.data:
            root.right = self.RightRotate(root.right)
            return self.LeftRotate(root)

        #LeftRight rotate
        if balance > 1 and key > root.left.data:
            root.left = self.LeftRotate(root.left)
            return self.RightRotate(root)

        return root
    def preOrder(self, node):
        if node:
            print(node.data,end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)


def printTree(node, level = 0):
    if node:
        printTree(node.right, level + 1)
        print('   '*level, node.data)
        printTree(node.left, level + 1)
l = list(map(int, input().split()))
Tree = AVL()
root = None
for i in l:
    root = Tree.insert(root, i)

Tree.preOrder(root)
printTree(root)

printTree(root)