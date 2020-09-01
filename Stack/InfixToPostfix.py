class Conversion :
    def __init__(self,expression = ""):
        self.top = -1
        self.array = list()
        self.output = ""
        self.precedence = {"+":1, "-":1, "*":2, "/":2, "^":3}
        self.expression =expression
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
        return ch.isalpha() or ch.isdigit()
    def notGreater(self,key) :
        try:
            a = self.precedence[key]
            b = self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False
    def __str__(self):
        return self.output
    def InfixToPostfix(self):
        self.__init__(expression= self.expression)
        print(f"Inbound InPo : {self.expression}")
        for char in self.expression:
            #print(f"Current char --> {char}")
            if self.isOperand(char):
                self.output += char
                #print(f"Append {char} in output --> Output : {self.output}")
            elif char == "(":
                self.push(char)
                #print(f"Push ( in stack.")
            elif char == ")":
                #print(f") found --> pop stack and append to output until (\n--------------------------------------")
                while not self.isEmpty() and self.peek() != "(":
                    operator = self.pop()
                    self.output += operator
                    #print(f"Pop {operator} from stack and Append {operator} to output. --> Stack : {self.array}, Output : {self.output}")
                if not self.isEmpty() and self.peek() != "(" :
                    return -1
                else :
                    last = self.pop()
                #print(f"Current output : {self.output}")
                #print(f"Last pop is {last} --> Stack : {self.array}\n--------------------------------------")
            else :
                #print(f"Operator {char} found --> pop stack until precedence is lower\n**************************************")
                while not self.isEmpty() and self.notGreater(char):
                    operator = self.pop()
                    self.output += operator
                    #print(f"Pop {operator} from stack and Append {operator} to output. --> Stack : {self.array}, Output : {self.output}")

                self.push(char)
                #print(f"Current output : {self.output}")
                #print(f"Push {char} to stack. --> Stack : {self.array}\n**************************************")
        #print(f"***Iterate over the expression end pop all the operator from the stack.***")
        while not self.isEmpty() :
            operator = self.pop()
            self.output += operator
            #print(f"Pop {operator} from stack and Append {operator} to output. --> Stack : {self.array}, Output : {self.output}")
        #print(f"Infix-to-Postfix : {self.output}")
        self.expression = self.output
        print(f"Out : {self.output} Ex : {self.expression}")
        return self
    def PostfixToInfix(self):
        self.__init__(expression = self.expression)
        print(f"Inbound PoIn : {self.expression}")
        for char in self.expression:
            if self.isOperand(char) :
                self.push(char)
            else :
                operand1 = self.pop()
                operand2 = self.pop()
                self.push(operand2+char+operand1)
        self.output = self.pop()
        self.expression = self.output
        print(f"Out : {self.output} Ex : {self.expression}")
        return self
exp = input()
print(Conversion(exp).InfixToPostfix())