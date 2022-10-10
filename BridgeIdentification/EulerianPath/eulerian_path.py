from create_adjacencyList import listaAdjacencia
from naive import naive_bridge
from tarjan_1974 import tarjan

import time

def FleuryNaive(edges, num_vertices):
    start = time.time()
    caminho = list()
    adjacecy_list_graph_ = listaAdjacencia(edges, num_vertices)
    if isValidGraph(adjacecy_list_graph_) == True:
        caminho.append('VAZIO')
        end = time.time()
        return caminho, (end - start)
    pontes = naive_bridge(edges, num_vertices) # Pegar as pontes depois de conferir se o grafo é válido -> Custoso
    initial_vertex = getImparVertex(adjacecy_list_graph_)
    for i in range(len(edges)): # Passar por todas as arestas uma só vez
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

def FleuryTarjan(graph, num_vertices):
    start = time.time()
    caminho = list()
    adjacecy_list_graph_ = listaAdjacencia(graph, num_vertices)
    if isValidGraph(adjacecy_list_graph_) == True:
        caminho.append('VAZIO')
        end = time.time()
        return caminho, (end - start)
    pontes = tarjan(adjacecy_list_graph_) # Única linha alterada para usar o método do tarjan -> mais eficiente.
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
    