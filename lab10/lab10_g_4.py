import math 
class Hash:
    def __init__(self, maxSize, maxCollision, threshold):
        self.maxSize = maxSize
        self.maxCollision = maxCollision
        self.table = [None]*maxSize
        self.threshold = threshold
        self.collectedData = []

    def hashing(self, data):
        count = 0
        if data not in self.collectedData:
            self.collectedData.append(data)
            print(f"Add : {data}")

        while count <= self.maxSize:
            index = (data + count * count) % self.maxSize
            if self.table[index] is None:
                self.table[index] = data
                if (self.maxSize - self.table.count(None)) / self.maxSize * 100 > self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehashing()
                return
            count += 1
            print(f"collision number {count} at {index}")
            if count == self.maxCollision:
                print("****** Max collision - Rehash !!! ******")
                self.rehashing()
                return
    def rehashing(self):
        minTmp = self.maxSize * 2
        rehashSize = nextPrime(minTmp)
        self.table = [None] * rehashSize
        self.maxSize = rehashSize
        for data in self.collectedData:
            self.hashing(data)
    def __str__(self):
        output = ""
        for i in range(self.maxSize):
            output += f"#{i + 1}	{self.table[i]}" + "\n"
        output += "----------------------------------------"
        return output

def isPrime(n):  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
    if(n % 2 == 0 or n % 3 == 0): 
        return False
        
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
    return True
   
def nextPrime(N):  
    if (N <= 1): 
        return 2
    prime = N 
    found = False
    while(not found): 
        prime = prime + 1
    
        if(isPrime(prime) == True): 
            found = True
    return prime

print(" ***** Rehashing *****")
a, b = input("Enter Input : ").split('/')
tSize, maxColl, threshold = map(int, a.split())
dataList = list(map(int, b.split()))

ht = Hash(tSize, maxColl, threshold)
print("Initial Table :")
print(ht)
for data in dataList:
    ht.hashing(data)
    print(ht)
