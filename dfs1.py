from collections import defaultdict
graphs=defaultdict(list)
edges=[(1,0), (2,0),(1,2),(0,2)]
for u,v in edges:
    graphs[u].append(v)
print(graphs)

def dfs(gr, node, check):
    check.add(node)
    print(node, end=" ")
    for neigh in gr[node]:
        if neigh not in check:
            check.add(node)
            dfs(gr, neigh, check)
x=set()
print(dfs(graphs, 0, x))

