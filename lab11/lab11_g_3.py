import sys
class AdjMatrix:
    def __init__(self, size) -> None:
        self.matrix = []
        self.name = dict()
        for i in range(size):
            self.matrix.append([0 for _ in range(size)])
        self.size = size
    def addEdge(self, v1:str, v2:str, wt:int):
        if 0 <= self.name[v1] < self.size and 0 <= self.name[v2] < self.size:
            self.matrix[self.name[v1]][self.name[v2]] = wt
            self.matrix[self.name[v2]][self.name[v1]] = wt
    def __len__(self):
        return self.size
    def __str__(self) -> str:
        return "\n".join([str(row_i) for row_i in self.matrix])
    def getEdge(self, src:str, dst:str):
        return self.matrix[self.name[src]][self.name[dst]]
def dijkstra(graph:AdjMatrix, src:str, dst:str, vertexList):
    def minDistance(dist, sptSet):
        mini = sys.maxsize
        minIndex = None
        for v in range(len(graph)):
            if dist[v] < mini and sptSet[v] == False:
                mini = dist[v]
                minIndex = v
        return minIndex
    if src not in vertexList or dst not in vertexList:
        print(f"Not have path : {src} to {dst}")
        return
    path = vertexList.copy()
    matrix = graph.matrix
    graphSize = len(graph)
    dist = [sys.maxsize] * graphSize
    dist[graph.name[src]] = 0
    sptSet = [False] * graphSize
    for _ in range(graphSize):
        u = minDistance(dist, sptSet)
        if u is None:
            break
        sptSet[u] = True
        for v in range(graphSize):
            if matrix[u][v] > 0 and \
                sptSet[v] == False and \
                dist[v] > dist[u] + matrix[u][v]:
                dist[v] = dist[u] + matrix[u][v]
                path[v] = vertexList[u]
    print(dist)
    if dist[graph.name[dst]] == sys.maxsize:
        print(f"Not have path : {src} to {dst}")
    else:
        shortestPath = []
        ptr = dst
        while ptr != src:
            shortestPath.append(ptr)
            ptr = path[graph.name[ptr]]
        shortestPath.append(ptr)
        print(f"{src} to {dst} : {'->'.join(shortestPath[::-1])}")
vertexList = []
nodeInp, cmdInp = input("Enter : ").split('/')
node = []
for s in nodeInp.split(','):
    src, weight, dst  = s.split()
    weight = int(weight)
    if src not in vertexList:
        vertexList.append(src)
    if dst not in vertexList:
        vertexList.append(dst)
    node.append((src, weight, dst))
Matrix = AdjMatrix(len(vertexList))
for vertex in vertexList:
    Matrix.name[vertex] = len(Matrix.name)
for src, weight, dst in node:
    Matrix.addEdge(src, dst, weight)
cmd = [tuple(s.split()) for s in cmdInp.split(',')]
for src, dst in cmd:
    dijkstra(Matrix, src, dst, vertexList)