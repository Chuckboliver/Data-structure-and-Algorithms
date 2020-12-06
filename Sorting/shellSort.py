def shellSort(lst:list[int]) -> tuple[list[int], int]:
    n = len(lst)
    count = 0
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and\
                lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
            count += 1
            print(lst)
        gap //= 2 
    return lst, count

print(shellSort(list(map(int, input().split()))))