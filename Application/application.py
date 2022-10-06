# Importar pastas a serem usadas
import sys
sys.path.insert(0, '../RandomGraphs')
sys.path.insert(1, '../BridgeIdentification')
sys.path.insert(2, '../BridgeIdentification/EulerianPath')

# Importar classes e metodos de outros arquivos
from random_graph import Graph # Classe
from naive import naive_bridge # Metodo
from tarjan_1974 import tarjan # Metodo
from eulerian_path import eulerianPath # Metodo

# Importando bibliotecas
import time

# libs para testes
from create_adjacencyList import sorting
from create_adjacencyList import listaAdjacencia

'''
Criação do grafo de exemplo para testar os métodos
'''
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
    # graph = createGraphTest()
    # print(naive_bridge(graph.graph, graph.num_vertices))
    graph = Graph(100000)
    graph.eurelianGraph()
    start = time.time()
    print(naive_bridge(graph.graph, graph.num_vertices))
    end = time.time()
    print(f'Time: {end - start}')
    print(f'Tempo de execução = {end - start} segundos.')

if __name__ == "__main__":
    main()