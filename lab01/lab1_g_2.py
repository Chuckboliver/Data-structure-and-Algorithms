print("*** multiplication or sum ***")
a,b = map(int,input("Enter num1 num2 : ").split())
print(f"The result is {a+b}"if a*b >1000 else f"The result is {a*b}")