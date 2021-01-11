class Node:
    """
    data node.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    """
    AVL tree object.
    """
    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def left_rotate(self, root:Node) -> Node:
        #choose pivot
        y = root.right
        x = y.left

        #rotate
        y.left = root
        root.right = x

        #update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, root:Node) -> Node:
        y = root.left
        x = y.right

        y.right = root
        root.left = x

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    
    def insert(self, root:Node, key:int) -> Node:

        #normal BST insert
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        #update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        #get Balance factor
        balance = self.get_balance_factor(root)

        #if unbalanced try out 4 cases
        #Right rotate
        if  balance > 1 and key < root.left.data:
            return  self.right_rotate(root)
        #Left rotate
        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)

        #RightLeft rotate
        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        #LeftRight rotate
        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        return root
    def preorder(self, node:Node) -> None:
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


def print_tree(node:Node, level:int = 0) -> None:
    if node:
        print_tree(node.right, level + 1)
        print('   '*level, node.data)
        print_tree(node.left, level + 1)


if __name__ == "__main__":
    l = list(map(int, input().split()))
    Tree = AVL()
    root: Node = None
    for i in l:
        root = Tree.insert(root, i)
    print_tree(root)