class Stack:
    def __init__(self,lists:list = None) -> None:
        if lists is not None:
            self._items = lists
            self._size = len(lists)
        else:
            self._items = []
            self._size = 0
    def isEmpty(self) -> bool:
        return self._size == 0
    def peek(self) :
        if not self.isEmpty():
            return self._items[-1]
        return None
    def push(self,data) -> None:
        self._items.append(data)
        self._size += 1
    def pop(self):
        if not self.isEmpty():
            self._size -= 1
            return self._items.pop()
        return None
    def __len__(self) -> int:
        return self._size
    def __str__(self) -> str:
        return " ".join(self._items)
def isNotGreater(ch,stack):
    priority = {
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3
    }
    try:
        a = priority[ch]
        b = priority[stack.peek()]
        return a<=b
    except KeyError:
        return False
def isOperand(ch):
    return ch.isalpha() or ch.isdigit()
def infix2postfix(line):
    chk = Stack()
    output  = ""
    for ch in line:
        if isOperand(ch):
            output += ch
        elif ch == '(':
            chk.push(ch)
        elif ch == ')':
            while not chk.isEmpty() and chk.peek() != '(':
                output += chk.pop()
            chk.pop()
        else:
            while not chk.isEmpty() and isNotGreater(ch,chk):
                output += chk.pop()
            chk.push(ch)
    while not chk.isEmpty():
        output += chk.pop()

    return output

def postfix2infix(line):
    chk = Stack()
    for ch in line:
        if isOperand(ch):
            chk.push(ch)
        elif ch in "+-*/":
            b = chk.pop()
            a = chk.pop()
            chk.push(f"{a}{ch}{b}")
    return chk.pop()
print(infix2postfix(input()))
print(postfix2infix(input()))
