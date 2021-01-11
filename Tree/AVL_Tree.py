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

    def __right_rotation(self, root: Node) -> Node:
        center_pivot = root._left
        rchild_of_center = center_pivot._right
        center_pivot._right = root
        root._left = rchild_of_center
        root._height = 1 + max(
                                self.__get_height(root._left),
                                self.__get_height(root._right)
                            )
        center_pivot._height = 1 + max(
                                        self.__get_height(center_pivot._left),
                                        self.__get_height(center_pivot._right)
                                        )
        return center_pivot

    def __left_rotation(self, root: Node) -> Node:
        center_pivot = root._right
        lchild_of_center = center_pivot._left
        center_pivot._left = root
        root._right = lchild_of_center
        root._height = 1 + max(
                                self.__get_height(root._left),
                                self.__get_height(root._right)
                            )
        center_pivot._height = 1 + max(
                                        self.__get_height(center_pivot._left),
                                        self.__get_height(center_pivot._right)
                                        )
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
            
            root._height = 1 + max(self.__get_height(root._left),       #update root's height
                                    self.__get_height(root._right)
                                  )
            balance = self.__get_balance(root)      #get balance factor
            if balance > 1:         #Rotate if unbalanced
                if key < root._left._key: 
                    return self.__right_rotation(root)
                else:
                    root._left = self.__left_rotation(root._left)
                    return self.__right_rotation(root)
            if balance < -1:
                if key > root._right._key:
                    return self.__left_rotation(root)
                else:
                    root._right = self.__right_rotation(root._right)
                    return self.__left_rotation(root)
            return root
        self.__root = __insert_util(self.__root, key)

def print_tree(node: Node, level: int = 0) -> None:
    """
    display BST
    """
    if node:
        print_tree(node._right, level + 1)
        print('   '*level, node._key)
        print_tree(node._left, level + 1)

if __name__ == "__main__":
    avl_tree = AVL()
    for key in list(map(int, input().split())):
        avl_tree.insert(key)
    print_tree(avl_tree.get_root())
