from itertools import combinations
def addToZero(lst) :
    ans = list()
    if len(lst) < 3:
        return "Array Input Length Must More Than 2"
    for i in combinations(lst,3) :
        if sum(i) == 0 and list(i) not in ans:
            ans.append(list(i))
    return ans
lst = list(map(int,input("Enter Your List : ").split()))
print(addToZero(lst))