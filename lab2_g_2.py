class Calculator :
    ### Enter Your Code Here ###
    def __init__(self,a):
        self.a =a
    def __add__(self,b):
        ###Enter Your Code For Add Number###
        return self.a+b
    def __sub__(self,b):
        ###Enter Your Code For Sub Number###
        return self.a-b
    def __mul__(self,b):
        ###Enter Your Code For Mul Number###
        return self.a*b
    def __truediv__(self,b):
        ###Enter Your Code For Div Number###
        return self.a/b
x,y = map(int,input("Enter num1 num2 : ").split(","))
x = Calculator(x)
#print(cal1.__add__(),cal1.__sub__(),cal1.__mul__(),cal1.__truediv__(),sep = "\n")
print(x+y,x-y,x*y,x/y)
