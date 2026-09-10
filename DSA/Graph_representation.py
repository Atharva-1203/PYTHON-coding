"""
GRAPH REPRESENTATION — COMPLETE STUDY GUIDE
============================================

Goal:
    Understand graphs from scratch and learn the representations you will
    repeatedly use in LeetCode and exams.

A graph has:
    V = vertices / nodes
    E = edges / connections

Example:

        0
       / \
      1---2
       \
        3

Vertices = 0, 1, 2, 3
Edges    = (0,1), (0,2), (1,2), (1,3)

Think:
    Linked List -> chain
    Tree        -> hierarchy
    Graph       -> arbitrary network


============================================================
1. GRAPH TERMINOLOGY
============================================================

VERTEX / NODE
    An object in the graph.

EDGE
    Connection between two vertices.

DEGREE
    Number of edges connected to a vertex in an undirected graph.

IN-DEGREE
    Number of incoming edges in a directed graph.

OUT-DEGREE
    Number of outgoing edges in a directed graph.

PATH
    A sequence of vertices connected by edges.

CYCLE
    A path that eventually returns to a previously visited vertex.

CONNECTED GRAPH
    Every vertex can be reached from every other vertex
    (for an undirected graph).

CONNECTED COMPONENT
    One connected "island" inside a possibly disconnected graph.

DAG
    Directed Acyclic Graph.
    A directed graph with no cycles.


============================================================
2. UNDIRECTED GRAPH
============================================================

Edge:

    0 -- 1

means:

    0 -> 1
    1 -> 0

Therefore, in an adjacency list we store the edge twice.


============================================================
3. DIRECTED GRAPH
============================================================

Edge:

    0 -> 1

means only:

    0 can go to 1

It does NOT imply:

    1 can go to 0


============================================================
4. WEIGHTED GRAPH
============================================================

An edge can contain a cost:

    0 --5-- 1

Meaning:

    edge 0 -> 1 has weight 5.

Common examples:
    distance
    price
    time
    network cost


============================================================
5. ADJACENCY MATRIX
============================================================

For n vertices, create an n x n matrix.

Example:

    0 -- 1
    |    |
    2 -- 3

Matrix:

        0 1 2 3
      ----------
    0 | 0 1 1 0
    1 | 1 0 0 1
    2 | 1 0 0 1
    3 | 0 1 1 0

matrix[u][v] tells us whether an edge exists.

Complexity:
    Space: O(V^2)
    Check whether edge exists: O(1)

Good when:
    - graph is dense
    - you need frequent edge-existence checks


============================================================
6. BUILD AN UNWEIGHTED ADJACENCY MATRIX
============================================================
"""


def build_adjacency_matrix(n, edges, directed=False):
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        matrix[u][v] = 1

        if not directed:
            matrix[v][u] = 1

    return matrix


"""
IMPORTANT:
    If graph is UNDIRECTED, update BOTH:
        matrix[u][v]
        matrix[v][u]

For DIRECTED:
    only:
        matrix[u][v]


============================================================
7. WEIGHTED ADJACENCY MATRIX
============================================================
"""


def build_weighted_matrix(n, edges, directed=False):
    """
    edges:
        [(u, v, weight), ...]

    None means there is no edge.
    """
    matrix = [[None] * n for _ in range(n)]

    for u, v, weight in edges:
        matrix[u][v] = weight

        if not directed:
            matrix[v][u] = weight

    return matrix


"""
============================================================
8. ADJACENCY LIST — MOST IMPORTANT FOR LEETCODE
============================================================

Example:

    0 -- 1
    |    |
    2    3

Adjacency list:

    0 -> [1, 2]
    1 -> [0, 3]
    2 -> [0]
    3 -> [1]

In Python, the standard representation is:

    graph = [[] for _ in range(n)]

Then:

    graph[u].append(v)

For an undirected graph also:

    graph[v].append(u)

Complexity:
    Space: O(V + E)

This is usually the default representation for BFS and DFS.
"""


def build_adjacency_list(n, edges, directed=False):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)

        if not directed:
            graph[v].append(u)

    return graph


"""
============================================================
9. WEIGHTED ADJACENCY LIST
============================================================

Store:

    graph[u] = [(neighbor, weight), ...]

Example:

    0 --5-- 1
    0 --2-- 2

becomes:

    graph[0] = [(1, 5), (2, 2)]

This is heavily used by:
    Dijkstra
    Prim
    weighted graph problems
"""


def build_weighted_adjacency_list(n, edges, directed=False):
    graph = [[] for _ in range(n)]

    for u, v, weight in edges:
        graph[u].append((v, weight))

        if not directed:
            graph[v].append((u, weight))

    return graph


"""
============================================================
10. EDGE LIST
============================================================

Sometimes the input itself is easiest to keep as:

    edges = [
        (0, 1),
        (0, 2),
        (1, 3)
    ]

Weighted:

    (u, v, weight)

Useful for:
    - Kruskal
    - sorting edges
    - problems that process edges directly
"""


def sort_edges_by_weight(edges):
    return sorted(edges, key=lambda edge: edge[2])


"""
============================================================
11. DICTIONARY ADJACENCY LIST
============================================================

When nodes are strings rather than 0...n-1:

    A -- B
    A -- C
    B -- D

A dictionary is convenient:

    {
        "A": ["B", "C"],
        "B": ["A", "D"]
    }
"""


def build_dictionary_graph(edges, directed=False):
    from collections import defaultdict

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

        if not directed:
            graph[v].append(u)

    return graph


"""
============================================================
12. GRID = GRAPH
============================================================

A grid is secretly a graph.

Example:

    1 1 0
    1 0 0
    0 0 1

Each cell is a node.

Usually each cell connects to:

    UP
    DOWN
    LEFT
    RIGHT

Directions:

    (-1, 0)
    ( 1, 0)
    ( 0,-1)
    ( 0, 1)

This idea powers:
    Number of Islands
    Flood Fill
    Rotting Oranges
    Shortest Path in Binary Matrix
    Walls and Gates
"""


def get_grid_neighbors(r, c, rows, cols):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    result = []

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            result.append((nr, nc))

    return result


"""
============================================================
13. WHICH REPRESENTATION SHOULD I USE?
============================================================

ADJACENCY MATRIX
    Space: O(V^2)
    Edge check: O(1)
    Neighbor iteration: O(V)

ADJACENCY LIST
    Space: O(V + E)
    Edge check: O(degree(u))
    Neighbor iteration: O(degree(u))

EDGE LIST
    Space: O(E)
    Great when working directly with edges.

DEFAULT LEETCODE RULE:

If you receive:

    n
    edges

and the graph is unweighted, usually start with:

    graph = [[] for _ in range(n)]

Then for each edge [u, v]:

    graph[u].append(v)

and if UNDIRECTED:

    graph[v].append(u)


============================================================
14. COMMON BUG
============================================================

Problem says:

    "There are n nodes and an undirected edge [u, v]."

Wrong:

    graph[u].append(v)

Correct:

    graph[u].append(v)
    graph[v].append(u)

Forgetting the second line changes the problem into a directed graph.


============================================================
15. QUICK COMPLEXITY CHEAT SHEET
============================================================

Representation        Space          Edge lookup
------------------------------------------------
Matrix                 O(V^2)        O(1)
Adjacency List         O(V+E)        O(degree)
Edge List              O(E)          O(E)

For most sparse LeetCode graphs:
    adjacency list is the natural choice.


============================================================
16. PRACTICE
============================================================
"""

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3)]

    print("Adjacency List:")
    print(build_adjacency_list(4, edges))

    print("\nDirected:")
    print(build_adjacency_list(4, edges, directed=True))

    print("\nMatrix:")
    for row in build_adjacency_matrix(4, edges):
        print(row)

    weighted = [(0, 1, 5), (0, 2, 2), (1, 3, 7)]

    print("\nWeighted Adjacency List:")
    print(build_weighted_adjacency_list(4, weighted))

    print("\nEdges sorted by weight:")
    print(sort_edges_by_weight(weighted))
