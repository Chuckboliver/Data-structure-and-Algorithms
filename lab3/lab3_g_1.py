class Stack :
    def __init__(self, lists = None):
        if lists == None:
            self.items = []
        else :
            self.items = lists
        self.size = 0
    def push(self,item):
        self.items.append(item)
        self.size += 1
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]
        return None
    def isEmpty(self):
        return self.items == []
    def get_items(self):
        return self.items
def ParenthesisCheck(word) :
    mapping  = {"{":"}" ,"(":")", "<":">", "[":"]"}
    myStack = Stack()
    for char in word :
        if char in "(<{[" :
            myStack.push(char)
        elif char in ")>}]" :
            if not myStack.isEmpty() and char == mapping[myStack.peek()]:
                openParen = myStack.pop()
            else :
                return "Unmatched ! ! !"
    if myStack.size == 0:
        return "Matched ! ! !"
    return "Unmatched ! ! !"

w = input("Enter Input : ")
print(f"Parentheses : {ParenthesisCheck(w)}")