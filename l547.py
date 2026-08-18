class Solution(object):
    def findCircleNum(self, isConnected):
        def dfs(adjMat,visited,node):
            visited.add(node)
            for neigh in range(len(adjMat[node])):
                
                if neigh not in visited and adjMat[node][neigh]:
                    visited.add(neigh)
                    dfs(adjMat,visited,neigh)
        count=0
        x=set()
        for i in range(len(isConnected)):
            if i not in x:
                count=count+1
                dfs(isConnected,x,i)
        return count

        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        