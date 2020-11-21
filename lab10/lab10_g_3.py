class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    # Code Here
    def __init__(self,size, maxCollision):
        self.size = size
        self.maxCollision = maxCollision
        self.table = [None]*size

    def hashing(self, data):
        nStore = 0
        for item in data:
            collisionNumber = 1
            hashVal = sum(map(ord, item.key)) % self.size
            if nStore == self.size:
                print("This table is full !!!!!!")
                break
            if self.table[hashVal] is None:
                self.table[hashVal] = item
                nStore += 1
                print(self)
            else:
                for j in range(self.size):
                    newHashVal = (hashVal + j * j) % self.size
                    if self.table[newHashVal] is None:
                        self.table[newHashVal] = item
                        nStore += 1
                        print(self)
                        break
                    print(f"collision number {collisionNumber} at {newHashVal}")
                    if collisionNumber == self.maxCollision:
                        print("Max of collisionChain")
                        print(self)
                        break
                    collisionNumber += 1
    def __str__(self):
        output = ""
        for i in range(self.size):
            output += f"#{i + 1}	{self.table[i]}" + "\n"
        output += "---------------------------"
        return output

print(" ***** Fun with hashing *****")
a, b = input("Enter Input : ").split('/')
tSize, maxColl = map(int, a.split())
dataList = list(Data(*k.split()) for k in b.split(',') )

ht = hash(tSize, maxColl)
ht.hashing(dataList)
