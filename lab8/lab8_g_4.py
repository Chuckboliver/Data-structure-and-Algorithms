from collections import deque
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def insertBST(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insertBST(node.left, data)
    else:
        node.right = insertBST(node.right, data)
    return node

def insertBinaryTree(root, data):
    if root is None:
        
        return Node(data)
    
    q = deque()
    q.append(root)
    while len(q):
        p = q.popleft()
        if p.left is None:
            p.left = Node(data)
            break
        else:
            q.append(p.left)
        if p.right is None:
            p.right = Node(data)
            break
        else:
            q.append(p.right)
    return root
def sums(node):
    if node is None:
        return 0
    return node.data + sums(node.left) + sums(node.right)

def hierarchy(node):
    if node is None:
        return 0
    node.data += hierarchy(node.left) + hierarchy(node.right)
    return node.data

def printTree(node, level = 0):
    if node:
        printTree(node.right, level + 1)
        print('   '*level, node.data)
        printTree(node.left, level + 1)

def BFS(root, n):
    q = deque()
    q.append(root)
    count = 0
    while len(q):
        p = q.popleft()
        if count == n:
            return p.data
        q.append(p.left)
        q.append(p.right)
        count+=1
    return None

def compare(root,a,b):
    sA = BFS(root,a)
    sB = BFS(root,b)
    if sA > sB:
        print(f"{a}>{b}")
    elif sA < sB:
        print(f"{a}<{b}")
    else:
        print(f"{a}={b}")
root = None   
knight, cmp = input("Enter Input : ").split('/')
knight = list(map(int, knight.split()))
cmp = list((int(k[0]),int(k[2])) for k in cmp.split(','))
for i in knight:
    root = insertBinaryTree(root, i)
print(sums(root))
#printTree(root)
hierarchy(root)
#printTree(root)
for a,b in cmp:
    compare(root,a,b)