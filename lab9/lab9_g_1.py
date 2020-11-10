def bubbleSort(ls, st, nd, n):
    if st == n:
        return ls
    if nd == n:
        return bubbleSort(ls ,st + 1, st + 1 ,n)
    if ls[st] > ls[nd]:
        ls[st], ls[nd] = ls[nd], ls[st]
    return bubbleSort(ls, st, nd + 1, n)


ls = list(map(int, input("Enter Input : ").split()))
print(bubbleSort(ls ,0, 0, len(ls)))