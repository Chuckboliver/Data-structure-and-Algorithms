def insertionSort(lst:list[int]) -> tuple[list[int], int]:
    n = len(lst)
    count = 0
    for i in range(1, n):
        key = lst[i]
        j = i - 1 #Before i index
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
        print(lst)
        count += 1
    return lst, count

print(insertionSort(list(map(int, input().split()))))