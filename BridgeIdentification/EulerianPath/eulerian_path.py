from create_adjacencyList import listaAdjacencia
import time

def FleuryNaive(graph, num_vertices):
    start = time.time()
    caminho = list()
    adjacecy_list = listaAdjacencia(graph, num_vertices)
    if isValidGraph(adjacecy_list) == True:
        print('Não tem caminho euleriano')
        caminho.append('VAZIO')
        end = time.time()
        return caminho, (end - start)
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
        graph_.remove(graph_[i])
    end = time.time()
    return caminho, (end - start)

def FleuryTarjan(graph):
    adjacecy_list = listaAdjacencia(graph)

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
    