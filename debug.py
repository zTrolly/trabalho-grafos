import time
import random
import sys

sys.setrecursionlimit(10000)

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = list()
    
    def addEdges(self, u, v):
        self.graph.append([u, v])

    def semiEurelianGraph(self):
        self.eurelianGraph()
        randomEdgeU = random.randint(0, (self.num_vertices - 1))
        randomEdgeV = random.randint(0, (self.num_vertices - 1))
        while randomEdgeU == randomEdgeV:
            randomEdgeU = random.randint(0, (self.num_vertices - 1))
            randomEdgeV = random.randint(0, (self.num_vertices - 1))
        self.addEdges(randomEdgeU, randomEdgeV)
    
    def eurelianGraph(self):
        for i in range(0, (self.num_vertices - 1)):
            self.addEdges(i, i + 1)
        self.addEdges((self.num_vertices - 1), 0)

def bridges(G):
    if len(G) == 0:
        return []
    if len(G) == 1:
        return []
    bridges = []
    n = len(G)
    visited = [False] * n
    low = [float('inf')] * n
    disc = [float('inf')] * n
    parent = [-1] * n
    def dfs(u, disc, low, parent, visited, bridges):
        visited[u] = True
        disc[u] = low[u] = next(time)
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v, disc, low, parent, visited, bridges)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append([u, v])
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    time = iter(range(n))
    for u in range(n):
        if not visited[u]:
            dfs(u, disc, low, parent, visited, bridges)
    return bridges

def FleuryTarjan(graph, num_vertices):
    start = time.time()
    caminho = list()
    adjacecy_list_graph_ = listaAdjacencia(graph, num_vertices)
    if isValidGraph(adjacecy_list_graph_) == True:
        caminho.append('VAZIO')
        end = time.time()
        return caminho, (end - start)
    pontes = bridges(adjacecy_list_graph_) # Única linha alterada para usar o método do tarjan -> mais eficiente.
    initial_vertex = getImparVertex(adjacecy_list_graph_)
    for i in range(len(graph)): # Passar por todas as arestas uma só vez
        if degreeVertex(adjacecy_list_graph_, initial_vertex) > 1:
            edge, vertex_caminhado = selectEdge(initial_vertex, adjacecy_list_graph_, pontes)
            caminho.append(edge)
        else:
            edge = [initial_vertex, adjacecy_list_graph_[initial_vertex][0]]
            caminho.append(edge)
            vertex_caminhado = adjacecy_list_graph_[initial_vertex][0]
        initial_vertex = vertex_caminhado
        adjacecy_list_graph_[edge[0]].remove(vertex_caminhado)
        adjacecy_list_graph_[edge[1]].remove(edge[0])
    end = time.time()
    return caminho, (end - start)

def selectEdge(vertex, adjacency_list, pontes):
    for i in range(len(adjacency_list[vertex])):
        edge = [vertex, adjacency_list[vertex][i]]
        if edge not in pontes:
            return [vertex, adjacency_list[vertex][i]], adjacency_list[vertex][i]
    
'''
Pegar grau do vértice atual, escolhido
'''
def degreeVertex(adjacency_list, vertex):
    return len(adjacency_list[vertex])

'''
Pegar o vértice inicial para o algoritmo de fleury, tentaod prevalecer o vértice ímpar
'''
def getImparVertex(graph):
    for i in range(len(graph)):
        if len(graph[i]) % 2 != 0:
            return i # Pegar vértice ímpar caso tenha
    return 0 # Pegar vértice inicial caso não tenha ímpar

'''
Olhar quantos vértices de grau ímpar tem no grafo, para ver se é válido
'''
def isValidGraph(graph):
    count = 0
    for i in range(len(graph)):
        if len(graph[i]) % 2 != 0:
            count += 1
        if count > 2: return True
    return False

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
    graph = Graph(1000)
    graph.semiEurelianGraph()
    caminho, tempo = FleuryTarjan(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

if __name__ == "__main__":
    main()