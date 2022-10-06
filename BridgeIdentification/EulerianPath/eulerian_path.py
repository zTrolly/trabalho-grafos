from naive import is_connected

'''
Para entender como funciona o algoritmo de Fleury, considere o grafo da figura 4a da ligaçao.
Suponhamos que o algoritmo começa com o vértice 6. Ele pode escolher uma das arestas h, d, e ou i.
Supondo que ele escolhe d, ele se encontra depois no vértice 2, onde ele é obrigado a seguir pela ponte que liga com o vértice 5.
Isso é ilustrado na figura 4b. Nesse momento, ele pode escolher entre b, g o h. O último é descartado por ser uma ponte.
Então sobram somente b e g. Supondo que b é selecionado, ele chega ao vértice 1, como ilustrado na figura 4c.
Nas três próximas etapas, ele não tem escolha. Chegando ao vértice 6, de novo ele tem mais du uma opção.
Em mais três etapas, ele volta à origem, o que completa o circuito euleriano.
'''
# https://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
def eulerianPath(graph, bridges):
    C = [] #circuit
    V = [] #vertices
    E = [] #edges
    for vert in graph:
        if len(vert) > 1:
            V.append(vert[0])
            for edge in vert[1:]:
                E.append(edge)
    v0 = V[0]
    C.append(v0)
    while len(E) > 0:
        vi = C[-1]
        if len(graph[vi]) == 1:
            ai = graph[vi][0]
        else:
            for edge in graph[vi][1:]:
                if edge not in bridges:
                    ai = edge
        E.remove(ai)
        C.append(ai)
        vj = graph[vi][graph[vi].index(ai)]
        C.append(vj)
    return C

def grau(vertice):
    return len(vertice)