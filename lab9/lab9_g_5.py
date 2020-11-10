def combiSum(lst, target, prod, ans):
    if target == 0:
        ans.append(prod.copy())
    else:
        for i in range(len(lst)):
            complement = target - lst[i]
            prod.append(lst[i])
            combiSum(lst[i+1:], complement, prod, ans)
            prod.pop()

def wp2_bubble(blist):
    n = len(blist)
    while True:
        swapped = False
        for i in range(1, n):
            if len(blist[i-1]) > len(blist[i]):
                blist[i-1], blist[i] = blist[i], blist[i-1]
                swapped = True
        if not swapped:
            break
    return blist
def insertionSort(arr): 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1 
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr
target, ls = input("Enter Input : ").split('/')
target, ls = int(target), list(map(int, ls.split()))
ans = []
combiSum(insertionSort(ls), target, [], ans)
if len(ans) > 0:
    print(*wp2_bubble(ans), sep = "\n")
else:
    print("No Subset")