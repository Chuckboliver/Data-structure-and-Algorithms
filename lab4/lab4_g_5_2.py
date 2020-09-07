class Stack :
    def __init__(self, lists = None):
        if lists == None:
            self.items = []
        else :
            self.items = lists
            self.size = len(lists)
        self.size = 0
    def push(self,item):
        self.items.append(item)
        self.size += 1
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        return "Empty"
    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]
        return None
    def isEmpty(self):
        return self.size == 0
    def __len__(self):
        return self.size
    def get_items(self):
        return self.items
    def __str__(self):
        return "".join(self.items[::-1]) if not self.isEmpty() else "Empty"
class Queue:
    def __init__(self, lists = None):
        if lists is not None:
            self.items = lists
            self.size = len(lists)
        else:
            self.items = []
            self.size = 0
    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        self.items.append(item)
        self.size += 1
    def dequeue(self):
        if not self.isEmpty():
            self.size -= 1
            return self.items.pop(0)
        return "Empty"
    def front(self):
        return self.items[0]
    def rear(self):
        return self.items[-1]
    def __len__(self):
        return self.size
    def __str__(self):
        return f"{self.items}"


A,B = input("Enter Input (Red, Blue) : ").split()
waitForCollision = Stack()
FreezeBomb = Stack()
RescueBomb = Stack()
RedTeam,BlueTeam = Queue(list(A)),Queue(list(B))
while not BlueTeam.isEmpty():
    FreezeBomb.push(BlueTeam.dequeue())
    if len(FreezeBomb) > 2:
        items = FreezeBomb.get_items()
        if items[-1] == items[-2] == items[-3]:
            RescueBomb.push(FreezeBomb.peek())
            for _ in range(3):
                FreezeBomb.pop()
nRes = len(RescueBomb)
redExplode = 0
Mistake = 0
while not RedTeam.isEmpty():
    waitForCollision.push(RedTeam.dequeue())
    if len(waitForCollision) > 2:
        items = waitForCollision.get_items()
        if items[-1] == items[-2] == items[-3]:
            fBomb = RescueBomb.pop()
            if fBomb == "Empty":
                redExplode += 1
                for _ in range(3):
                    waitForCollision.pop()
            elif fBomb == waitForCollision.peek():
                Mistake += 1
                for _ in range(2):
                    waitForCollision.pop()
            else :
                temp = waitForCollision.pop()
                waitForCollision.push(fBomb)
                waitForCollision.push(temp)

print("Red Team :")
print(f"{len(waitForCollision)}")
print(waitForCollision)
print(f"{redExplode} Explosive(s) ! ! ! (HEAT)")
if Mistake > 0:
    print(f"Blue Team Made (a) Mistake(s) {Mistake} Bomb(s)")
print("----------TENETTENET----------")
print(": maeT eulB")
print(len(FreezeBomb))
print(FreezeBomb.__str__()[::-1])
print(f"(EZEERF) ! ! ! (s)evisolpxE {nRes}")