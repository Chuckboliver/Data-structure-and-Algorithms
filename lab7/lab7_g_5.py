class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.val)

def insert(root,data):
    if root is None:
        return Node(data)
    if root.val < data:
        root.right = insert(root.right,data)
    else:
        root.left = insert(root.left,data)
    return root

def isOperator(ch):
    return ch in {'+','-','*','/'}

def ExpressionTree(postfix):
    stack = list()
    for ch in postfix:
        if not isOperator(ch):
            stack.append(Node(ch))
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            node = Node(ch)
            node.left = t2
            node.right = t1
            stack.append(node)
    return stack.pop()

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

def inorder(node):
    if node is None:
        return
    if node.left:
        print("(",end="")
    inorder(node.left)
    print(node.val,end="")
    inorder(node.right)
    if node.right:
        print(")",end="")
def preorder(node):
    if node is None:
        return
    print(node.val,end="")
    preorder(node.left)
    preorder(node.right)
postfix = input("Enter Postfix : ")
print("Tree : ")
ept = ExpressionTree(postfix)
printTree(ept)
print("--------------------------------------------------")
print("Infix : ",end="")
inorder(ept)
print("\nPrefix : ",end="")
preorder(ept)