class Stack :
    def __init__(self, lists = None):
        if lists == None:
            self.items = []
        else :
            self.items = lists
        self.size = 0
    def push(self,item):
        self.items.append(item)
        self.size += 1
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]
        return None
    def isEmpty(self):
        return self.items == []
    def get_items(self):
        return self.items

class TreeView:
    def __init__(self,walk):
        self.walk = walk   
        self.Path = Stack()
        self.temp = Stack()
        self.st = Stack()
    def isTaller(self,tree):
        return int(tree[1]) >= self.st.peek()
    def start(self):
        See = 0
        for step in self.walk:
            if step[0] == "A":
                fTree = int(step[1])
                See = self.Path.size+1
                self.temp.push(fTree)
                while not self.Path.isEmpty():
                    if self.Path.peek() <= fTree:
                        See -= 1
                    else :
                        fTree = self.Path.peek()
                    self.temp.push(self.Path.pop())
                while not self.temp.isEmpty():
                    self.Path.push(self.temp.pop())
                # self.Path.push(int(step[1]))
                # while not self.st.isEmpty() and self.isTaller(step):
                #     self.st.pop()
                # self.st.push(int(step[1]))
                # See = self.st.size
            elif step[0] == "B":
                 print(See)
            elif step[0] == "S":
                See = self.Path.size
                for i in range(self.Path.size):
                    if self.Path.get_items()[i] and self.Path.get_items()[i] % 2 == 0 :
                        self.Path.get_items()[i] -= 1
                    elif self.Path.get_items()[i]:
                        self.Path.get_items()[i] += 2
                if not self.Path.isEmpty():
                    fTree = self.Path.pop()
                    self.temp.push(fTree)
                while not self.Path.isEmpty():
                    if self.Path.peek() <= fTree:
                        See -= 1
                    else:
                        fTree = self.Path.peek()
                    self.temp.push(self.Path.pop())
                while not self.temp.isEmpty():
                    self.Path.push(self.temp.pop())
                #print(f"After eat poison see{See} Path{self.Path.get_items()}")
w = input("Enter Input : ").split(",")
walk = list()
for i in w:
    walk.append(tuple(i.split()))
#print(walk)
TreeView(walk).start()