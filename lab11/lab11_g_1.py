class AdjList:
    def __init__(self):
        self.n = 0
        self.graph = dict()

    def add_vertex(self, v):
        if v not in self.graph:
            self.n += 1
            self.graph[v] = []

    def add_edge(self, v1, v2, e):
        if v1 in self.graph and v2 in self.graph:
            node =  (v2, e)
            self.graph[v1].append(node)
    def printGraph(self):
        for v in sorted(self.graph.keys()):
            print(v, end = " ")
        for vertex, edge in self.graph.items():
            print(f"{vertex} : ",end="")
            print(*edge, sep = ", ")

class AdjMatrix:
    def __init__(self) -> None:
        self.n = 0
        self.vertices = []
        self.graph = []

    def add_vertex(self, v):
        if v not in self.vertices:
            self.n += 1
            self.vertices.append(v)
            if self.n > 1:
                for vertex in self.graph:
                    vertex.append(0)
            temp = []
            for i in range(self.n):
                temp.append(0)
            self.graph.append(temp)

    def add_edge(self, v1, v2, e):
        if v1 in self.vertices and v2 in self.vertices:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.graph[index1][index2] = e

    def printGraph(self):

        print("    " + "  ".join(self.vertices))
        for i in range(self.n):
            print(f"{self.vertices[i]} : ",end="")
            print( *self.graph[i], sep= ", ")

def bb(lst):
    n = len(lst)
    while True:
        swapped = False
        for i in range(1, n):
            if lst[i - 1] > lst[i]:
                lst[i - 1],lst[i] =  lst[i],lst[i -1]
                swapped = True
        if not swapped:
            break
    return lst

inp = input("Enter : ").split(',')
k = [(i[0], i[2]) for i in inp]
maps = AdjMatrix()
for src, dst in k:
    if src not in maps.vertices:
        maps.add_vertex(src)
    if dst not in maps.vertices:
        maps.add_vertex(dst)
    #maps.add_edge(src, dst, 1)
bb(maps.vertices)
for src,dst in k:
    maps.add_edge(src, dst, 1)
maps.printGraph()

    
