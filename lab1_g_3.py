import math
def pm(ls):
    size = len(ls)
    #print(f"On start --> {ls}")
    if size == 2:
        ls[0],ls[1] = ls[1],ls[0]
        return ls
    curmem = memory.setdefault(size,size-1)
    core = ls.pop(curmem)
    #print(f"Debug :: {curmem} {core}")
    memory[size] = (memory[size]+1)%size
    if memory[size] == 0:#get subPattern of low level
        pm(ls)
        ls.insert(memory[size],core)
        return ls
    else:
        ls.insert(memory[size],core)
        return ls
def merge(ls):
    for _ in range(math.factorial(len(ls))):
        res.append([*map(int,pm(ls))])
        
memory = dict()#remember index of each level 
res = list() #list store answer
print("*** Fun with permute ***")
lst = list(map(int,input("input : ").split(",")))
print(f"Original Cofllection:  {lst}")
merge(lst)
print(f"Collection of distinct numbers:\n {res}")