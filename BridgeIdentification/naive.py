from create_adjacencyList import sorting
from create_adjacencyList import listaAdjacencia

def naive_bridge(grafo):
    pontes = list()
    for i in range(len(grafo)):
        grafo_aux = grafo.copy()
        grafo_aux.remove(grafo_aux[i])
        grafo_aux_ordenado = sorting(grafo_aux)
        lista_adj = listaAdjacencia(grafo_aux_ordenado)
        if is_connected(lista_adj) == False:
            pontes.append(grafo[i])
    return pontes

def is_connected(graph):
  visited = []
  for i in range(1, len(graph)):
    if i not in visited:
      visited.append(i)
      for j in graph[i]:
        if j not in visited:
          visited.append(j)
  return len(visited) == len(graph)