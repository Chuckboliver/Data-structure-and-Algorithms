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

def ParenthesisCheck(string) :
    mapping  = {"{":"}" ,"(":")", "<":">", "[":"]"}
    myStack = Stack()
    for char in word :
        #print(myStack.item())
        if char in "(<{[" :
            myStack.push(char)
            print(f"Push {char} into stack.")
        elif char in ")>}]" :
            print(f"Get close parenthesis : {char}")
            if not myStack.isEmpty() and char == mapping[myStack.peek()]:
                openParen = myStack.pop()
                print(f"Valid parenthesis : {openParen} match {char}")
            else :
                print(f"Invalid parenthesis : {myStack.peek()} not match {char} --> remaining stack size : {myStack.size} --> Stack : {myStack.get_items()}.")
                return False
    if myStack.size == 0:
        print(f"{string} is valid parenthesis.")
        return True
    print(f"{string} is not valid parenthesis --> remaining stack size : {myStack.size} --> Stack : {myStack}.")
    return False
word = input()
ParenthesisCheck(word)