from collections import deque
from collections import defaultdict
graphs=defaultdict(list)
edges=[(0,1),(1,2),(2,0),(2,1)]
for (u,v) in edges:
    graphs[u].append(v)
    graphs[v].append(u)

def bfs(gr, node):
    queue=deque()
    x=set()
    x.add(node)
    queue.append(node)
    while queue:
        f=queue.popleft()
        print(f, end=" ")
        for neigh in gr[f]:
            if neigh not in x:
                x.add(neigh)
                queue.append(neigh)
            
print(bfs(graphs,0))