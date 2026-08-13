from collections import defaultdict

class Solution(object):
    def numIslands(self, grid):
        graph=defaultdict(list)
        for u in range(len(grid)):
            for v in range(len(grid[u])):
                if(grid[u][v]==1):
                    graph[u].append(v)

        def dfs(graphs,node,visited):
            
            visited.add(node)

            for neigh in graphs[node]:
                if node not in visited:
                    dfs(graphs,neigh)
            count=0
            for n in graphs:
                if n not in visited:
                    count=count+1
                    dfs(graphs,n)
            return count

        x=set()
        return dfs(graph,0,x)

