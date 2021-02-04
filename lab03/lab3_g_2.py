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


def Greater(plate):
    return True if plate[0] >st.peek()[0] else False

w = input("Enter Input : ").split(",") 
plates = []
st = Stack()
for i in w:
    plates.append(tuple(map(int, i.split())))
for plate in plates:
    while not st.isEmpty() and Greater(plate):
        brPlate = st.pop()
        print(brPlate[1])
    st.push(plate)
