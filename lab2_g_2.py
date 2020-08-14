class Calculator :
    ### Enter Your Code Here ###
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def __add__(self):
        ###Enter Your Code For Add Number###
        return self.a+self.b
    def __sub__(self):
        ###Enter Your Code For Sub Number###
        return self.a-self.b
    def __mul__(self):
        ###Enter Your Code For Mul Number###
        return self.a*self.b
    def __truediv__(self):
        ###Enter Your Code For Div Number###
        return self.a/self.b
x,y = map(int,input("Enter num1 num2 : ").split(","))
cal1 = Calculator(x,y)
print(cal1.__add__(),cal1.__sub__(),cal1.__mul__(),cal1.__truediv__(),sep = "\n")

