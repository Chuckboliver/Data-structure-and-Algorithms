def mergeSort(lst:list[int]) -> list[int]:
    n = len(lst)
    if n > 1:
        mid = n // 2 #find middle point to divide
        L = lst[:mid] #divide first half
        R = lst[mid:] #divide second half
        mergeSort(L) #mergesort the first half
        mergeSort(R) #mergesort the second half
        #Copy data to temp list
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        #Checking left element was left
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1 
    return lst

print(mergeSort(list(map(int, input().split()))))  