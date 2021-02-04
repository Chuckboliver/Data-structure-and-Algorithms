def isSortedAscending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
def isSortedDescending(lst):
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
def haveDuplicate(lst):
    hSet = set()
    for n in lst:
        if n in hSet:
            return True
        hSet.add(n)
    return False

l = list(map(int, list(input("Enter Input : "))))
if len(set(l)) == 1:
    print("Repdrome")
elif isSortedAscending(l):
    if haveDuplicate(l):
        print("Plaindrome")
    else:
        print("Metadrome")
elif isSortedDescending(l) :
    if haveDuplicate(l):
        print("Nialpdrome")
    else:
        print("Katadrome")
else:
    print("Nondrome")