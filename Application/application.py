# Importar pastas a serem usadas
import sys
sys.path.insert(0, '../RandomGraphs')
sys.path.insert(1, '../BridgeIdentification')
sys.path.insert(2, '../BridgeIdentification/EulerianPath')
sys.setrecursionlimit(10000000)

# Importar classes e metodos de outros arquivos
from random_graph import Graph # Classe
from eulerian_path import FleuryNaive # Metodo
from eulerian_path import FleuryTarjan # Metodo

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
    graph = Graph(100)

    graph.eurelianGraph()
    print('TARJAN - Euleriano')
    caminho, tempo = FleuryTarjan(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

    print('NAIVE - Euleriano')
    caminho, tempo = FleuryNaive(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

    print("===========================================================")

    graph.semiEurelianGraph()
    print('TARJAN - Semi-Euleriano')
    caminho, tempo = FleuryTarjan(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

    print('NAIVE - Semi-Euleriano')
    caminho, tempo = FleuryNaive(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

    print("===========================================================")

    graph.notEurelianGraph()
    print('TARJAN - Não Euleriano')
    caminho, tempo = FleuryTarjan(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

    print('NAIVE - Não Euleriano')
    caminho, tempo = FleuryNaive(graph.graph, graph.num_vertices)
    print(f'Tempo de execução: {tempo} segundos.')
    print(f'Caminho: {caminho}')

if __name__ == "__main__":
    main()