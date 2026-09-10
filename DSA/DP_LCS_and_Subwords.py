"""
LCS + COMMON SUBSTRING
======================

SUBSEQUENCE:
    Characters need not be adjacent.
    "ace" is a subsequence of "abcde".

SUBSTRING / contiguous common subword:
    Characters MUST be adjacent.
    "bcd" is a substring of "abcde".
"""

def lcs_memo(a, b):
    """
    dp(i,j) = LCS length of a[:i] and b[:j].

    Match:
        1 + dp(i-1,j-1)

    Mismatch:
        max(dp(i-1,j), dp(i,j-1))
    """
    memo = {}

    def dp(i, j):
        if i == 0 or j == 0:
            return 0

        state = (i, j)
        if state in memo:
            return memo[state]

        if a[i - 1] == b[j - 1]:
            memo[state] = 1 + dp(i - 1, j - 1)
        else:
            memo[state] = max(dp(i - 1, j), dp(i, j - 1))

        return memo[state]

    return dp(len(a), len(b))


def lcs_tabulation(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(a, b):
    """Return one actual LCS, not just its length."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    answer = []
    i, j = m, n

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            answer.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(answer))


def longest_common_substring(a, b):
    """
    DIFFERENCE FROM LCS:
    mismatch -> 0, because a contiguous substring cannot cross a mismatch.
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    best_len = 0
    best_end = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

                if dp[i][j] > best_len:
                    best_len = dp[i][j]
                    best_end = i
            else:
                dp[i][j] = 0

    return a[best_end - best_len:best_end]


# Memorize this difference:
#
# LCS:
#   match    -> diagonal + 1
#   mismatch -> max(up, left)
#
# SUBSTRING:
#   match    -> diagonal + 1
#   mismatch -> 0
#
# Complexity for strings of lengths m,n:
#   Time  = O(m*n)
#   Space = O(m*n)
#
if __name__ == "__main__":
    print(lcs_memo("abcde", "ace"))
    print(lcs_string("abcde", "ace"))
    print(longest_common_substring("abcde", "zbcdf"))
