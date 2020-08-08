n = int(input("Enter Input : "))
for i in range(n+2): 
    print("."*(n+1-i) + "#"*(i+1),end="")
    if i==0 or i==n+1 :
        print("+"*(n+2))
    else :
        print("+"+"#"*n+"+")
for i in range(n+2):
    if i==0 or i==n+1 :
        print("#"*(n+2),end="")
    else :
        print("#"+"+"*n+"#",end="")
    print("+"*(n+2-i) + "."*(i))