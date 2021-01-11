from collections import deque

class Node:
    """
    data node
    """
    def __init__(self, data: int) -> None:
        self.key = data
        self.left = None
        self.right = None

def inorder(node: Node) -> None:
    """
    depth first traversal for binary tree 
    """
    if node is None:
        return
    inorder(node.left)
    print(node.key, end = " ")
    inorder(node.right)

def insert(node: Node, key: int) -> Node:
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

def delete(root: Node, key: int) -> Node:
    """
    delete element from binary tree and put deepest node to maintain  binary tree.
    """
    def __delete_deepest_util(root: Node, del_node: Node) -> None:
        if root is del_node:
            root = None
            return
        queue = deque()
        queue.append(root)
        while len(queue):
            parent: Node = queue.popleft()
            if parent.left is not None:
                if parent.left is del_node:
                    parent.left = None
                    return
                else:
                    queue.append(parent.left)
            if parent.right is not None:
                if parent.right is del_node:
                    parent.right = None
                    return
                else:
                    queue.append(parent.right)
    if root is None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node: Node = None
    temp: Node = None
    queue = deque()
    queue.append(root)
    while len(queue):
        temp: Node = queue.popleft()
        if temp.key == key:
            key_node = temp
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
    if key_node is not None:
        deepest_key = temp.key
        __delete_deepest_util(root, temp)
        key_node.key = deepest_key
    return root

def is_mirror(root: Node) -> bool:
    """
    check if tree is symmetric or not.
    """
    def __is_mirror_check_util(left_node: Node, right_node: Node) -> bool:
    
        if left_node is None and right_node is None:
            return True

        if left_node is not None and\
            right_node is not None and\
            left_node.key == right_node.key:
            return __is_mirror_check_util(left_node.left, right_node.right) and __is_mirror_check_util(left_node.right, right_node.left)
        
        return False
    
    return __is_mirror_check_util(root, root)

def is_foldable(root: Node) -> bool:
    """
    check if tree is foldable or not.
    """
    def __is_foldable_util(left_node: Node, right_node: Node) -> bool:

        if left_node is None and right_node is None:
            return True

        if left_node is not None and\
             right_node is not None:
            return __is_foldable_util(left_node.left, right_node.right) and __is_foldable_util(left_node.right, right_node.left)

        return False
    
    return __is_foldable_util(root, root)

def print_tree(node: Node, level: int = 0) -> None:
    """
    print binary tree
    """
    if node:
        print_tree(node.right, level + 1)
        print('   '*level, node.key)
        print_tree(node.left, level + 1)

if __name__ == "__main__":
    root: Node = None
    for i in list(map(int, input("Enter key to insert : ").split())):
        root = insert(root, i)
    delete(root, 9)
    print_tree(root)
    print(f"Symmetric : {is_mirror(root)}")
    print(f"Foldable : {is_foldable(root)}")