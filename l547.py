from collections import defaultdict

class Solution(object):
    def findCircleNum(self, isConnected):
        graphs=defaultdict(list)
        for u in range(len(isConnected)):
            for v in range(len(isConnected)):
                if (isConnected[u][v]==1):
                    graphs[u].append(v)
        def dfs(node,x):
            x.add(node)
            for neigh in graphs[node]:
                if neigh not in x:
                    dfs(neigh,x)

        visited=set()
        count=0
        for u in range(len(isConnected)):
            if u not in visited:
                count=count+1
                dfs(u,visited)
        return count