def sorting(graph):
    relacao_ordenada = sorted(graph, key=lambda item: item[0])
    return relacao_ordenada

def listaAdjacencia(array):
    resultado = []
    for i in range(0, len(array)): 
        if (array[i][0] not in resultado):
            resultado.append(array[i][0])
        if (array[i][1] not in resultado):
            resultado.append(array[i][1])
    for i in range(0, len(resultado)):
        aux = []
        for j in range(0, len(array)):
            if (resultado[i] in array[j]):
                aux.append(array[j][1] if (resultado[i] == array[j][0]) else array[j][0]) 
        resultado[i] = aux
    return resultado