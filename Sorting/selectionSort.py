def selectionSort(lst:list[int]) -> tuple[list[int], int]:
    n = len(lst)
    count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(lst)
        count += 1
    return lst, count

print(selectionSort(list(map(int, input().split()))))