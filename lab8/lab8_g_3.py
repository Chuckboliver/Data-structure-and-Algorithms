
def traverse(tree, index = 0):
    if tree[index] is not None:
        return tree[index]
    
    l = traverse(tree, 2*index+1)
    r = traverse(tree, 2*index+2)
    if l < r:
        tree[index] = tree[2*index+1]
        tree[2*index+2] -= tree[2*index+1]
        tree[2*index+1] = 0
    else:
        tree[index] = tree[2*index+2]
        tree[2*index+1] -= tree[2*index+2]
        tree[2*index+2] = 0
    return tree[index]
    
def sums(tree,index = 0):
    if index > len(tree) -1:
        return 0
    if tree[index] is None:
        return 0
    return tree[index] + sums(tree, 2*index+1) + sums(tree, 2*index+2)


def printTree(tree, level:int = 0, index = 0) -> None:
    if index > len(tree)-1:
        return
    if tree[index] is not None:
        printTree(tree, level + 1,2*index+2)
        print('     '*level, tree[index])
        printTree(tree, level + 1, 2*index+1)

n, l =  input("Enter Input : ").split('/')
l = list(map(int, l.split()))
if len(l) != int(n)//2+1:
    print("Incorrect Input")
else:
    tree = [None]*int(n)
    for i in range(int(n)//2, int(n)):
        tree[i] = l[i - int(n)//2]
    #print(tree)
    #printTree(tree)
    traverse(tree)
    #printTree(tree)
    print(sums(tree))
    #print(tree)
