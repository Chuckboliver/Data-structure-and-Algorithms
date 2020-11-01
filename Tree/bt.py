
def safeSpot(ans,n):
    if ans == []:
        return True
    # ptr = len(ans) - 1
    # newPtr = ptr + 1
    # while ptr >= 0 :
    #     if ans[ptr] == n and newPtr - ptr <= n:
    #         return False
    #     ptr -= 1
    # return True
    if n in ans and len(ans) >= n + 1 and ans[len(ans) - 1 - n] == n:
        return True
    if n not in ans:
        return True
    return False


def isFull(ans:list, n):
    #already have 2 n in ans
    return ans.count(n) == 2


def ChooseNum(q,ans,out):
    #base case
    #if ans size == 2q append ans
    if len(ans) == 2*len(q):
        if ans not in out:
            out.append([i for i in ans])
    else:
        #chooose num
        for num in q:
            #if correct
            if safeSpot(ans, num) and not isFull(ans, num):
                #append choose number to ans
                ans.append(num)
                #find next number to append to ans
                #if finish find answer return True
                ChooseNum(q, ans, out)
                #Backtracking pop wrong number
                ans.pop()
        #No correct number to choose
        return False



n = int(input())

ls = list(range(1,n+1))
# perm = []
# permutation(ls,0,len(ls)-1, perm)
out = []
ChooseNum(ls,[], out)
print(len(out))
print(*out,sep = "\n")
