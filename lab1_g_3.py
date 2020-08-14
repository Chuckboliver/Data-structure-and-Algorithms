import math

def pm(ls):
    size = len(ls)
    if size == 2:# if size=2 swap then return as list
        ls[0],ls[1] = ls[1],ls[0]
        return ls
    memIndex.setdefault(size,size-1) #write index of each level in dict
    coreNumber = ls.pop(memIndex[size]) #split coreNumber from subPattern and wait for insert
    memIndex[size] = (memIndex[size]+1)%size #step up index by 1    if index > size-1 then it return to 0
    if memIndex[size] == 0:#get subPattern of low level if index run to 0
        pm(ls)#call this function again to get subPattern 
        ls.insert(memIndex[size],coreNumber)#insert coreNumber in index then return to called function
        return ls
    else: #only insert coreNumber in index  then return to called function
        ls.insert(memIndex[size],coreNumber)
        return ls 
def getPermu(ls):
    res = list()#list store permutation answer
    for _ in range(math.factorial(len(ls))):
        res.append([*map(int,pm(ls))]) 
    return res
memIndex = dict()#remember index of each level 


print("*** Fun with permute ***")
lst = list(map(int,input("input : ").split(",")))
print(f"Original Cofllection:  {lst}")
ans = getPermu(lst)
print(f"Collection of distinct numbers:\n {ans}")