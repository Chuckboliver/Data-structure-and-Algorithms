import string
class Queue:
    def __init__(self,lists = None):
        if lists == None:
            self.items = []
            self.size = 0
        else:
            self.items = lists
            self.size = len(lists)
    def isEmpty(self):
        return self.size == 0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def front(self):
        if not self.isEmpty():
            return self.items[0]
        return None
    def rear(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    def __len__(self):
        return self.size
    def __str__(self):
        return str(self.items)
def encodemsg(msg,key):
    for i in range(len(msg)):
        if msg.front() in upAlp:
            frontChar = upAlp[(upAlp.find(msg.front())+key.front())%26]
        elif msg.front() in lowAlp:
            frontChar = lowAlp[(lowAlp.find(msg.front())+key.front())%26]
        msg.dequeue()
        msg.enqueue(frontChar)
        key.enqueue(key.dequeue())
    print(f"Encode message is :  {msg}")
def decodemsg(msg,key):
    keySize = len(key)
    msgSize = len(msg)
    for _ in range(keySize - (msgSize%keySize)):
        key.enqueue(key.dequeue())
    for i in range(len(msg)):
        if msg.front() in upAlp:
            frontChar = upAlp[(upAlp.find(msg.front())-key.front())%26]
        elif msg.front() in lowAlp:
            frontChar = lowAlp[(lowAlp.find(msg.front())-key.front())%26]
        msg.dequeue()
        msg.enqueue(frontChar)
        key.enqueue(key.dequeue())
    print(f"Decode message is :  {msg}")
lowAlp = string.ascii_lowercase
upAlp = string.ascii_uppercase
message,origkey = input("Enter String and Code : ").split(",")
msg = Queue(list("".join(message.split())))
key = Queue(list(map(int,origkey)))
encodemsg(msg,key)
decodemsg(msg,key)