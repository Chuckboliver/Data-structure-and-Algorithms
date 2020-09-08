def eat1(n):
    if n == 0:
        return 
    eat1(n-1)
    print(n)

def eat2(n):
    if n==0:
        return
    print(n)
    eat2(n-1)

eat2(5)