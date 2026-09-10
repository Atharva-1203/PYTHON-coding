"""
BFS — BREADTH FIRST SEARCH
==========================

BFS = Breadth First Search.

Mental model:

             0
           /   \
          1     2
         / \     \
        3   4     5

BFS visits LEVEL BY LEVEL:

    Level 0: 0
    Level 1: 1, 2
    Level 2: 3, 4, 5

Therefore:

    BFS -> QUEUE

Python queue:
    from collections import deque

    q.append(x)
    q.popleft()


============================================================
1. BASIC BFS
============================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Return BFS traversal order.

    graph = adjacency list
    start = starting vertex
    """
    visited = set()
    q = deque()

    visited.add(start)
    q.append(start)

    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return order


"""
IMPORTANT:

Mark a node visited WHEN YOU PUT IT INTO THE QUEUE.

Correct:

    if neighbor not in visited:
        visited.add(neighbor)
        q.append(neighbor)

Why?

If you wait until removal from the queue, the same node can be
added multiple times by different parents.


============================================================
2. BFS ON ONE COMPONENT
============================================================

If:

    0 -- 1 -- 2

    3 -- 4

BFS(0) only reaches:
    0, 1, 2

It does NOT reach 3, 4.

A graph can be disconnected.

To traverse EVERYTHING, run BFS from every unvisited node.
"""


def bfs_all_components(graph):
    visited = set()
    order = []

    for start in range(len(graph)):

        if start in visited:
            continue

        q = deque([start])
        visited.add(start)

        while q:
            node = q.popleft()
            order.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

    return order


"""
============================================================
3. BFS LEVEL ORDER
============================================================

Sometimes you need:

    level 0
    level 1
    level 2
    ...

Use:

    level_size = len(q)

Then process exactly level_size nodes.
"""


def bfs_levels(graph, start):
    visited = {start}
    q = deque([start])

    levels = []

    while q:
        level_size = len(q)
        current_level = []

        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        levels.append(current_level)

    return levels


"""
============================================================
4. SHORTEST PATH IN AN UNWEIGHTED GRAPH
============================================================

THIS IS A MAJOR BFS USE CASE.

If every edge has equal cost:

    BFS finds minimum number of edges.

Why?

BFS explores:

    distance 0
    distance 1
    distance 2
    distance 3
    ...

Therefore the first time a node is reached,
its distance is minimal.
"""


def shortest_distances(graph, start):
    n = len(graph)

    distance = [-1] * n
    distance[start] = 0

    q = deque([start])

    while q:
        node = q.popleft()

        for neighbor in graph[node]:

            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)

    return distance


"""
Example:

    0 -- 1 -- 3
    |
    2

shortest_distances(graph, 0)

    0 -> 0
    1 -> 1
    2 -> 1
    3 -> 2


============================================================
5. SHORTEST PATH — ACTUAL PATH
============================================================

Distance tells us HOW FAR.

Parent tells us HOW WE GOT THERE.

Store:

    parent[neighbor] = node

Then start from target and walk backward.
"""


def shortest_path(graph, start, target):
    n = len(graph)

    parent = [-1] * n
    visited = [False] * n

    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()

        if node == target:
            break

        for neighbor in graph[node]:

            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                q.append(neighbor)

    if not visited[target]:
        return []

    path = []
    curr = target

    while curr != -1:
        path.append(curr)
        curr = parent[curr]

    path.reverse()

    return path


"""
============================================================
6. COUNT CONNECTED COMPONENTS
============================================================

Pattern:

    answer = 0

    for every node:
        if unvisited:
            answer += 1
            BFS(node)

Each BFS discovers exactly one new component.
"""


def count_components(graph):
    visited = set()
    count = 0

    for start in range(len(graph)):

        if start in visited:
            continue

        count += 1

        q = deque([start])
        visited.add(start)

        while q:
            node = q.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

    return count


"""
============================================================
7. BIPARTITE GRAPH — BFS COLORING
============================================================

Use two colors:

    0
    1

Every edge must connect DIFFERENT colors.

If:

    color[node] == color[neighbor]

then graph is not bipartite.

For disconnected graphs, start BFS at every uncolored node.
"""


def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n

    for start in range(n):

        if color[start] != -1:
            continue

        color[start] = 0
        q = deque([start])

        while q:
            node = q.popleft()

            for neighbor in graph[node]:

                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    q.append(neighbor)

                elif color[neighbor] == color[node]:
                    return False

    return True


"""
============================================================
8. BFS ON A GRID
============================================================

A grid is a graph.

Node:
    (row, col)

Neighbors:
    up
    down
    left
    right

Template:

    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

Queue stores:
    (row, col)
"""


def grid_bfs(grid, start_row, start_col):
    """
    0 = open
    1 = blocked
    """
    if not grid:
        return []

    rows = len(grid)
    cols = len(grid[0])

    if grid[start_row][start_col] == 1:
        return []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    visited = {(start_row, start_col)}
    q = deque([(start_row, start_col)])

    order = []

    while q:
        r, c = q.popleft()
        order.append((r, c))

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == 0
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                q.append((nr, nc))

    return order


"""
============================================================
9. MULTI-SOURCE BFS
============================================================

VERY IMPORTANT.

Normal BFS:

    ONE source -> spreads outward.

Multi-source BFS:

    MANY sources -> all spread simultaneously.

Example:
    all initially rotten oranges are sources.

Put ALL sources into the queue before starting BFS.

Their distance starts at 0.
"""


def multi_source_bfs(graph, sources):
    n = len(graph)

    distance = [-1] * n
    q = deque()

    for source in sources:
        if distance[source] == -1:
            distance[source] = 0
            q.append(source)

    while q:
        node = q.popleft()

        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)

    return distance


"""
============================================================
10. BFS COMPLEXITY
============================================================

Adjacency list:

    Time  = O(V + E)
    Space = O(V)

Grid:

    Time  = O(R * C)
    Space = O(R * C)

because each node/cell is processed at most once.


============================================================
11. WHEN SHOULD BFS COME TO MIND?
============================================================

Look for words such as:

    shortest
    minimum steps
    minimum moves
    nearest
    level
    distance
    number of edges
    spread
    simultaneously
    closest

Especially:

    "shortest path in an UNWEIGHTED graph"

-> BFS is usually the first algorithm to consider.


============================================================
12. BFS MASTER TEMPLATE
============================================================

    from collections import deque

    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


============================================================
13. COMMON BFS MISTAKES
============================================================

[ ] Using a list with pop(0) instead of deque.popleft()
[ ] Forgetting visited
[ ] Marking visited too late
[ ] Forgetting disconnected components
[ ] Treating a directed graph as undirected
[ ] Forgetting grid boundaries
[ ] Forgetting that BFS shortest path assumes equal edge cost
"""


if __name__ == "__main__":
    graph = [
        [1, 2],
        [0, 3],
        [0, 3],
        [1, 2]
    ]

    print("BFS:", bfs(graph, 0))
    print("Levels:", bfs_levels(graph, 0))
    print("Distances:", shortest_distances(graph, 0))
    print("Path:", shortest_path(graph, 0, 3))
    print("Components:", count_components(graph))
    print("Bipartite:", is_bipartite(graph))
