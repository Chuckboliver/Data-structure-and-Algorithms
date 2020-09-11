def fac1(n):
    if n == 0:
        return 1
    return n*fac1(n-1)
def fac2(n):
    if n==0:
        return 1
    return fac2(n-1)*n
print(fac1(5))
print(fac2(5))