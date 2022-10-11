from copy import deepcopy
import time
import random
import sys

sys.setrecursionlimit(10000000)

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = list()
    
    def addEdges(self, u, v):
        self.graph.append([u, v])
    
    def eurelianGraph(self):
        for i in range(0, (self.num_vertices - 1)):
            self.addEdges(i, i + 1)
        self.addEdges((self.num_vertices - 1), 0)
    
    def semiEurelianGraph(self):
        self.eurelianGraph()
        randomEdgeU = random.randint(0, (self.num_vertices - 1))
        randomEdgeV = random.randint(0, (self.num_vertices - 1))
        while randomEdgeU == randomEdgeV:
            randomEdgeU = random.randint(0, (self.num_vertices - 1))
            randomEdgeV = random.randint(0, (self.num_vertices - 1))
        self.addEdges(randomEdgeU, randomEdgeV)
    
    def notEurelianGraph(self):
        for vertex in range(0, self.num_vertices):
            randomDegree = random.randint(1, 2)
            for _ in range(0, randomDegree):
                randomEdgeV = random.randint(0, (self.num_vertices - 1))
                while vertex == randomEdgeV:
                    randomEdgeV = random.randint(0, (self.num_vertices - 1))
                if [vertex, randomEdgeV] not in self.graph:
                    self.addEdges(vertex, randomEdgeV)

def listaAdjacencia(arestas, vertices):
    listaAdjacencia = [[] for i in range(vertices)] # Inicialização do array
    for i in range(len(arestas)):
        listaAdjacencia[arestas[i][0]].append(arestas[i][1])
        listaAdjacencia[arestas[i][1]].append(arestas[i][0])
    return listaAdjacencia

def sorting(graph):
    relacao_ordenada = sorted(graph, key=lambda item: item[0])
    return relacao_ordenada

def sorting2(graph):
    relacao_ordenada = sorted(graph, key=lambda item: item[1])
    return relacao_ordenada






















def naive_bridge(grafo):
    pontes = list()
    for i in range(len(grafo)):
        for j in range(len(grafo[i])):
            grafo_aux = deepcopy(grafo)
            del(grafo_aux[i][j])
            if is_connected(grafo_aux) == False:
                pontes.append([i, grafo[i][j]])
                pontes.append([grafo[i][j], i])
    return pontes


def is_connected(graph):
    visited = set()
    queue = []
    start = 0
    queue.append(start)
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return len(visited) == len(graph)

def FleuryNaive(edges, num_vertices):
    start = time.time()
    caminho = list()
    adjacecy_list_graph_ = listaAdjacencia(edges, num_vertices)
    #print(adjacecy_list_graph_)
    if isValidGraph(adjacecy_list_graph_) == True:
        caminho.append('VAZIO')
        end = time.time()
        return caminho, (end - start)
    initial_vertex = getImparVertex(adjacecy_list_graph_)
    caminho.append(initial_vertex)
    for _ in range(len(edges)): # Passar por todas as arestas uma só vez
        pontes = naive_bridge(adjacecy_list_graph_) # Pegar as pontes depois de conferir se o grafo é válido -> Custoso
        #print(pontes)
        if degreeVertex(adjacecy_list_graph_, initial_vertex) > 1:
            edge, vertex_caminhado = selectEdge(initial_vertex, adjacecy_list_graph_, pontes)
            caminho.append(vertex_caminhado)
        else:
            edge = [initial_vertex, adjacecy_list_graph_[initial_vertex][0]]
            caminho.append(edge[1])
            vertex_caminhado = adjacecy_list_graph_[initial_vertex][0]
        initial_vertex = vertex_caminhado
        adjacecy_list_graph_[edge[0]].remove(vertex_caminhado)
        adjacecy_list_graph_[edge[1]].remove(edge[0])
    end = time.time()
    return caminho, (end - start)




def tarjan(graph):
    visited = [False] * len(graph)
    disc = [-1] * len(graph)
    low = [-1] * len(graph)
    parent = [-1] * len(graph)
    def bridge(v, visited, disc, low, parent, graph):
        visited[v] = True
        disc[v] = low[v] = time.time()
        for w in graph[v]:
            if not visited[w]:
                parent[w] = v
                bridge(w, visited, disc, low, parent, graph)
                low = min(low[w], low[v])
            elif w != parent[v]:
                low[v] = min[low[v], disc[w]]
    bridge(0, visited, disc, low, parent, graph)
    return bridges

def FleuryTarjan(graph, num_vertices):
    start = time.time()
    caminho = list()
    adjacecy_list_graph_ = listaAdjacencia(graph, num_vertices)
    #print(adjacecy_list_graph_)
    if isValidGraph(adjacecy_list_graph_) == True:
        caminho.append('VAZIO')
        end = time.time()
        return caminho, (end - start)
    initial_vertex = getImparVertex(adjacecy_list_graph_)
    caminho.append(initial_vertex)
    for i in range(len(adjacecy_list_graph_)): # Passar por todas as arestas uma só vez
        pontes = tarjan(adjacecy_list_graph_, initial_vertex) # Única linha alterada para usar o método do tarjan -> mais eficiente.
        #print(pontes)
        if degreeVertex(adjacecy_list_graph_, initial_vertex) > 1:
            edge, vertex_caminhado = selectEdge(initial_vertex, adjacecy_list_graph_, pontes)
            caminho.append(vertex_caminhado)
        else:
            edge = [initial_vertex, adjacecy_list_graph_[initial_vertex][0]]
            caminho.append(edge[1])
            vertex_caminhado = adjacecy_list_graph_[initial_vertex][0]
        initial_vertex = vertex_caminhado
        adjacecy_list_graph_[edge[0]].remove(vertex_caminhado)
        adjacecy_list_graph_[edge[1]].remove(edge[0])
    end = time.time()
    return caminho, (end - start)

def selectEdge(vertex, adjacency_list, pontes):
    for i in range(len(adjacency_list[vertex])):
        edge = [vertex, adjacency_list[vertex][i]] # Conferir nos dois caminhos
        edge_ = [adjacency_list[vertex][i], vertex]
        if edge not in pontes and edge_ not in pontes:
            return [vertex, adjacency_list[vertex][i]], adjacency_list[vertex][i]
        return [vertex, adjacency_list[vertex][i + 1]], adjacency_list[vertex][i + 1]
    
def degreeVertex(adjacency_list, vertex):
    return len(adjacency_list[vertex])

def getImparVertex(graph):
    for i in range(len(graph)):
        if len(graph[i]) % 2 != 0:
            return i # Pegar vértice ímpar caso tenha
    return 0 # Pegar vértice inicial caso não tenha ímpar

def isValidGraph(graph):
    count = 0
    for i in range(len(graph)):
        if len(graph[i]) % 2 != 0:
            count += 1
        if count > 2: return True
    return False


















def createGraphTest2():
    graph = Graph(7)
    graph.addEdges(0, 1)
    graph.addEdges(0, 2)
    graph.addEdges(1, 2)
    graph.addEdges(1, 3)
    graph.addEdges(1, 4)
    graph.addEdges(2, 3)
    graph.addEdges(2, 5)
    graph.addEdges(3, 4)
    graph.addEdges(3, 5)
    graph.addEdges(4, 5)
    graph.addEdges(4, 6)
    graph.addEdges(5, 6)
    return graph


def main():
    graph = Graph(20)
    graph.semiEurelianGraph()
    '''
    print('TARJAN')
    caminho, tempo = FleuryTarjan(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

    print('NAIVE')
    caminho, tempo = FleuryNaive(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')
    '''
    print('TARJAN')
    lista = listaAdjacencia(graph.graph, graph.num_vertices)
    caminho = tarjan(lista, 0)
    print(f'Caminho: {caminho}')

    print('NAIVE')
    lista = listaAdjacencia(graph.graph, graph.num_vertices)
    caminho = naive_bridge(lista)
    print(f'Caminho: {caminho}')
    

if __name__ == "__main__":
    main()