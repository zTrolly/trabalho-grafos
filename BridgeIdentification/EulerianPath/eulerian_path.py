from naive import is_connected

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