from itertools import groupby
class Queue:
    class Node:
        def __init__(self,data = None,n=0,next = None):
            self.data = data
            self.n = n
            self.next = None
        def __str__(self):
            return str(self.data)
    def __init__(self):
        self.head = self.Node(None,None)
        self.tail = self.head
        self.size = 0
        q = self.head.next
        while q != None:
            self.size += 1
            q = q.next
            self.tail =q     
    def __str__(self):
        s=""
        t =self.head.next
        while t != None:
            s+="<"+str(t.data)+", "+str(t.n)+">"
            t=t.next
        return s
    def __len__(self):
        return self.size
    def enqueue(self,data,n):
        p = self.Node(data,n)
        self.tail.next = p
        self.tail = p
        self.size += 1
    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.head.next
        if temp == self.tail:
            self.tail=self.head
        self.head.next = temp.next
        self.size -= 1
        return temp
    def isEmpty(self):
        return self.size == 0
    def front(self):
        return self.head.next
    def rear(self):
        return self.tail
A,B = input("Enter Input (Red, Blue) : ").split()
RedTeamBomb = Queue()
BlueTeamBomb = Queue()
for ch,item in groupby(A):
    n = len(list(item))
    RedTeamBomb.enqueue(ch,n)
for ch,item in groupby(B[::-1]):
    n = len(list(item))
    BlueTeamBomb.enqueue(ch,n)

redExplode = 0
blueFreeze = 0
RedAns = ""
BlueAns = ""
bombList = []
Mistake = 0
while not BlueTeamBomb.isEmpty():
    f = BlueTeamBomb.front()
    if f.n // 3 >=1:
        BlueTeamBomb.front().n -=3
        bombList.append(f.data)
        if BlueTeamBomb.front().n == 0:
            BlueTeamBomb.dequeue()
    else:
        BlueAns += f.data * f.n
        BlueTeamBomb.dequeue()
print(bombList)
blueFreeze = len(bombList)
while not RedTeamBomb.isEmpty():
    f = RedTeamBomb.front()
    if f.n // 3 >= 1 : #Found Bomb 
        #RedTeamBomb.front().n -= 3
        #print(f"Current red : {RedTeamBomb}")
        if len(bombList)>0:
            nextBlueBomb = bombList.pop(0)
        else:
            nextBlueBomb = None
        #print(f"Next bBomb is : {nextBlueBomb}")
        if nextBlueBomb is None:
            RedTeamBomb.front().n -= 3
            redExplode += 1
        elif f.data == nextBlueBomb:
            #print("MISTAKE")
            Mistake += 1
            RedTeamBomb.front().n -= 2
            print(f"Mistake : {RedTeamBomb}")
            #RedAns += nextBlueBomb
        else:
            RedAns += f.data*2+nextBlueBomb+f.data
            RedTeamBomb.front().n -= 3
        if RedTeamBomb.front().n == 0:
            RedTeamBomb.dequeue()
    else : #Not found
        RedAns += RedTeamBomb.front().data * RedTeamBomb.front().n
        RedTeamBomb.dequeue()

nR = len(RedAns)
nB = len(BlueAns)
if RedAns == "":
    RedAns = "ytpmE"
if BlueAns == "":
    BlueAns = "Empty"
print(f"Red Team :\n{nR}\n{RedAns[::-1]}\n{redExplode} Explosive(s) ! ! ! (HEAT)")
if Mistake > 0:
    print(f"Blue Team Made (a) Mistake(s) {Mistake} Bomb(s)")
print(f"----------TENETTENET----------\n: maeT eulB\n{nB}\n{BlueAns[::-1]}\n(EZEERF) ! ! ! (s)evisolpxE {blueFreeze}")