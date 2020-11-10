def selection(ls ,n):
    if n == 1:
        return ls
    maxElement  =  max(ls[0:n])
    maxIndex = ls.index(maxElement)
    ls[maxIndex], ls[n - 1] = ls[n - 1], ls[maxIndex]
    if maxIndex != n - 1:
        print(f"swap {ls[maxIndex]} <-> {maxElement} : {ls}")
    return selection(ls , n - 1)

ls = list(map(int, input("Enter Input : ").split()))
print(selection(ls, len(ls)))