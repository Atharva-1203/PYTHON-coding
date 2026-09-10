"""
DP FOUNDATIONS + MEMOIZATION
============================
Dynamic Programming = solve overlapping subproblems once, save answers,
and reuse them.

Two styles:
    Top-down  = recursion + memoization
    Bottom-up = tabulation

Before coding, identify:
    STATE -> CHOICE -> TRANSITION -> BASE CASE -> FINAL ANSWER
"""

def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n):
    """Top-down DP: recursion + cache."""
    memo = {}

    def dp(x):
        if x <= 1:
            return x
        if x in memo:
            return memo[x]

        memo[x] = dp(x - 1) + dp(x - 2)
        return memo[x]

    return dp(n)


def fib_tabulation(n):
    """Bottom-up DP."""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fib_optimized(n):
    """Same recurrence, O(1) extra space."""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1


def climb_stairs(n):
    """
    State: current stair i
    Choices: take 1 or 2 steps
    Transition: dp(i-1) + dp(i-2)
    """
    memo = {}

    def dp(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]

        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)


# IMPORTANT MEMOIZATION RULE:
# The state must contain ALL information that can change the answer.
#
# Bad example:
#     dp(i)
# when the answer also depends on capacity.
#
# Correct:
#     dp(i, capacity)
#
# For multiple variables:
#     memo[(i, capacity)] = answer
#
# A useful complexity rule:
#     Time ≈ (# unique states) × (work per state)
#
# DP recognition signals:
#     count ways, min/max, longest/shortest, number of operations,
#     choose/skip, repeated smaller problems, grid movement, partitions.
#
# DP vs recursion:
#     recursion solves smaller problems;
#     DP also REUSES repeated smaller problems.
#
# Practice order:
#     Fibonacci -> Climbing Stairs -> Min Cost Climbing Stairs
#     -> House Robber -> Coin Change -> Knapsack
#
if __name__ == "__main__":
    print(fib_memo(10))
    print(fib_tabulation(10))
    print(climb_stairs(5))
