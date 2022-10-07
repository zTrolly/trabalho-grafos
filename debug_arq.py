import random

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

    def printGraph(self):
        for i in range(0, len(self.graph)):
            print(self.graph[i])

def sorting(graph):
    relacao_ordenada = sorted(graph, key=lambda item: item[0])
    return relacao_ordenada

def listaAdjacencia(arestas, vertices):
    listaAdjacencia = [[] for i in range(vertices)] # Inicialização do array
    for i in range(len(arestas)):
        listaAdjacencia[arestas[i][0]].append(arestas[i][1])
        listaAdjacencia[arestas[i][1]].append(arestas[i][0])
    return listaAdjacencia

def naive_bridge(grafo, num_vertices):
    pontes = list()
    for i in range(len(grafo)):
        grafo_aux = grafo.copy()
        grafo_aux.remove(grafo_aux[i])
        lista_adj = listaAdjacencia(grafo_aux, num_vertices)
        if is_connected(lista_adj) == False:
            pontes.append(grafo[i])
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


def FleuryNaive(graph, num_vertices):
    caminho = list()
    adjacecy_list = listaAdjacencia(graph, num_vertices)
    if isValidGraph(adjacecy_list) == True:
        print('Não tem caminho euleriano')
        return caminho
    graph_ = graph.copy()
    initial_vertex = getImparVertex(adjacecy_list)
    for i in range(len(graph_)):
        if degreeVertex(adjacecy_list, initial_vertex) > 1:
            # Selecionar aresta {v, w} que nao seja ponte em graph_
            caminho.append(graph_[i])
            vertex_caminhado = 1 # selecionar vertice caminhado
        else:
            # Selecionar única aresta {v, w} em graph_
            caminho.append(graph_[i])
            vertex_caminhado = 1 # selecionar vertice caminhado
        initial_vertex = vertex_caminhado
        print(graph_[i])
        graph_.remove(graph_[i])
    return caminho

def FleuryTarjan(graph):
    adjacecy_list = listaAdjacencia(graph)

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
    #print(naive_bridge(graph.graph, graph.num_vertices))
    #graph = Graph(100)
    #graph.eurelianGraph()
    FleuryNaive(graph.graph, graph.num_vertices)

if __name__ == "__main__":
    main()