class Solution(object):
    def numEnclaves(self, grid):

        m = len(grid)
        n = len(grid[0])

        vis = [[False] * n for _ in range(m)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row, col):

            vis[row][col] = True

            for u, v in directions:

                r = row + u
                c = col + v

                if (0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == 1 and
                    not vis[r][c]):

                    dfs(r, c)

        for i in range(m):

            if grid[i][0] == 1 and not vis[i][0]:
                dfs(i, 0)

            if grid[i][n-1] == 1 and not vis[i][n-1]:
                dfs(i, n-1)

        for j in range(n):

            if grid[0][j] == 1 and not vis[0][j]:
                dfs(0, j)

            if grid[m-1][j] == 1 and not vis[m-1][j]:
                dfs(m-1, j)

        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1 and not vis[i][j]:
                    count += 1

        return count

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        