import time

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = list()
    
    def addEdges(self, u, v):
        self.graph.append([u, v])

def bridge_dfs(u, visited, disc, low, parent, graph):
    visited[u] = True
    disc[u] = low[u] = time.time()
    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            bridge_dfs(v, visited, disc, low, parent, graph)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                print("Bridge between", u, "and", v)
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])
 
def find_bridges(graph):
    V = len(graph)
    visited = [False] * V
    disc = [float("Inf")] * V
    low = [float("Inf")] * V
    parent = [-1] * V
    for i in range(V):
        if not visited[i]:
            bridge_dfs(i, visited, disc, low, parent, graph)

def listaAdjacencia(arestas, vertices):
    listaAdjacencia = [[] for i in range(vertices)] # Inicialização do array
    for i in range(len(arestas)):
        listaAdjacencia[arestas[i][0]].append(arestas[i][1])
        listaAdjacencia[arestas[i][1]].append(arestas[i][0])
    return listaAdjacencia

def createGraphTest():
    graph = Graph(9)
    graph.addEdges(0, 1)
    graph.addEdges(0, 3)
    graph.addEdges(0, 4)
    graph.addEdges(1, 2)
    graph.addEdges(1, 3)
    graph.addEdges(1, 4)
    graph.addEdges(2, 3)
    graph.addEdges(2, 4)
    graph.addEdges(2, 5)
    graph.addEdges(3, 5)
    graph.addEdges(4, 5)
    graph.addEdges(5, 6)
    graph.addEdges(6, 7)
    graph.addEdges(6, 8)
    graph.addEdges(7, 8)
    return graph

def main():
    graph = createGraphTest()
    # graph = Graph(1000)
    # graph.semiEurelianGraph()
    # caminho, tempo = FleuryNaive(graph.graph, graph.num_vertices)
    # print(f'Tempo de execução: {tempo} segundos.')
    # print(f'Caminho: {caminho}')
    adjacencia = listaAdjacencia(graph.graph, graph.num_vertices)
    print(adjacencia)
    print(find_bridges(adjacencia))

if __name__ == "__main__":
    main()