class node:
    def __init__(self,data,next = None ):
        ### Code Here ##
        self.data = data
        self.next = None
    def __str__(self):
        ### Code Here ###
        return str(self.data)
def createList(l=[]):
    ### Code Here ###
    head = node(int(l.pop(0)))
    temp = head
    for n in l:
        temp.next = node(int(n))
        temp = temp.next
    return head
def printList(H):
    ### Code Here ###
    temp = H
    while temp is not None:
        print(temp.data,end=" ")
        temp = temp.next
    print()
def mergeOrderesList(p,q):
    ### Code Here ###
    dummy = node(None)
    temp = dummy
    while p is not None and q is not None:
        #print(f"Compare {p.data} {q.data}",end = " ")
        if p.data <= q.data:
            #print(f"Choose {p.data}")
            temp.next = p
            p = p.next
        else:
            #print(f"Choose {q.data}")
            temp.next = q
            q = q.next
        temp = temp.next
    if p is not None:
        temp.next = p
    else:
        temp.next = q
    return dummy.next
L1,L2 = input("Enter 2 Lists : ").split()
L1 = L1.split(",")
L2 = L2.split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print(f'LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)