from collections import defaultdict
graph=defaultdict(list)

edges=[(1,2),(1,0),(2,0),(0,2)]
for u,v in edges:
    graph[u].append(v)
    

print(graph)