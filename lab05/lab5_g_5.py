from collections import deque
import math
class Queue:
    def __init__(self,l = None):
        if l is None:
            self._items = deque()
            self._size = 0
        elif isinstance(l,SLL):
            temp = l._head

        else:
            self._items = deque(l)
            self._size = len(l)
    def isEmpty(self):
        return self._size == 0
    def enqueue(self,data):
        self._items.append(data)
        self._size += 1
    def dequeue(self):
        if not self.isEmpty():
            self._size -= 1
            return self._items.popleft()
        return None
    def __len__(self):
        return self._size
    def front(self):
        return self._items[0]
    def rear(self):
        return self._items[-1]
    def item(self):
        return list(self._items)
    def __str__(self):
        return " ".join(list(map(str,self.item())))

class SLL:
    class Node:
        def __init__(self,data=None):
            self._data = data
            self._next = None
        def __str__(self):
            return str(self._data)
    def __init__(self):
        dummyNode = self.Node(None)
        self._head = dummyNode
        self._size = 0
    def __str__(self):
        s = ""
        t = self._head._next
        while t is not None:
            s += str(t._data)+" "
            t = t._next
        return s
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def append(self,data):
        newNode = self.Node(data)
        t = self._head
        while t._next is not None and newNode._data >= t._next._data:
            t = t._next
        
        newNode._next = t._next
        t._next = newNode
        self._size += 1
    def pop(self):
        if not self.isEmpty():
            self._size -= 1
            temp = self._head._next
            self._head._next = temp._next
            return temp._data
        return None
    def find_max(self):
        mx = -math.inf
        temp = self._head._next
        while temp is not None:
            mx = max(mx,temp._data)
            temp = temp._next
        return mx

def get_digit(n,d):
    n = abs(n)
    for i in range(d-1):
        n //= 10
    return n % 10
    
def get_max_bits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i
    
def radix_sort(l):
    q = Queue(l)
    max_bits = get_max_bits(max(l))
    qq  = [SLL() for _ in range(10)]
        
    for i in range(1,max_bits+2):
        print(f"Round : {i}")
        while not q.isEmpty():
                #print(self)
            num = q.dequeue()
            num_digit = get_digit(num,i)
            qq[num_digit].append(num)
        bCase = len(qq[0])  
        for j in range(10):
            print(f"{j} : ",end= "")
            while not qq[j].isEmpty():
                p = qq[j].pop()
                print(p,end = " ")
                q.enqueue(p)
            print()
        print("------------------------------------------------------------")
        if bCase == len(q):
            print(i-1,"Time(s)")
            return q
    print(max_bits,"Time(s)")
    return q
l =list(map(int, input("Enter Input : ").split() ) ) 
 
print("------------------------------------------------------------")
Bfradix = " -> ".join(list(map(str,l)))
w = radix_sort(l)
print(f"Before Radix Sort : {Bfradix}")
print(f"After  Radix Sort : {' -> '.join([str(i) for i in w.item()])}")
