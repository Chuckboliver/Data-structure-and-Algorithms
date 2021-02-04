class Exp:
    def __init__(self,exp=""):
        self.top = -1
        self.array = list()
        self.output = ""
        self.priority = {"+":1, "-":1, "*":2, "/":2, "^":3}
        self.expression = exp
    def isEmpty(self):
        return self.top == -1
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return None
    def push(self,ele):
        self.top+=1
        self.array.append(ele)
    def isOperand(self,ch):
        return ch.isalpha() or ch.isdigit()
    def isLowPriority(self,ch):
        try:
            pr1 = self.priority[ch]
            pr2 = self.priority[self.peek()]
            return pr1<=pr2
        except KeyError:
            return False
    def InfixToPostfix(self):
        for char in self.expression:
            if self.isOperand(char):
                self.output += char
            elif char == "(":
                self.push(char)
            elif char == ")":
                while not self.isEmpty() and self.peek() != "(":
                    self.output += self.pop()
                self.pop()
            else:
                while not self.isEmpty() and self.isLowPriority(char):
                    self.output += self.pop()
                self.push(char)
        while not self.isEmpty():
            self.output += self.pop()
        return self.output

exp = input("Enter Infix : ")
print(f"Postfix : {Exp(exp).InfixToPostfix()}")
