def MinimumWeight(Weights, n):
    #binary search on interval [max(Weights), sum(Weights)]
    left, right = max(Weights), sum(Weights)
    while left < right:
        mid = left + (right - left)//2
        currentWeight, needBox = 0, 1
        for wt in Weights:
            if currentWeight + wt > mid:
                needBox += 1
                currentWeight = wt
            else:
                currentWeight += wt
        if needBox <= n :
            right = mid 
        else:
            left = mid + 1
    return left

boxs, n = input("Enter Input : ").split('/')
boxs, n = list(map(int, boxs.split())), int(n)
print(f"Minimum weigth for {n} box(es) = {MinimumWeight(boxs, n)}")