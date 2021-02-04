def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)
x,y = map(int,input("Enter Input : ").split())

if x!=0 or y!=0:
    if x<0 and y < 0:
        x,y = min(x,y),max(x,y)
    else:
        x,y = max(x,y),min(x,y)
    print(f"The gcd of {x} and {y} is : {gcd(abs(x),abs(y))}")
else:
    print("Error! must be not all zero.")