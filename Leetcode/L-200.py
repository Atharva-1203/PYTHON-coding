class Solution(object):
    def numIslands(self, grid):

        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(row, col):

            visited[row][col] = True

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:

                r = row + dr
                c = col + dc

                if (0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == "1" and
                    not visited[r][c]):

                    dfs(r, c)

        count = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1" and not visited[i][j]:

                    count += 1
                    dfs(i, j)

        return count
            
            
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        