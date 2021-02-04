"""
Binary Search Tree Implement tutorial.
"""
class Node:
    """
    data node.
    """
    def __init__(self, key: int) -> None:
        self._key = key
        self._left = None
        self._right = None
class BST:
    """
    Binary Search Tree obj.
    """
    def __init__(self) -> None:
        self.__root = None
    
    def insert(self, key: int) -> None:
        """
        insert key into BST.
        """
        def __insert_util(root: Node, key: int) -> Node:
            if root is None:
                return Node(key)
            elif key < root._key:
                root._left = __insert_util(root._left, key)
            else:
                root._right = __insert_util(root._right, key)
            return root
        
        self.__root = __insert_util(self.__root, key)

    def delete(self, key: int) -> None:
        """
        delete key from BST.
        """
        def __delete_util(root: Node, key: int) -> Node:

            def __deepest_node(root: Node) -> Node:
                if root is None or root._left is None:
                    return root
                return __deepest_node(root._left)

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
                else:
                     deepest_node = __deepest_node(root._right)
                     root._key = deepest_node._key
                     root._right = __delete_util(root._right, deepest_node._key)
            return root

if __name__ == "__main__":
    tree = BST()    
    for i in range(int(input())):
        tree.insert(i)
