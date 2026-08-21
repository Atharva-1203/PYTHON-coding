from collections import defaultdict
graphs=defaultdict(list)
edges=[(0,1),(0,2),(1,3),(1,4),(2,5)]
for u,v in edges:
    graphs[u].append(v)
    graphs[v].append(u)
print(graphs)

def dfs_cc(graph, node, x):
    x.add(node)
    print(x, end=" ")
    for neigh in graph[node]:
        if neigh not in x:
            x.add(node)
            
            dfs_cc(graph,neigh,x)

d=set()
print(dfs_cc(graphs,0,d))
