# https://codeforces.com/blog/entry/71146

def tarjan(graph):
    if len(graph) == 0:
        return []
    if len(graph) == 1:
        return []
    bridges = []
    n = len(graph)
    visited = [False] * n
    low = [float('inf')] * n
    disc = [float('inf')] * n
    parent = [-1] * n
    def dfs(u, disc, low, parent, visited, bridges):
        visited[u] = True
        disc[u] = low[u] = next(time)
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v, disc, low, parent, visited, bridges)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append([u, v])
                    bridges.append([v, u])
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    time = iter(range(n))
    for u in range(n):
        if not visited[u]:
            dfs(u, disc, low, parent, visited, bridges)
    return bridges