"""
DFS — DEPTH FIRST SEARCH
========================

DFS = Depth First Search.

Mental model:

             0
           /   \
          1     2
         / \
        3   4

DFS goes as DEEP as possible before backtracking.

One possible order:

    0 -> 1 -> 3 -> 4 -> 2

The exact order depends on neighbor order.

Therefore:

    DFS -> STACK / RECURSION


============================================================
1. RECURSIVE DFS
============================================================
"""


def dfs_recursive(graph, start):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)

    return order


"""
WHY VISITED?

Graph:

    0 -- 1
    |    |
    2 -- 3

There are cycles.

Without visited, DFS could do:

    0 -> 1 -> 3 -> 2 -> 0 -> 1 -> ...

and never stop.

So:

    visited = set()

is fundamental in graph DFS.


============================================================
2. CLASSIC EXAM-STYLE DFS
============================================================

Sometimes the question expects DFS as a separate function.
"""


def dfs(node, graph, visited, order):
    visited.add(node)
    order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, order)


def run_dfs(graph, start):
    visited = set()
    order = []

    dfs(start, graph, visited, order)

    return order


"""
============================================================
3. ITERATIVE DFS
============================================================

Recursive DFS uses the call stack.

Iterative DFS uses your own stack:

    stack = []

    stack.append(...)
    stack.pop()

STACK = LIFO

Last In -> First Out
"""


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return order


"""
BFS:
    queue
    popleft()

DFS:
    stack
    pop()


============================================================
4. DFS OVER ALL COMPONENTS
============================================================

One DFS only explores one connected component.

To visit the entire graph:

    for every node:
        if unvisited:
            DFS(node)
"""


def dfs_all_components(graph):
    visited = set()
    order = []

    for start in range(len(graph)):

        if start in visited:
            continue

        stack = [start]

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)
            order.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


"""
============================================================
5. COUNT CONNECTED COMPONENTS
============================================================

Each DFS started from an unvisited node discovers
one connected component.
"""


def count_components_dfs(graph):
    visited = set()
    count = 0

    def explore(start):
        stack = [start]

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    for node in range(len(graph)):
        if node not in visited:
            count += 1
            explore(node)

    return count


"""
============================================================
6. DFS ON GRID — NUMBER OF ISLANDS
============================================================

A grid is a graph.

Each cell is a node.
Neighboring cells are connected.

Example:

    1 1 0
    1 0 0
    0 0 1

Each connected group of 1s = one island.

Algorithm:

    for every cell:
        if land:
            answer += 1
            DFS from this cell
            mark every connected land cell visited
"""


def number_of_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def dfs_grid(r, c):

        # Outside grid.
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        # Water or already visited.
        if grid[r][c] != '1':
            return

        # Mark visited.
        grid[r][c] = '0'

        # Explore four directions.
        for dr, dc in directions:
            dfs_grid(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == '1':
                count += 1
                dfs_grid(r, c)

    return count


"""
Instead of a visited set, we modified:

    '1' -> '0'

This is a common LeetCode trick.

If modifying the input is not allowed, use:

    visited = set()


============================================================
7. PATH EXISTS?
============================================================
"""


def path_exists(graph, start, target):
    visited = set()

    def dfs(node):

        if node == target:
            return True

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(start)


"""
============================================================
8. CYCLE DETECTION — UNDIRECTED GRAPH
============================================================

IMPORTANT:

In an undirected graph, seeing a visited neighbor does NOT
automatically mean a cycle.

Example:

    0 -- 1

When at node 1, we see node 0 is visited.

But 0 is simply our PARENT.

Therefore we track:

    parent

Rule:

    if neighbor is visited AND neighbor != parent:
        cycle exists
"""


def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                if dfs(neighbor, node):
                    return True

            elif neighbor != parent:
                return True

        return False

    for node in range(len(graph)):

        if node not in visited:

            if dfs(node, -1):
                return True

    return False


"""
============================================================
9. CYCLE DETECTION — DIRECTED GRAPH
============================================================

Directed graphs require a different technique.

Use 3 states:

    0 = unvisited
    1 = currently being explored
    2 = completely finished

If we encounter a node with state 1:

    BACK EDGE -> CYCLE

This pattern is extremely useful for dependency problems.


Example:

    0 -> 1 -> 2
         ^    |
         |____|

There is a directed cycle.
"""


def has_cycle_directed(graph):
    n = len(graph)
    state = [0] * n

    def dfs(node):
        state[node] = 1

        for neighbor in graph[node]:

            if state[neighbor] == 1:
                return True

            if state[neighbor] == 0:
                if dfs(neighbor):
                    return True

        state[node] = 2
        return False

    for node in range(n):

        if state[node] == 0:

            if dfs(node):
                return True

    return False


"""
============================================================
10. TOPOLOGICAL SORT — DFS
============================================================

Topological sorting works on a DAG:

    Directed Acyclic Graph

Example:

    A -> B
    A -> C
    B -> D
    C -> D

A valid answer:

    A, C, B, D

DFS idea:

    Explore children FIRST.
    Add node AFTER exploring children.

This is POSTORDER.

Then reverse the result.
"""


def topological_sort_dfs(graph):
    n = len(graph)

    state = [0] * n
    order = []

    def dfs(node):
        state[node] = 1

        for neighbor in graph[node]:

            if state[neighbor] == 1:
                # Cycle -> impossible.
                return False

            if state[neighbor] == 0:

                if not dfs(neighbor):
                    return False

        state[node] = 2

        # Add AFTER exploring neighbors.
        order.append(node)

        return True

    for node in range(n):

        if state[node] == 0:

            if not dfs(node):
                return []

    order.reverse()

    return order


"""
============================================================
11. DFS + BACKTRACKING CONNECTION
============================================================

DFS is also the basic idea behind many backtracking problems.

Think:

    choose
      |
      v
    explore
      |
      v
    undo choice
      |
      v
    choose next

Graph DFS:

    visit node
        |
        v
    visit neighbor
        |
        v
    go deeper
        |
        v
    backtrack

This connection becomes important for:
    permutations
    combinations
    subsets
    maze/path problems
    word search


============================================================
12. RECURSION MENTAL MODEL
============================================================

For:

    0 -> 1 -> 2

Calling:

    dfs(0)

means:

    dfs(0)
        dfs(1)
            dfs(2)
                return
            return
        return

The deepest call finishes first.

That is why recursion naturally behaves like a stack.


============================================================
13. DFS COMPLEXITY
============================================================

Adjacency list:

    Time  = O(V + E)
    Space = O(V)

Space includes:
    visited
    recursion stack / explicit stack

Grid:

    Time  = O(R * C)
    Space = O(R * C)

Potential Python issue:

Very deep recursive DFS can exceed Python's recursion limit.

For very deep graphs, iterative DFS can be safer.


============================================================
14. DFS VS BFS
============================================================

DFS:
    stack / recursion
    deep exploration

Good for:
    connected components
    cycle detection
    topological sorting
    exploring regions
    backtracking-style problems

BFS:
    queue
    level-by-level exploration

Good for:
    shortest path in unweighted graphs
    minimum steps
    nearest node
    level problems
    spreading / multi-source problems


============================================================
15. MASTER DFS TEMPLATE
============================================================

    visited = set()

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)


============================================================
16. GRID DFS TEMPLATE
============================================================

    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    def dfs(r, c):

        if outside_grid:
            return

        if invalid:
            return

        mark_visited()

        for dr, dc in directions:
            dfs(r + dr, c + dc)


============================================================
17. GRAPH PROBLEM CHECKLIST
============================================================

Before coding, ask:

    1. What are the nodes?
    2. What are the edges?
    3. Directed or undirected?
    4. Weighted or unweighted?
    5. Connected or potentially disconnected?
    6. Do I need visited?
    7. Is it a grid disguised as a graph?
    8. Am I looking for shortest path?
    9. Am I detecting a cycle?
    10. Do I need parent/state/color?


============================================================
18. COMMON DFS MISTAKES
============================================================

[ ] Forgetting visited
[ ] Forgetting disconnected components
[ ] Confusing directed and undirected cycle logic
[ ] Forgetting grid boundaries
[ ] Marking grid cells incorrectly
[ ] Forgetting parent in undirected cycle detection
[ ] Using simple visited[] for directed cycle detection
[ ] Hitting recursion depth on huge graphs
"""


if __name__ == "__main__":
    graph = [
        [1, 2],
        [0, 3],
        [0, 3],
        [1, 2]
    ]

    print("Recursive DFS:", dfs_recursive(graph, 0))
    print("Iterative DFS:", dfs_iterative(graph, 0))
    print("Components:", count_components_dfs(graph))
    print("Path 0 -> 3:", path_exists(graph, 0, 3))
    print("Undirected cycle:", has_cycle_undirected(graph))

    directed = [
        [1],
        [2],
        []
    ]

    print("Directed cycle:", has_cycle_directed(directed))
    print("Topological order:", topological_sort_dfs(directed))

    grid = [
        ['1', '1', '0'],
        ['1', '0', '0'],
        ['0', '0', '1']
    ]

    print("Islands:", number_of_islands(grid))
