def staircase(i,n):
    if i == n:
        return
    if n>0:
        print("_"*(n-1-i)+"#"*(i+1))
        staircase(i+1,n)
    else:
        print("_"*abs(i)+"#"*(abs(n)-abs(i)))
        staircase(i-1,n)

n = int(input("Enter Input : "))
if n!=0:
    staircase(0,n)
else:
    print("Not Draw!")