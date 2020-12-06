def bubbleSort(lst:list[int]) -> tuple[list[int], int]:
    n = len(lst)
    count = 0
    for i in range(n):
        swapped =  False
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(lst)
                count += 1
                swapped = True
        if not swapped:
            break
    return lst, count

lst = list(map(int, input().split()))
print(bubbleSort(lst))
