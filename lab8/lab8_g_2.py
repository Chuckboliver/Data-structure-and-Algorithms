import sys
class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.data)

def insert(node:Node, data:int) -> Node:
    if node is None:
        return Node(data)
    if data >= node.data:
        node.right = insert(node.right, data)
    else:
        node.left = insert(node.left, data)
    return node

def printTree(node:Node, level:int = 0) -> None:
    if node:
        printTree(node.right, level + 1)
        print('     '*level, node.data)
        printTree(node.left, level + 1)

def closestValue(node:Node, n:int, closest:int):
    if node is None:
        return closest
    if closest is None:
        closest = node.data
    elif abs(node.data - n) < abs(n - closest):
        closest = node.data
    if n < node.data:
        return closestValue(node.left, n, closest)
    else:
        return closestValue(node.right, n, closest)

def maxDepth(node): 
    if node is None: 
        return 0 ;  
  
    else : 
  
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
  
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1

def height(node):
    return node and 1 + max(height(node.left), height(node.right)) or 0

def height2(node):
    if node is None:
        return -1
    return 1 + max(height2(node.left), height2(node.right))
def isBST(node, lower = 0, upper = 100):
    if node is None:
        return True
    if node.data < lower or node.data > upper:
        return False
    return isBST(node.left, lower, upper - 1) and isBST(node.right, lower, upper)
l,n = input("Enter Input : ").split('/')
root = None
for i in l.split():
    root = insert(root, int(i))
    printTree(root)
    print("--------------------------------------------------")

print(f"Closest value of {n} : {closestValue(root, int(n), None)}")

#print(height2(root))
#print(maxDepth(root))
#print(isBST(root))