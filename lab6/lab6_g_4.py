def display(A,B,C,i ):
    if i < 0:
        return
    poleA = list(*filter(lambda x:x[0] == 'A',(A,B,C)))[1]
    poleB = list(*filter(lambda x:x[0] == 'B',(A,B,C)))[1]
    poleC = list(*filter(lambda x:x[0] == 'C',(A,B,C)))[1]
    print(poleA[i] if i < len(poleA) else "|",end="  ")
    print(poleB[i] if i < len(poleB) else "|",end="  ")
    print(poleC[i] if i < len(poleC) else "|")
    display(A,B,C,i-1)
def toh(n,fp,tp,axp,maxn): 
    if n == 1:
        tp[1].append(fp[1].pop())
        print(f"move 1 from  {fp[0]} to {tp[0]}")
        display(fp,tp,axp,maxn)
        return
    toh(n-1,fp,axp,tp,maxn)
    tp[1].append(fp[1].pop())
    print(f"move {n} from  {fp[0]} to {tp[0]}")
    display(fp,tp,axp,maxn)
    toh(n-1,axp,tp,fp,maxn)

n = int(input("Enter Input : "))
fp,tp,axp = ('A',list(reversed(range(1,n+1)))),('C',list()),('B',list())
display(fp,tp,axp,n)
toh(n,fp,tp,axp,n)