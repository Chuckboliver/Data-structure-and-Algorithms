def TowerOfHanoi(n,fr,to,aux):
    global c
    if n == 1:
        print(f"{c} Move disk 1 from rod {fr} to {to}")
        c+=1
        return
    TowerOfHanoi(n-1,fr,aux,to)
    print(f"{c} Move disk {n} from rod {fr} to {to}")
    c+=1
    TowerOfHanoi(n-1,aux,to,fr)
c=1
TowerOfHanoi(10,'A','C','B')