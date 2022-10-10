# https://www2.eecs.berkeley.edu/Pubs/TechRpts/1974/ERL-m-427.pdf
# https://memgraph.com/docs/mage/algorithms/traditional-graph-analytics/bridges-algorithm

def tarjan(graph, num_vertices):
    print('TARJAN')



'''
0. Receba uma lista de adjacências no formato [[],[]] -> OK
1. Encontre uma floresta abrangente de G
2. Crie uma floresta enraizada F a partir da floresta abrangente
3. Percorra a floresta F em pré-ordem e numere os nós. Os nós pais na floresta agora têm números menores do que os nós filhos.
4. Para cada nó v em pré-ordem (indicando cada nó usando seu número de pré-ordem), faça:
    4.1. Calcule o número de descendentes de floresta ND(v) para este nó, adicionando um à soma dos descendentes de seus filhos.
    4.2. Calcule L(v), o rótulo de pré-ordem mais baixo alcançável de v por um caminho para o qual todas, exceto a última aresta, permanecem dentro da subárvore enraizada em v. Este é o mínimo do conjunto que consiste no rótulo de pré-ordem de v, dos valores de L(w) em nós filhos de v e dos rótulos de pré-ordem de nós alcançáveis ​​de v por arestas que não pertencem a F.
    4.3. Da mesma forma, calcule H(v), o rótulo de pré-ordem mais alto alcançável por um caminho para o qual todas, exceto a última aresta, permanecem dentro da subárvore com raiz em v. Este é o máximo do conjunto consistindo no rótulo de pré-ordem de v, dos valores de H(w) em nós filhos de v e dos rótulos de pré-ordem de nós alcançáveis ​​de v por arestas que não pertencem a F.
    4.4. Para cada nó com nó pai v, se L(w) = w e H(w) < w + ND(w) então a aresta de v a w é uma ponte.
5. Voltar à lista de pontes

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