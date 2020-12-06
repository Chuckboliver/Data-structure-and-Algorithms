def heapify(lst:list[int], n:int, root:int) -> None:
    largest = root
    l = 2 * root + 1
    r = 2 * root + 2
    #See if left child exist and is greater than root
    if l < n and\
        lst[largest] < lst[l]:
        largest = l
    #See if right child exist and is greater than root
    if r < n and\
        lst[largest] < lst[r]:
        largest = r
    #Change root is needed
    if largest != root:
        lst[root], lst[largest] = lst[largest], lst[root]#Swap
        heapify(lst, n, largest)

def heapSort(lst:list[int]) -> list[int]:
    n = len(lst)
    #Build maxHeapby heapify 
    for i in range(n//2 - 1, -1, -1):
        heapify(lst, n, i)
    #One-by-one extract element and heapify root
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0) 
    return lst


lst = list(map(int, input().split()))
print(heapSort(lst)  )
