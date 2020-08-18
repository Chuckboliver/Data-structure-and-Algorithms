class Conversion :
    def __init__(self):
        self.top = -1
        self.array = list()
        self.output = list()
        self.precedence = {"+":1, "-":1, "*":2, "/":2, "^":3}
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        #print(self.array)
            return self.array[-1] 
    def pop(self):
        if not self.isEmpty() :
            self.top -= 1
            return self.array.pop()
        else :
            return None
    def push(self,element):
        self.top += 1
        self.array.append(element)
    def isOperand(self,ch):
        return ch.isalpha()
    def notGreater(self,key) :
        try:
            a = self.precedence[key]
            b = self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False
    def InfixToPostfix(self,expression):
        for char in expression:
            print(f"Current char --> {char}")
            if self.isOperand(char):
                self.output.append(char)
                print(f"Append {char} in output --> Output : {self.output}")
            elif char == "(":
                self.push(char)
                print(f"Push ( in stack.")
            elif char == ")":
                print(f") found --> pop stack and append to output until (\n--------------------------------------")
                while not self.isEmpty() and self.peek() != "(":
                    operand = self.pop()
                    self.output.append(operand)
                    print(f"Pop {operand} from stack and Append {operand} to output. --> Stack : {self.array}, Output : {self.output}")
                # if not self.isEmpty() and self.peek() != "(" :
                #     return -1
                # else :
                last = self.pop()
                print(f"Current output : {self.output}")
                print(f"Last pop is {last} --> Stack : {self.array}\n--------------------------------------")
            else :
                print(f"Operand {char} found --> pop stack until precedence is lower\n**************************************")
                while not self.isEmpty() and self.notGreater(char):
                    operand = self.pop()
                    self.output.append(operand)
                    print(f"Pop {operand} from stack and Append {operand} to output. --> Stack : {self.array}, Output : {self.output}")

                self.push(char)
                print(f"Current output : {self.output}")
                print(f"Push {char} to stack. --> Stack : {self.array}\n**************************************")
        print(f"***Iterate over the expression end pop all the operator from the stack.***")
        while not self.isEmpty() :
            operand = self.pop()
            self.output.append(operand)
            print(f"Pop {operand} from stack and Append {operand} to output. --> Stack : {self.array}, Output : {self.output}")
        ans = "".join(self.output)
        print(f"Infix-to-Postfix : {ans}")

exp = input()
obj = Conversion()
obj.InfixToPostfix(exp)

