from collections import deque

class Node:

    def __init__(self, key:str) -> None:
        self._data = key
        self._left = None
        self._right = None
    
    def __str__(self) -> str:
        return self._data

def expression_tree(postfix:str) -> Node:
    """
    get expression tree from postfix 
    return as root of tree.
    """
    stack = deque()
    for ch in postfix:
        if ch not in {'+', '-', '*', '/', '^'}:
            stack.append(Node(ch))
        else:
            middle_node = Node(ch)
            right_node = stack.pop()
            left_node = stack.pop()
            middle_node ._right = right_node
            middle_node._left = left_node
            stack.append(middle_node)
    return stack.pop()

def evaluate_expression_tree(root:Node) -> float:
    if root is None:
        return 0
    if root._left is None and root._right is None:
        return float(root._data)
    left_sum = evaluate_expression_tree(root._left)
    right_sum = evaluate_expression_tree(root._right)
    if root._data == '+':
        return left_sum + right_sum
    elif root._data == '-':
        return left_sum - right_sum
    elif root._data == '*':
        return left_sum * right_sum
    elif root._data == '/':
        return left_sum / right_sum
    elif root._data == '^':
        return left_sum ** right_sum
    else:
        raise ArithmeticError(root._data)
def infix_to_postfix(infix:str) -> str:
    """
    infix to postfix
    return as string.
    """
    stack = deque()
    precedence = {'+':1, '-':1,
                  '*':2, '/':2,
                  '^':3, '(':-9
                }
    output = ""
    for ch in infix:
        if ch not in {'+', '-', '*', '/', '^', '(', ')'}:
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while len(stack) > 0 and\
                stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while len(stack) > 0 and\
                 precedence[stack[-1]] >= precedence[ch]:
                output += stack.pop()
            stack.append(ch)
    while len(stack) > 0:
        output += stack.pop()
    return output

if __name__ == "__main__":
    postfix = infix_to_postfix(input())
    expression_tree_root = expression_tree(postfix)
    evaluate_number = evaluate_expression_tree(expression_tree_root)
    print(f"{evaluate_number:g}")