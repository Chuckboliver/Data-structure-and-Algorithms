from collections import defaultdict
class AdjList:
    def __init__(self, size:int) -> None:
        self.graph = defaultdict(list)
        self.size = size
    def addEdge(self, u:int, v:int):
        self.graph[u].append(v)
    def isCycleUtil(self, curNode, visited, recStack):
        visited[curNode] = True
        recStack[curNode] = True
        for neighbor in self.graph[curNode]:
            if visited[neighbor] == False:
                if self.isCycleUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True
        recStack[curNode] = False
        return False
    def isCycle(self):
        visited = [False] * self.size
        recStack = [False] * self.size
        for node in range(self.size):
            if visited[node] == False:
                if self.isCycleUtil(node, visited, recStack) == True:
                    return True
        return False

inp = input("Enter : ").split(',')
edgeList = [tuple(i.split()) for i in inp]
vertexTable = dict()#Map vertex name to vertex number
for src, dst in edgeList:
    vertexTable.setdefault(src, len(vertexTable))
    vertexTable.setdefault(dst, len(vertexTable))
graph = AdjList(len(vertexTable))
for src, dst in edgeList:
    graph.addEdge(vertexTable[src], vertexTable[dst])
#print(graph.graph)
if graph.isCycle():
    print("Graph has a cycle")
else:
    print("Graph has no cycle")