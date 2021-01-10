def partition(lst:list[int], low:int, high:int) -> int:
    i = low - 1
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1 #return partition index
def quickSort(lst:list[int], low:int, high:int) -> list[int]:
    if low < high:
        partitioningIndex = partition(lst, low, high)
        quickSort(lst, low, partitioningIndex - 1)
        quickSort(lst, partitioningIndex + 1, high)
    return lst

lst = list(map(int, input().split()))
print(quickSort(lst, 0, len(lst) - 1))  
