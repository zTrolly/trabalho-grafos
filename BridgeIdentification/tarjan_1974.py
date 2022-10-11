# https://www2.eecs.berkeley.edu/Pubs/TechRpts/1974/ERL-m-427.pdf
# https://memgraph.com/docs/mage/algorithms/traditional-graph-analytics/bridges-algorithm

def tarjan(G):
    if len(G) == 0:
        return []
    if len(G) == 1:
        return []
    bridges = []
    n = len(G)
    visited = [False] * n
    low = [float('inf')] * n
    disc = [float('inf')] * n
    parent = [-1] * n
    def dfs(u, disc, low, parent, visited, bridges):
        visited[u] = True
        disc[u] = low[u] = next(time)
        for v in G[u]:
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

'''
0. Receive an adjacency list in the format [[],[]]
1. Find a spanning forest of G
2. Create a rooted forest F from the spanning forest
3. Traverse the forest F in preorder and number the nodes. Parent nodes in the forest now have lower numbers than child nodes.
4. For each node v in preorder (denoting each node using its preorder number), do:
    4.1. Compute the number of forest descendants ND(v) for this node, by adding one to the sum of its children's descendants.
    4.2. Compute L(v), the lowest preorder label reachable fromv by a path for which all but the last edge stays within the subtree rooted at v. This is the minimum of the set consisting of the preorder label of v, of the values ofL(w) at child nodes of v and of the preorder labels of nodes reachable from v by edges that do not belong to F.
    4.3. Similarly, compute H(v), the highest preorder label reachable by a path for which all but the last edge stays within the subtree rooted at v. This is the maximum of the set consisting of the preorder label of v, of the values of H(w) at child nodes of v and of the preorder labels of nodes reachable from v by edges that do not belong to F.
    4.4. For each nodew with parent node v, if L(w) = w and H(w) < w + ND(w) then the edge from v to w is a bridge.
5. Return a list of bridges
'''