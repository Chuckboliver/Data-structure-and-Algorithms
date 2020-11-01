class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.data)

def insert(node:Node, data:int) -> Node:
    if node is None:
        print('*')
        return Node(data)
    if data >= node.data:
        print('R',end="")
        node.right = insert(node.right, data)
    else:
        print('L',end="")
        node.left = insert(node.left, data)
    return node
root = None
l = list(map(int,input("Enter Input : ").split()))
for i in l:
    root = insert(root, i)