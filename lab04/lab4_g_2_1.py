class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
ENqueue = Queue()
ESqueue = Queue()
select = {"EN":ENqueue.enqueue, "ES":ESqueue.enqueue}
w = input("Enter Input : ").split(",")
for i in w:
    c,*otaID = i.split()
    if c in select.keys():
        select[c](*otaID)
    else:
        if not ESqueue.isEmpty():
            print(ESqueue.dequeue() )
        elif not ENqueue.isEmpty():
            print(ENqueue.dequeue() )
        else:
            print("Empty")