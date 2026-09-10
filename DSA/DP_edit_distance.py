"""
EDIT DISTANCE / LEVENSHTEIN DISTANCE
====================================

Convert A into B with minimum:
    insert
    delete
    replace

State:
    dp(i,j) = minimum operations to convert A[:i] -> B[:j]

Base:
    dp(0,j) = j       # insert j characters
    dp(i,0) = i       # delete i characters
"""

def edit_distance_memo(a, b):
    memo = {}

    def dp(i, j):
        if i == 0:
            return j
        if j == 0:
            return i

        state = (i, j)
        if state in memo:
            return memo[state]

        if a[i - 1] == b[j - 1]:
            memo[state] = dp(i - 1, j - 1)
        else:
            insert = dp(i, j - 1)
            delete = dp(i - 1, j)
            replace = dp(i - 1, j - 1)

            memo[state] = 1 + min(insert, delete, replace)

        return memo[state]

    return dp(len(a), len(b))


def edit_distance_tabulation(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m + 1):
        dp[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],      # insert
                    dp[i - 1][j],      # delete
                    dp[i - 1][j - 1]   # replace
                )

    return dp[m][n]


# Mental picture on mismatch:
#
#          insert -> dp(i, j-1)
#
# delete -> dp(i-1, j)
#
# replace -> dp(i-1, j-1)
#
# Each operation costs 1, hence "+ 1".
#
# Example:
#   horse -> ros has distance 3.
#
# Complexity:
#   Time  = O(m*n)
#   Space = O(m*n), reducible to O(min(m,n)) if only distance is needed.
#
if __name__ == "__main__":
    print(edit_distance_memo("horse", "ros"))
    print(edit_distance_tabulation("horse", "ros"))
