def mx(l):
    #base case
    if len(l) <= 1 :
        return l[0]
    #recursive call
    k = mx(l[1:])
    return k if k >l[0] else l[0]

l = list(map(int , input("Enter Input : ").split()))
print(f"Max : {mx(l)}")