"""
MATRIX CHAIN MULTIPLICATION
===========================

Classic INTERVAL DP.

We do NOT perform the matrix multiplication.
We choose the parenthesization with minimum scalar multiplications.

If:
    A = p x q
    B = q x r

then multiplying A*B costs:
    p*q*r
"""

def matrix_chain_memo(p):
    """
    p = dimension array.

    A1 = p[0] x p[1]
    A2 = p[1] x p[2]
    ...

    dp(i,j) = minimum cost for Ai...Aj
    """
    n = len(p) - 1
    if n <= 0:
        return 0

    memo = {}

    def dp(i, j):
        if i == j:
            return 0

        state = (i, j)
        if state in memo:
            return memo[state]

        best = float("inf")

        # Try every split:
        # (Ai...Ak) (A(k+1)...Aj)
        for k in range(i, j):
            cost = (
                dp(i, k)
                + dp(k + 1, j)
                + p[i - 1] * p[k] * p[j]
            )
            best = min(best, cost)

        memo[state] = best
        return best

    return dp(1, n)


def matrix_chain_tabulation(p):
    n = len(p) - 1
    if n <= 0:
        return 0

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Solve shorter intervals before longer intervals.
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


def matrix_chain_order(p):
    """Return (minimum_cost, best_parenthesization)."""
    n = len(p) - 1
    if n <= 0:
        return 0, ""

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[None] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    def build(i, j):
        if i == j:
            return f"A{i}"
        k = split[i][j]
        return f"({build(i,k)} x {build(k+1,j)})"

    return dp[1][n], build(1, n)


# INTERVAL DP RECOGNITION:
#   - answer for range [i,j]
#   - partition/split the range
#   - try every k
#   - combine left + right + split cost
#
# Complexity:
#   states = O(n^2)
#   split choices per state = O(n)
#   Time = O(n^3)
#   Space = O(n^2)
#
# Classic related problems:
#   Burst Balloons
#   Palindrome Partitioning variants
#   Optimal BST variants
#
if __name__ == "__main__":
    p = [10, 20, 30, 40]
    print(matrix_chain_memo(p))
    print(matrix_chain_tabulation(p))
    print(matrix_chain_order(p))
