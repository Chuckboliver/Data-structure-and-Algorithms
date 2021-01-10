class AdjMatrix:
    def __init__(self, size) -> None:
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        self.name = dict()
    def addEdge(self, v1:str, v2:str, wt:int) -> None:
        if 0 <= self.name[v1] < self.size and 0 <= self.name[v2] < self.size:
            self.matrix[self.name[v1]][self.name[v2]] = wt
            self.matrix[self.name[v2]][self.name[v1]] = wt
    def __len__(self) -> int:
        return self.size
    def __str__(self) -> str:
        return "\n".join([str(row_i) for row_i in self.matrix])
def BFS(graph:AdjMatrix, start:str, vertexList):
    matrix = graph.matrix
    graphSize = len(graph)
    visited = [False] * graphSize
    queue = []
    queue.append(start)
    visited[graph.name[start]] = True
    while len(queue) > 0 or False in visited:
        if len(queue) == 0 and False in visited:
            queue.append(vertexList[visited.index(False)])
            visited[visited.index(False)] = True
        for v in range(graphSize):
            if matrix[graph.name[queue[0] ] ][v] >= 1 and not visited[v]:
                queue.append(vertexList[v])
                visited[v] = True
        print(queue.pop(0), end = " ")
    print()
def DFS(graph:AdjMatrix, start:str, vertextList):
    matrix = graph.matrix
    graphSize = len(graph)
    visited = [False] * graphSize
    stack = []
    stack.append(start)
    while len(stack) > 0 or False in visited:
        if len(stack) == 0 and False in visited:
            stack.append(vertexList[visited.index(False)])
        tmp = stack.pop()
        if not visited[graph.name[tmp]]:
            print(tmp, end = " ")
            visited[graph.name[tmp]] = True
        for v in range(graphSize - 1, 0, -1):
            if matrix[graph.name[tmp] ][v] >= 1 and not visited[v]:
                stack.append(vertexList[v])
    print()
inp = input("Enter : ").split(',')
edgeList = [tuple(i.split()) for i in inp]
vertexList = set()
for src, dst in edgeList:
    vertexList.add(src)
    vertexList.add(dst)
vertexList = sorted(list(vertexList))
Matrix = AdjMatrix(len(vertexList))
for i in range(len(vertexList)):
    Matrix.name[vertexList[i]] = i
for src, dst in edgeList:
    Matrix.addEdge(src, dst, 1)
print("Depth First Traversals : ",end="")
DFS(Matrix, vertexList[0], vertexList)
print("Bredth First Traversals : ",end="")
BFS(Matrix, vertexList[0], vertexList)
