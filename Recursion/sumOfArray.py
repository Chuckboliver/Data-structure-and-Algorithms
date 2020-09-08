def sums(lst,n):
    if n == 0:
        return 0
    if n == 1:
        return lst[0]
    return sums(lst,n-1)+lst[n-1]

l = list(range(1,10))
print(l)
print(sums(l,len(l)))