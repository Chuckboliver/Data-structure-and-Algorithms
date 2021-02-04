"""
AVL Tree Implement tutorial
"""
class Node:
    """
    Node object for tree data structure.
    """
    def __init__(self, key: int) -> None:
        self._key: int = key
        self._left: Node = None
        self._right: Node = None
        self._height: int = 1
    def __str__(self) -> str:
        return str(self._key)

class AVL:
    """
    AVL tree object
    """
    def __init__(self) -> None:
        self.__root: Node = None
        self.__size: int = 0

    def __len__(self) -> int:
        return self.__size
    
    def height(self) -> int:
        """
        get height of tree.\n
        height of leaf node is 0.
        """
        def __height_util(root: Node) -> int:
            if root is None:
                return 0
            return 1 + max(
                            __height_util(root._left),
                            __height_util(root._right)
                            )
        return __height_util(self.__root)

    def get_root(self) -> Node:
        return self.__root

    def __get_height(self, node: Node) -> int:
        if node is None:
            return 0
        return node._height

    def __get_balance(self, root: Node) -> int:
        if root is None:
            return 0
        return self.__get_height(root._left) - self.__get_height(root._right)

    def __update_height(self, node: Node) -> None:
        node._height = 1 + max(
                                self.__get_height(node._left),
                                self.__get_height(node._right)
                            )

    def __right_rotation(self, root: Node) -> Node:
        center_pivot = root._left
        rchild_of_center = center_pivot._right
        center_pivot._right = root
        root._left = rchild_of_center
        self.__update_height(root)
        self.__update_height(center_pivot)
        return center_pivot

    def __left_rotation(self, root: Node) -> Node:
        center_pivot = root._right
        lchild_of_center = center_pivot._left
        center_pivot._left = root
        root._right = lchild_of_center
        self.__update_height(root)
        self.__update_height(center_pivot)
        return center_pivot

    def insert(self, key: int) -> None:
        """
        Insert data to AVL tree:
        1.) Perform normal BST insert .
        2.) Update the height of parent node.
        3.) Get the balance factor.
        4.) If unbalance try out 4 cases.
        """
        def __insert_util(root: Node, key: int) -> Node:
            if root is None:        #Perform normal BST insertion
                return Node(key)
            elif root._key > key:
                root._left = __insert_util(root._left, key)
            elif root._key <= key:
                root._right = __insert_util(root._right, key)
            
            self.__update_height(root)

            balance = self.__get_balance(root)      #get balance factor
            if balance > 1:         #Rotate if unbalanced
                if key < root._left._key: 
                    return self.__right_rotation(root)
                else:
                    root._left = self.__left_rotation(root._left)
                    return self.__right_rotation(root)
            if balance < -1:
                if key >= root._right._key:
                    return self.__left_rotation(root)
                else:
                    root._right = self.__right_rotation(root._right)
                    return self.__left_rotation(root)
            return root
        self.__root = __insert_util(self.__root, key)
        self.__size += 1
    
    def delete(self, key: int) -> None:
        """
        Delete data from AVL tree:
        1.) Standard BST delete.
        2.) Update the height of parent node.
        3.) Get the balance factor.
        4.) If unbalanced try out 4 cases.
        """
        def __delete_util(root: Node, key: int) -> Node:

            def __get_min_val_node(root: Node) -> Node:
                if root is None or root._left is None:
                    return root
                return __get_min_val_node(root._left)
                
            if root is None:
                return root
            elif key < root._key:
                root._left = __delete_util(root._left, key)
            elif key > root._key:
                root._right = __delete_util(root._right, key)
            else:
                if root._left is None:
                    temp = root._right
                    root = None
                    return temp
                elif root._right is None:
                    temp = root._left
                    root = None
                    return temp
                temp = __get_min_val_node(root._right)
                root._key = temp._key
                root._right = __delete_util(root._right, temp._key)

            if root is None:
                return root

            self.__update_height(root)
            balance = self.__get_balance(root)
            if balance > 1:
                if self.__get_balance(root._left) >= 0:
                    return self.__right_rotation(root)
                else:
                    root._left = self.__left_rotation(root._left)
                    return self.__right_rotation(root)
            elif balance < -1:
                if self.__get_balance(root._right) <= 0:
                    return self.__left_rotation(root)
                else:
                    root._right = self.__right_rotation(root._right)
                    return self.__left_rotation(root)

            return root

        self.__root = __delete_util(self.__root, key)
        self.__size -= 1

def print_tree(node: Node, level: int = 0) -> None:
    """
    display BST
    """
    if node:
        print_tree(node._right, level + 1)
        print('   '*level, node._key)
        print_tree(node._left, level + 1)
def preorder(node: Node) -> None:
    """
    display preorder.
    """
    if node is None:
        return
    print(node._key, end=" ")
    preorder(node._left)
    preorder(node._right)
if __name__ == "__main__":
    avl_tree = AVL()
    for key in range(1000):
        avl_tree.insert(key)
    for key in range(999):
        avl_tree.delete(key)
    print_tree(avl_tree.get_root())
    print(f"\nSize : {len(avl_tree)}")
    print(f"Height : {avl_tree.height()}")
    print(f"Root : {avl_tree.get_root()}")