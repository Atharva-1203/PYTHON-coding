"""
DYNAMIC PROGRAMMING MASTER GUIDE
================================

STUDY ORDER:
    Foundations + Memoization
    -> Grid DP
    -> LCS / Common Substring
    -> Edit Distance
    -> Matrix Chain Multiplication
    -> LeetCode practice

==================================================
1. DP IN ONE SENTENCE
==================================================

Solve a problem as smaller states, notice repeated states, and store
each state's answer so it is not recomputed.

==================================================
2. THE 5 QUESTIONS
==================================================

1. STATE:
       What completely describes a subproblem?

2. CHOICE:
       What decisions can I make?

3. TRANSITION:
       How do choices move between states?

4. BASE CASE:
       What are the smallest states?

5. FINAL ANSWER:
       Which state contains the requested answer?

==================================================
3. MEMOIZATION TEMPLATE
==================================================

memo = {}

def dp(state):
    if base_case:
        return base_answer

    if state in memo:
        return memo[state]

    answer = ...
    memo[state] = answer
    return answer

KEY RULE:
    Same state -> same answer.

If answer can change because of capacity, previous choice, index, etc.,
that information belongs in the state.

==================================================
4. TABULATION
==================================================

Bottom-up:
    initialize smallest states
    compute larger states in dependency order
    return final state

Memoization:
    top-down, usually recursive, computes reachable states.

Tabulation:
    bottom-up, iterative, may compute every table state.

==================================================
5. CORE PATTERNS
==================================================

Fibonacci / Climbing Stairs:
    state = i
    time = O(n)

Grid:
    state = (r,c)
    time = O(rows*cols)

LCS:
    state = (i,j)
    match = diagonal + 1
    mismatch = max(up,left)
    time = O(m*n)

Longest Common Substring:
    state = (i,j)
    match = diagonal + 1
    mismatch = 0
    time = O(m*n)

Edit Distance:
    state = (i,j)
    mismatch = 1 + min(insert,delete,replace)
    time = O(m*n)

Matrix Chain:
    state = (i,j)
    try every split k
    time = O(n^3)

==================================================
6. SUBSEQUENCE VS SUBSTRING
==================================================

SUBSEQUENCE:
    Can skip characters.

SUBSTRING:
    Must be contiguous.

LCS mismatch:
    max(up,left)

Substring mismatch:
    0

This is one of the most important distinctions in string DP.

==================================================
7. GRID DP
==================================================

Typical:
    dp[r][c]

Counting:
    top + left

Minimum:
    cell_cost + min(top,left)

Maximum:
    cell_value + max(top,left)

Obstacles:
    blocked -> 0 (for counting), or an impossible value for optimization.

==================================================
8. EDIT DISTANCE
==================================================

State:
    dp(i,j) = minimum operations for A[:i] -> B[:j]

Base:
    dp(0,j) = j
    dp(i,0) = i

Match:
    dp(i,j) = dp(i-1,j-1)

Mismatch:
    1 + min(
        dp(i,j-1),       # insert
        dp(i-1,j),       # delete
        dp(i-1,j-1)      # replace
    )

==================================================
9. INTERVAL DP
==================================================

State:
    dp(i,j) = answer for interval i...j

Then:
    try every split k

Generic shape:
    best over k:
        left_answer
        + right_answer
        + combine_cost

Matrix Chain Multiplication is the classic example.

==================================================
10. COMPLEXITY RULE
==================================================

VERY USEFUL:

    Time ≈ unique states × work per state

Examples:

LCS:
    O(m*n) states × O(1) work = O(m*n)

Edit Distance:
    O(m*n) states × O(1) work = O(m*n)

MCM:
    O(n^2) states × O(n) splits = O(n^3)

==================================================
11. SPACE
==================================================

Usually:
    stored states + recursion stack

2D string/grid DP:
    often O(m*n)

If only previous row is required:
    often optimize to O(min(m,n))

Do NOT optimize space before the recurrence is correct.

==================================================
12. DP DEBUGGING
==================================================

Use tiny inputs.

Strings:
    ""
    "a"
    equal strings
    completely different strings

Grids:
    1x1
    1xn
    mx1
    blocked start/end

MCM:
    one matrix
    two matrices
    three matrices

For bottom-up DP:
    ask which smaller cells each cell depends on.
    If they are not computed yet, loop order is wrong.

For memoization:
    check that the cache key contains the complete state.

==================================================
13. RECOGNITION SIGNALS
==================================================

Strong hints:
    - number of ways
    - minimum cost
    - maximum profit/value
    - longest/shortest
    - number of operations
    - can/cannot achieve target
    - choose/skip
    - repeated subproblems
    - grid movement
    - partition a sequence/range

But not every optimization problem is DP.
You still need a manageable state and overlapping subproblems.

==================================================
14. LEETCODE STUDY PATH
==================================================

LEVEL 1:
    Fibonacci
    Climbing Stairs
    Min Cost Climbing Stairs

LEVEL 2:
    Unique Paths
    Unique Paths II
    Minimum Path Sum

LEVEL 3:
    House Robber
    Coin Change
    Partition Equal Subset Sum
    0/1 Knapsack

LEVEL 4:
    Longest Common Subsequence
    Longest Palindromic Subsequence
    Edit Distance
    Common Substring variants

LEVEL 5:
    Matrix Chain Multiplication
    Burst Balloons
    Palindrome Partitioning

==================================================
15. EXAM ANSWER FORMAT
==================================================

When asked for a DP solution, write:

    State definition
    Base cases
    Recurrence
    Evaluation order
    Final answer
    Time complexity
    Space complexity

==================================================
16. FINAL CHEAT SHEET
==================================================

MEMOIZATION = recursion + cache

TABULATION = iterative table

STATE = complete description of a subproblem

TRANSITION = how choices connect states

BASE CASE = smallest solvable state

LCS:
    match -> diagonal + 1
    mismatch -> max(up,left)

COMMON SUBSTRING:
    match -> diagonal + 1
    mismatch -> 0

EDIT DISTANCE:
    match -> diagonal
    mismatch -> 1 + min(insert,delete,replace)

GRID:
    count -> top + left
    min   -> cost + min(top,left)
    max   -> value + max(top,left)

MCM:
    interval + try every split

MOST IMPORTANT QUESTION:
    "What information completely determines the remaining problem?"

If you can answer that, you have solved the hardest conceptual part of DP.
"""
