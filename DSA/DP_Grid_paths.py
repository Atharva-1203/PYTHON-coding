"""
GRID DP
=======
Classic state:
    dp[r][c] = answer for cell (r,c)

If moves are down/right:
    dp[r][c] depends on top and left.

Counting:  top + left
Minimum:   cost + min(top, left)
Maximum:   value + max(top, left)
"""

def unique_paths_memo(m, n):
    """Top-down memoization."""
    memo = {}

    def dp(r, c):
        if r >= m or c >= n:
            return 0
        if r == m - 1 and c == n - 1:
            return 1

        state = (r, c)
        if state in memo:
            return memo[state]

        memo[state] = dp(r + 1, c) + dp(r, c + 1)
        return memo[state]

    return dp(0, 0)


def unique_paths_tabulation(m, n):
    dp = [[0] * n for _ in range(m)]

    for r in range(m):
        dp[r][0] = 1
    for c in range(n):
        dp[0][c] = 1

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[-1][-1]


def unique_paths_optimized(m, n):
    """O(n) space instead of O(m*n)."""
    dp = [1] * n

    for r in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c - 1]

    return dp[-1]


def unique_paths_with_obstacles(grid):
    """
    0 = open, 1 = blocked.
    A blocked cell contributes zero paths.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    if grid[0][0] == 1:
        return 0

    dp[0][0] = 1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dp[r][c] = 0
                continue
            if r == 0 and c == 0:
                continue

            top = dp[r - 1][c] if r > 0 else 0
            left = dp[r][c - 1] if c > 0 else 0
            dp[r][c] = top + left

    return dp[-1][-1]


def min_path_sum(grid):
    """Minimum sum when moving only right/down."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    for c in range(1, cols):
        dp[0][c] = dp[0][c - 1] + grid[0][c]
    for r in range(1, rows):
        dp[r][0] = dp[r - 1][0] + grid[r][0]

    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

    return dp[-1][-1]


# Complexity for an m x n grid:
# Time  = O(m*n)
# 2D space = O(m*n)
# 1D optimized space = O(n)
#
# Derivation checklist:
#   1. What does dp[r][c] mean?
#   2. Which cells can reach it?
#   3. Are we counting, minimizing, or maximizing?
#   4. What are boundaries/obstacles?
#
if __name__ == "__main__":
    print(unique_paths_memo(3, 3))
    print(unique_paths_tabulation(3, 3))
    print(unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))
