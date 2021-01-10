from collections import deque
class Node:
    def __init__(self, data:int) -> None:
        self.key = data
        self.left = None
        self.right = None

def inorder(node:Node) -> None:
    if node is None:
        return
    inorder(node.left)
    print(node.key, end = " ")
    inorder(node.right)

def insert(node:Node, key:int) -> Node:
    """
    insert element in binary tree
    """
    if node is None:
        return Node(key)
    queue = deque()
    queue.append(node)
    while len(queue):
        temp:Node = queue[0]
        queue.popleft()
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    return node
if __name__ == "__main__":
    root = None
    for i in range(5):
        root = insert(root, i)
    inorder(root)