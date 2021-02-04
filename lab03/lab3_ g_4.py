class Calculator:
    def __init__(self,exp=""):
        self.top = -1
        self.array = list()
        self.instructions = exp.split()
    
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
        self.top += 1
        self.array.append(ele)
    def isOperand(self,ch):
        return ch.isdigit()
    def isAlpha(self,ch):
        return ch.isalpha() and len(ch)!=3
    def isOperator(self,ch):
        return ch in ["+","-","*","/","^"]
    def run(self):
        #print(self.instructions)
        for ins in self.instructions:
            if self.isAlpha(ins):
                return f"Invalid instruction: {ins}"
            elif self.isOperand(ins):
                self.push(ins)
            elif self.isOperator(ins):
                operand1 = self.pop()
                operand2 = self.pop()
                self.push(str(eval(operand1+ins+operand2)) )
            else :
                if ins == "DUP":
                    self.push(self.peek())
                elif ins == "POP":
                    self.pop()
        p = self.pop()
        if p:
            return f"{float(p):g}"
        else:
            return 0
print("* Stack Calculator *")
arg = input("Enter arguments : ")
print(Calculator(arg).run())
