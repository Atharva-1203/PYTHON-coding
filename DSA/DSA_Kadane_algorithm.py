
"""
===============================================================================
                KADANE'S ALGORITHM: COMPLETE DSA REVISION
===============================================================================

Purpose:
    A complete, systematic guide to Kadane's Algorithm and its applications.

Requirements:
    Python 3.x

How to run:
    python kadanes_algorithm_dsa.py

TOPICS COVERED:
    1. Understanding the maximum subarray problem
    2. Subarray vs subsequence
    3. Brute-force approach
    4. Prefix-sum approach
    5. Kadane's Algorithm: intuition and implementation
    6. Dry run and step-by-step tracing
    7. Handling all-negative arrays
    8. Finding the actual maximum subarray
    9. Maximum subarray variations
   10. Maximum circular subarray sum
   11. Maximum product subarray
   12. Maximum sum of a fixed-length subarray
   13. Maximum subarray with length at most K
   14. Divide-and-conquer approach
   15. Two-dimensional maximum subarray
   16. Time and space complexity
   17. Common mistakes
   18. Practice problems

===============================================================================
"""


# =============================================================================
# SECTION 1: UNDERSTANDING THE MAXIMUM SUBARRAY PROBLEM
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 1: THE MAXIMUM SUBARRAY PROBLEM")
print("=" * 80)

# PROBLEM:
#
# Given an array of integers, find a NON-EMPTY contiguous subarray
# whose sum is as large as possible.
#
# Example:
#
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# One maximum-sum subarray is:
#
# [4, -1, 2, 1]
#
# Its sum is:
#
# 4 + (-1) + 2 + 1 = 6
#
# Therefore, the maximum subarray sum is 6.
#
# IMPORTANT:
# We must select contiguous elements.
#
# We cannot arbitrarily skip elements inside a subarray.


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Array:", arr)
print("Expected maximum subarray sum:", 6)


# =============================================================================
# SECTION 2: SUBARRAY VS SUBSEQUENCE
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 2: SUBARRAY VS SUBSEQUENCE")
print("=" * 80)

# SUBARRAY:
# A contiguous portion of an array.
#
# Example:
#
# arr = [1, 2, 3, 4]
#
# Valid subarrays include:
# [1]
# [2, 3]
# [1, 2, 3]
# [3, 4]
# [1, 2, 3, 4]
#
# [1, 3] is NOT a subarray because the elements are not contiguous.
#
#
# SUBSEQUENCE:
# A sequence obtained by deleting zero or more elements without
# changing the relative order of the remaining elements.
#
# For [1, 2, 3, 4]:
#
# [1, 3] is a valid subsequence.
#
# It is not a subarray.
#
#
# WHY THIS MATTERS:
#
# Maximum subarray:
# We must respect contiguity.
#
# Maximum subsequence sum:
# Depending on the exact problem definition, selecting all positive
# elements may be optimal, so the solution can be different.


# =============================================================================
# SECTION 3: THE BRUTE-FORCE APPROACH
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 3: BRUTE-FORCE APPROACH")
print("=" * 80)

# IDEA:
#
# Generate every possible non-empty subarray.
# Calculate its sum.
# Keep track of the largest sum.
#
# For an array of length n, there are:
#
# n * (n + 1) // 2
#
# non-empty contiguous subarrays.
#
# A straightforward implementation that calculates each subarray sum
# separately takes O(n^3) time.
#
# We can improve it to O(n^2) by maintaining a running sum for each
# possible starting index.


def maximum_subarray_bruteforce(arr):
    """
    Find the maximum non-empty subarray sum using a running sum.

    Time complexity: O(n^2)
    Auxiliary space: O(1)

    Returns:
        Maximum subarray sum.

    Raises:
        ValueError: If arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    best_sum = arr[0]

    # Choose the starting position.
    for start in range(len(arr)):

        current_sum = 0

        # Extend the subarray one element at a time.
        for end in range(start, len(arr)):

            current_sum += arr[end]

            # Update the best sum.
            if current_sum > best_sum:
                best_sum = current_sum

    return best_sum


example = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Array:", example)
print("Brute-force answer:", maximum_subarray_bruteforce(example))

# LIMITATION:
#
# The O(n^2) approach becomes slow for very large arrays.
#
# For n = 100,000, a quadratic algorithm would require an impractical
# number of operations.
#
# We need a better approach.


# =============================================================================
# SECTION 4: PREFIX-SUM APPROACH
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 4: PREFIX-SUM APPROACH")
print("=" * 80)

# IDEA:
#
# Define:
#
# prefix[i] = sum of the first i elements.
#
# Then the sum of arr[left:right + 1] is:
#
# prefix[right + 1] - prefix[left]
#
# This allows a subarray sum to be calculated in O(1) after building
# the prefix-sum array.
#
# However, checking every possible pair of boundaries still requires
# O(n^2) time.


def maximum_subarray_prefix_sum(arr):
    """
    Find the maximum non-empty subarray sum using prefix sums.

    Time complexity: O(n^2)
    Auxiliary space: O(n)

    Returns:
        Maximum subarray sum.

    Raises:
        ValueError: If arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    prefix = [0]

    for value in arr:
        prefix.append(prefix[-1] + value)

    best_sum = arr[0]
    n = len(arr)

    for left in range(n):

        for right in range(left, n):

            current_sum = prefix[right + 1] - prefix[left]

            if current_sum > best_sum:
                best_sum = current_sum

    return best_sum


example = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Prefix-sum answer:", maximum_subarray_prefix_sum(example))

# We now know how to calculate subarray sums efficiently.
#
# Kadane's Algorithm improves the overall problem to O(n) time
# by avoiding the need to examine every possible subarray.


# =============================================================================
# SECTION 5: KADANE'S ALGORITHM — THE CORE IDEA
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 5: KADANE'S ALGORITHM")
print("=" * 80)

# THE CENTRAL QUESTION:
#
# Suppose we are processing the next element x.
#
# We have two choices:
#
# CHOICE 1:
# Start a new subarray at x.
#
# CHOICE 2:
# Extend the best subarray ending at the previous position by adding x.
#
# Therefore:
#
# current_sum = max(x, current_sum + x)
#
# This is the fundamental recurrence relation of Kadane's Algorithm.
#
# At every position:
#
# current_sum = maximum sum of a non-empty subarray ending here.
#
# global_max = maximum subarray sum found anywhere so far.
#
# Update:
#
# global_max = max(global_max, current_sum)
#
# These two variables represent DIFFERENT things.
#
# current_sum:
# The best subarray sum ending at the current position.
#
# global_max:
# The best subarray sum across all positions processed so far.


def kadane(arr):
    """
    Return the maximum non-empty subarray sum.

    Time complexity: O(n)
    Auxiliary space: O(1)

    The input is not modified.

    Raises:
        ValueError: If arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    # Initialise with the first element rather than zero.
    #
    # This is essential for correctly handling arrays containing
    # only negative values.

    current_sum = arr[0]
    global_max = arr[0]

    # Start from the second element.
    for i in range(1, len(arr)):

        value = arr[i]

        # Either:
        # 1. Start a new subarray at value.
        # 2. Extend the previous subarray.

        current_sum = max(value, current_sum + value)

        # Update the best answer seen anywhere.

        global_max = max(global_max, current_sum)

    return global_max


example = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Array:", example)
print("Kadane's answer:", kadane(example))

# Expected answer: 6
#
# Time complexity: O(n)
# Auxiliary space: O(1)


# =============================================================================
# SECTION 6: STEP-BY-STEP DRY RUN
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 6: KADANE'S ALGORITHM DRY RUN")
print("=" * 80)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
global_max = arr[0]

print("Array:", arr)
print()
print(f"{'Index':<8}{'Value':<10}{'Current Sum':<16}{'Global Max':<12}")
print("-" * 46)

print(f"{0:<8}{arr[0]:<10}{current_sum:<16}{global_max:<12}")

for i in range(1, len(arr)):

    value = arr[i]

    # Keep extending or start a new subarray.
    current_sum = max(value, current_sum + value)

    # Update the overall maximum.
    global_max = max(global_max, current_sum)

    print(f"{i:<8}{value:<10}{current_sum:<16}{global_max:<12}")

print("-" * 46)
print("Final maximum subarray sum:", global_max)

# INTERPRETATION:
#
# At index 3, the value is 4.
#
# The previous current_sum is negative, so extending the old subarray
# would be worse than starting a new subarray at 4.
#
# Kadane's Algorithm effectively discards the unhelpful earlier portion.
#
# It then continues extending the subarray while doing so improves
# the sum.
#
# The best subarray is [4, -1, 2, 1], whose sum is 6.


# =============================================================================
# SECTION 7: WHY INITIALISING WITH ZERO CAN BE WRONG
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 7: HANDLING NEGATIVE NUMBERS")
print("=" * 80)

# Consider:
#
# arr = [-8, -3, -6, -2, -5, -4]
#
# The maximum non-empty subarray is [-2].
#
# Therefore, the answer must be -2.
#
# A common incorrect implementation is:
#
# current_sum = 0
# global_max = 0
#
# This returns 0 for an all-negative array.
#
# But 0 is not a valid answer because the problem requires a NON-EMPTY
# subarray.


negative_array = [-8, -3, -6, -2, -5, -4]

print("All-negative array:", negative_array)
print("Correct answer:", kadane(negative_array))

# The correct initialisation is:
#
# current_sum = arr[0]
# global_max = arr[0]
#
# This ensures that at least one element is selected.


# Demonstrate another important edge case.

single_element = [-10]

print("Single-element array:", single_element)
print("Maximum subarray sum:", kadane(single_element))

# A one-element array must return that element.


# =============================================================================
# SECTION 8: FIND THE ACTUAL MAXIMUM SUBARRAY
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 8: FIND THE SUBARRAY, NOT JUST ITS SUM")
print("=" * 80)

# Sometimes the question asks for:
#
# 1. Maximum subarray sum.
# 2. Starting index.
# 3. Ending index.
# 4. The actual subarray.
#
# We can solve this by tracking boundaries.
#
# Whenever a new subarray is started, record a temporary starting index.
#
# Whenever a better global maximum is found, save the boundaries.


def kadane_with_indices(arr):
    """
    Find the maximum subarray sum and its boundaries.

    Returns:
        (maximum_sum, start_index, end_index)

    The indices are inclusive.

    Time complexity: O(n)
    Auxiliary space: O(1), excluding the returned result.

    Raises:
        ValueError: If arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    current_sum = arr[0]
    best_sum = arr[0]

    # The current candidate subarray starts at index 0.
    temporary_start = 0

    # Best subarray boundaries found so far.
    best_start = 0
    best_end = 0

    for i in range(1, len(arr)):

        value = arr[i]

        # If starting fresh is better, discard the previous candidate.
        if value > current_sum + value:

            current_sum = value
            temporary_start = i

        else:

            current_sum += value

        # Update the best subarray if necessary.
        if current_sum > best_sum:

            best_sum = current_sum
            best_start = temporary_start
            best_end = i

    return best_sum, best_start, best_end


example = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maximum_sum, start, end = kadane_with_indices(example)

print("Original array:", example)
print("Maximum sum:", maximum_sum)
print("Start index:", start)
print("End index:", end)
print("Actual maximum subarray:", example[start:end + 1])

# Expected:
#
# Maximum sum: 6
# Start index: 3
# End index: 6
# Actual maximum subarray: [4, -1, 2, 1]
#
# Python slicing excludes the ending index.
# Therefore, use arr[start:end + 1] to include both boundaries.


# =============================================================================
# SECTION 9: KADANE'S ALGORITHM — TRACE EVERY SUBARRAY DECISION
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 9: UNDERSTANDING THE DECISION AT EACH POSITION")
print("=" * 80)

arr = [3, -4, 2, -1, 6, -3, 2]

current_sum = arr[0]
global_max = arr[0]

print("Array:", arr)
print()

for i in range(1, len(arr)):

    value = arr[i]

    extend_sum = current_sum + value

    if value > extend_sum:

        decision = "Start new subarray"
        current_sum = value

    else:

        decision = "Extend previous subarray"
        current_sum = extend_sum

    global_max = max(global_max, current_sum)

    print(
        f"Index={i}, "
        f"value={value:>3}, "
        f"decision={decision:<24}, "
        f"current={current_sum:>3}, "
        f"global={global_max:>3}"
    )

# If extending a subarray is beneficial, keep extending.
# Otherwise, begin a new candidate at the current element.
#
# The global maximum records the best result regardless of where
# the candidate subarray currently ends.


# =============================================================================
# SECTION 10: MAXIMUM SUBARRAY SUM — RETURN THE SUM AND SUBARRAY
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 10: RETURNING THE SUM AND SUBARRAY TOGETHER")
print("=" * 80)


def maximum_subarray(arr):
    """
    Return the maximum sum and the corresponding subarray.

    Returns:
        (maximum_sum, subarray)

    Time complexity: O(n)
    Auxiliary space: O(1) for the algorithm's working state,
                      excluding the returned subarray.

    Note:
        Creating the returned subarray requires O(k) additional space,
        where k is the length of that subarray.
    """

    best_sum, start, end = kadane_with_indices(arr)

    return best_sum, arr[start:end + 1]


example = [5, -9, 6, -2, 3, -1, 2, -8, 4]

best_sum, best_subarray = maximum_subarray(example)

print("Array:", example)
print("Maximum sum:", best_sum)
print("Maximum subarray:", best_subarray)


# =============================================================================
# SECTION 11: VARIATION — MAXIMUM SUBARRAY WITH A NON-EMPTY REQUIREMENT
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 11: NON-EMPTY MAXIMUM SUBARRAY")
print("=" * 80)

# The standard Kadane implementation in this program already solves
# the non-empty version of the problem.
#
# Examples:
#
# [1, 2, 3]       -> 6
# [-1, -2, -3]    -> -1
# [0, -2, 0]      -> 0
# [-5]            -> -5
#
# The distinction matters because some problem statements allow an
# empty subarray, while others require at least one element.
#
# If an empty subarray is permitted, its sum may be 0.
# In that variant, the answer is at least 0.


def kadane_allow_empty(arr):
    """
    Return the maximum subarray sum when an empty subarray is allowed.

    An empty subarray has sum 0.

    Time complexity: O(n)
    Auxiliary space: O(1)
    """

    current_sum = 0
    best_sum = 0

    for value in arr:

        current_sum = max(0, current_sum + value)
        best_sum = max(best_sum, current_sum)

    return best_sum


print("Non-empty answer for [-5, -2, -8]:", kadane([-5, -2, -8]))
print("Empty-allowed answer for [-5, -2, -8]:",
      kadane_allow_empty([-5, -2, -8]))


# =============================================================================
# SECTION 12: MAXIMUM CIRCULAR SUBARRAY SUM
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 12: MAXIMUM CIRCULAR SUBARRAY SUM")
print("=" * 80)

# In a circular array, the last element is adjacent to the first.
#
# Example:
#
# arr = [5, -3, 5]
#
# The ordinary maximum subarray sum is 7:
#
# [5, -3, 5] -> 7
#
# But a circular subarray can include the last and first elements:
#
# [5] + [5] -> 10
#
# Therefore, the circular answer is 10.
#
#
# KEY IDEA:
#
# There are two possibilities:
#
# CASE 1:
# The maximum subarray does not wrap around the boundary.
#
# Answer = ordinary Kadane's result.
#
# CASE 2:
# The maximum subarray wraps around the boundary.
#
# The selected circular subarray consists of:
# - A suffix of the original array.
# - A prefix of the original array.
#
# It is easier to remove the minimum-sum subarray from the middle.
#
# Therefore:
#
# Maximum circular sum =
# max(
#     maximum ordinary subarray sum,
#     total sum - minimum subarray sum
# )
#
# IMPORTANT EDGE CASE:
#
# If every element is negative, total_sum - minimum_subarray_sum becomes 0.
#
# That represents selecting no elements, which is invalid when the
# problem requires a non-empty subarray.
#
# We must return the ordinary Kadane result in that case.


def minimum_subarray_sum(arr):
    """
    Find the minimum non-empty subarray sum.

    Time complexity: O(n)
    Auxiliary space: O(1)
    """

    current_min = arr[0]
    global_min = arr[0]

    for value in arr[1:]:

        current_min = min(value, current_min + value)
        global_min = min(global_min, current_min)

    return global_min


def maximum_circular_subarray_sum(arr):
    """
    Find the maximum non-empty circular subarray sum.

    Time complexity: O(n)
    Auxiliary space: O(1)

    Raises:
        ValueError: If arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    ordinary_max = kadane(arr)
    total_sum = sum(arr)

    # If the ordinary maximum is negative, all elements are negative.
    # Returning total_sum - minimum_subarray_sum would incorrectly give 0.

    if ordinary_max < 0:
        return ordinary_max

    minimum_sum = minimum_subarray_sum(arr)

    wrapped_max = total_sum - minimum_sum

    return max(ordinary_max, wrapped_max)


examples = [
    [5, -3, 5],
    [1, -2, 3, -2],
    [-3, -2, -5],
    [3, -1, 2, -1],
]

for example in examples:

    print(
        "Array:", example,
        "| Circular maximum:", maximum_circular_subarray_sum(example)
    )


# =============================================================================
# SECTION 13: MAXIMUM PRODUCT SUBARRAY
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 13: MAXIMUM PRODUCT SUBARRAY")
print("=" * 80)

# PROBLEM:
#
# Find the maximum product of a non-empty contiguous subarray.
#
# Example:
#
# arr = [2, 3, -2, 4]
#
# Maximum product = 6
#
# Subarray = [2, 3]
#
#
# WHY ORDINARY KADANE'S ALGORITHM DOES NOT DIRECTLY WORK:
#
# Kadane's Algorithm uses addition.
#
# Maximum product subarrays use multiplication.
#
# A negative product can become positive after multiplication
# by another negative number.
#
# Therefore, we track BOTH:
#
# maximum product ending at the current position.
# minimum product ending at the current position.
#
# The minimum product is important because it may become the maximum
# after multiplication by a negative value.


def maximum_product_subarray(arr):
    """
    Return the maximum product of a non-empty contiguous subarray.

    Time complexity: O(n)
    Auxiliary space: O(1)

    Raises:
        ValueError: If arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    current_max = arr[0]
    current_min = arr[0]

    global_max = arr[0]

    for value in arr[1:]:

        # Save the previous maximum and minimum before updating.
        previous_max = current_max
        previous_min = current_min

        # The current value can:
        # 1. Start a new subarray.
        # 2. Extend the previous maximum product.
        # 3. Extend the previous minimum product.

        current_max = max(
            value,
            value * previous_max,
            value * previous_min
        )

        current_min = min(
            value,
            value * previous_max,
            value * previous_min
        )

        global_max = max(global_max, current_max)

    return global_max


product_examples = [
    [2, 3, -2, 4],
    [-2, 0, -1],
    [-2, 3, -4],
    [-2],
    [-2, -3, -4],
]

for example in product_examples:

    print(
        "Array:", example,
        "| Maximum product:", maximum_product_subarray(example)
    )


# =============================================================================
# SECTION 14: MAXIMUM SUM OF A FIXED-LENGTH SUBARRAY
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 14: FIXED-LENGTH SUBARRAY")
print("=" * 80)

# PROBLEM:
#
# Given an array and an integer k, find the maximum sum of a contiguous
# subarray containing EXACTLY k elements.
#
# Example:
#
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
#
# Subarrays of length 3:
#
# [2, 1, 5] -> 8
# [1, 5, 1] -> 7
# [5, 1, 3] -> 9
# [1, 3, 2] -> 6
#
# Maximum sum = 9
#
# This problem is usually solved using a sliding window.
#
# TIME COMPLEXITY:
# O(n)
#
# We calculate the first window's sum once.
# For each next window:
# - Subtract the element leaving the window.
# - Add the element entering the window.


def maximum_fixed_length_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray containing exactly k elements.

    Time complexity: O(n)
    Auxiliary space: O(1)

    Raises:
        ValueError: If k is invalid or exceeds the array length.
    """

    if k <= 0:
        raise ValueError("k must be greater than zero.")

    if k > len(arr):
        raise ValueError("k cannot exceed the array length.")

    # Calculate the first window.
    window_sum = sum(arr[:k])
    best_sum = window_sum

    # Move the window one position at a time.
    for right in range(k, len(arr)):

        # Remove the element leaving the window.
        window_sum -= arr[right - k]

        # Add the new element entering the window.
        window_sum += arr[right]

        best_sum = max(best_sum, window_sum)

    return best_sum


example = [2, 1, 5, 1, 3, 2]

print("Array:", example)
print("Window length:", 3)
print("Maximum fixed-length sum:",
      maximum_fixed_length_subarray_sum(example, 3))

# IMPORTANT:
#
# Standard Kadane's Algorithm allows subarrays of different lengths.
#
# A fixed-length maximum-sum problem is usually better solved using
# a sliding window.


# =============================================================================
# SECTION 15: MAXIMUM SUBARRAY WITH LENGTH AT MOST K
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 15: MAXIMUM SUBARRAY WITH LENGTH AT MOST K")
print("=" * 80)

# PROBLEM:
#
# Find the maximum sum of a non-empty contiguous subarray whose length
# is at most k.
#
# We can solve this using prefix sums and a monotonic deque.
#
# Let prefix[i] be the sum of the first i elements.
#
# The sum of the subarray arr[left:right] is:
#
# prefix[right] - prefix[left]
#
# If the subarray length must be at most k:
#
# right - left <= k
#
# Therefore:
#
# right - k <= left < right
#
# For every right boundary, we want the smallest prefix[left] among
# the valid left boundaries.
#
# A monotonic deque maintains candidate prefix indices in increasing
# order of prefix sum.
#
# Time complexity: O(n)
# Auxiliary space: O(n)
#
# This is an advanced sliding-window/prefix-sum technique.


from collections import deque


def maximum_subarray_sum_at_most_k(arr, k):
    """
    Find the maximum non-empty subarray sum with length at most k.

    Time complexity: O(n)
    Auxiliary space: O(n)

    Raises:
        ValueError: If k is invalid or arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    if k <= 0:
        raise ValueError("k must be greater than zero.")

    k = min(k, len(arr))

    prefix = [0]

    for value in arr:
        prefix.append(prefix[-1] + value)

    # Stores indices of prefix sums in increasing order of value.
    candidates = deque()

    best_sum = None

    for right in range(1, len(prefix)):

        # The earliest allowed left boundary is right - k.
        minimum_left = right - k

        # Remove indices that would produce a subarray longer than k.
        while candidates and candidates[0] < minimum_left:
            candidates.popleft()

        # The prefix at right - 1 becomes a new possible left boundary.
        new_left = right - 1

        # Remove dominated prefix candidates.
        #
        # If an earlier prefix is greater than or equal to the new one,
        # it cannot produce a better sum for any future right boundary.
        while (
            candidates
            and prefix[candidates[-1]] >= prefix[new_left]
        ):
            candidates.pop()

        candidates.append(new_left)

        # The smallest valid prefix gives the largest subarray sum.
        current_sum = prefix[right] - prefix[candidates[0]]

        if best_sum is None or current_sum > best_sum:
            best_sum = current_sum

    return best_sum


example = [3, -5, 2, 7, -2, 4]

print("Array:", example)
print("Maximum sum with length at most 3:",
      maximum_subarray_sum_at_most_k(example, 3))


# =============================================================================
# SECTION 16: DIVIDE-AND-CONQUER APPROACH
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 16: DIVIDE AND CONQUER")
print("=" * 80)

# Kadane's Algorithm is not the only way to solve the maximum subarray
# problem.
#
# A divide-and-conquer solution splits the array into two halves.
#
# The maximum subarray must be:
#
# 1. Entirely in the left half.
# 2. Entirely in the right half.
# 3. Crossing the midpoint.
#
# We solve the first two recursively and calculate the best crossing
# subarray by finding:
#
# - The maximum suffix sum of the left half.
# - The maximum prefix sum of the right half.
#
# Their sum gives the best crossing subarray.
#
# Time complexity: O(n log n)
# Auxiliary space: O(log n) recursion stack, excluding input storage.


def maximum_subarray_divide_conquer(arr):
    """
    Find the maximum non-empty subarray sum using divide and conquer.

    Time complexity: O(n log n)
    Auxiliary space: O(log n) recursion stack.

    Raises:
        ValueError: If arr is empty.
    """

    if not arr:
        raise ValueError("The input array must not be empty.")

    def solve(left, right):

        # Base case: one element.
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        # Best answer entirely in the left half.
        left_best = solve(left, mid)

        # Best answer entirely in the right half.
        right_best = solve(mid + 1, right)

        # Best suffix ending at the midpoint.
        current_sum = 0
        left_suffix_best = float("-inf")

        for i in range(mid, left - 1, -1):

            current_sum += arr[i]
            left_suffix_best = max(left_suffix_best, current_sum)

        # Best prefix starting at the right half's first element.
        current_sum = 0
        right_prefix_best = float("-inf")

        for i in range(mid + 1, right + 1):

            current_sum += arr[i]
            right_prefix_best = max(right_prefix_best, current_sum)

        crossing_best = left_suffix_best + right_prefix_best

        return max(left_best, right_best, crossing_best)

    return solve(0, len(arr) - 1)


example = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Divide-and-conquer answer:",
      maximum_subarray_divide_conquer(example))


# =============================================================================
# SECTION 17: TWO-DIMENSIONAL MAXIMUM SUBARRAY
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 17: MAXIMUM-SUM SUBMATRIX")
print("=" * 80)

# ADVANCED PROBLEM:
#
# Given a 2D matrix, find a non-empty rectangular submatrix with
# the largest possible sum.
#
# APPROACH:
#
# Fix the top row.
# Extend the bottom row one row at a time.
# Maintain the column sums between the selected top and bottom rows.
# Apply Kadane's Algorithm to those column sums.
#
# This reduces the 2D problem to repeated 1D maximum subarray problems.
#
# For an R x C matrix, this implementation takes:
#
# O(min(R, C)^2 * max(R, C))
#
# We transpose the conceptual orientation when necessary so that
# the squared dimension is the smaller one.


def maximum_submatrix_sum(matrix):
    """
    Find the maximum sum of a non-empty rectangular submatrix.

    Returns:
        Maximum submatrix sum.

    Time complexity:
        O(min(R, C)^2 * max(R, C))

    Auxiliary space:
        O(max(R, C))

    Raises:
        ValueError: If the matrix is empty or has empty rows.
    """

    if not matrix or not matrix[0]:
        raise ValueError("The matrix must not be empty.")

    rows = len(matrix)
    columns = len(matrix[0])

    if any(len(row) != columns for row in matrix):
        raise ValueError("All matrix rows must have equal length.")

    # Make the number of rows the smaller dimension.
    # This reduces the number of row-boundary pairs.

    if rows > columns:

        matrix = [
            [matrix[r][c] for r in range(rows)]
            for c in range(columns)
        ]

        rows, columns = columns, rows

    global_best = None

    # Select the top row.
    for top in range(rows):

        column_sums = [0] * columns

        # Extend the bottom row.
        for bottom in range(top, rows):

            # Update the sum for each column in the current band.
            for col in range(columns):
                column_sums[col] += matrix[bottom][col]

            # The best rectangle for this row band is found by
            # solving a 1D maximum subarray problem.
            current_best = kadane(column_sums)

            if global_best is None or current_best > global_best:
                global_best = current_best

    return global_best


matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

print("Maximum submatrix sum:", maximum_submatrix_sum(matrix))


# =============================================================================
# SECTION 18: COMPARING THE APPROACHES
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 18: ALGORITHM COMPARISON")
print("=" * 80)

# APPROACH                              TIME COMPLEXITY
# ---------------------------------------------------------------------------
# Three nested loops, straightforward   O(n^3)
# Running-sum brute force               O(n^2)
# Prefix-sum brute force                O(n^2)
# Kadane's Algorithm                    O(n)
# Divide and conquer                    O(n log n)
# Maximum circular subarray             O(n)
# Maximum product subarray              O(n)
# Fixed-length maximum sum              O(n)
# At-most-k maximum sum                  O(n), using a monotonic deque
# Maximum-sum submatrix                  O(min(R,C)^2 * max(R,C))
#
# IMPORTANT:
#
# 1. For the ordinary maximum subarray sum, Kadane's Algorithm is
#    generally the best simple approach.
#
# 2. For a circular array, ordinary Kadane's Algorithm alone is not enough.
#
# 3. For maximum product, track both maximum and minimum products.
#
# 4. For a fixed window size, use sliding window.
#
# 5. For a maximum subarray of length at most k, a monotonic deque
#    and prefix sums provide an O(n) solution.
#
# 6. For a 2D maximum-sum rectangle, compress rows or columns and
#    repeatedly use Kadane's Algorithm.


# =============================================================================
# SECTION 19: COMMON MISTAKES
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 19: COMMON MISTAKES")
print("=" * 80)

# MISTAKE 1:
# Initialising global_max = 0 for a non-empty subarray problem.
#
# This fails for all-negative arrays.
#
# Correct:
# global_max = arr[0]


# MISTAKE 2:
# Confusing current_sum and global_max.
#
# current_sum is the best sum ending at the current position.
# global_max is the best sum found anywhere so far.


# MISTAKE 3:
# Forgetting to consider starting a new subarray.
#
# Incorrect:
# current_sum += value
#
# Correct:
# current_sum = max(value, current_sum + value)


# MISTAKE 4:
# Using the circular-array formula without checking all-negative input.
#
# total_sum - minimum_subarray_sum may equal zero when all elements
# are negative, but the non-empty answer must be negative.


# MISTAKE 5:
# Applying ordinary maximum-sum Kadane directly to maximum-product problems.
#
# Products behave differently because two negative numbers can produce
# a positive product.
#
# Track both the maximum and minimum products.


# MISTAKE 6:
# Forgetting that binary search requires sorted input.
#
# This is not a Kadane-specific issue, but it is an important DSA rule.


# MISTAKE 7:
# Confusing a subarray with a subsequence.
#
# A subarray must be contiguous.
#
# A subsequence does not have to be contiguous.


# MISTAKE 8:
# Incorrectly slicing the answer when using inclusive end indices.
#
# Correct:
# arr[start:end + 1]


# MISTAKE 9:
# Forgetting empty-input handling.
#
# The maximum non-empty subarray sum is undefined for an empty array.
# The implementations above raise ValueError for that case.


# =============================================================================
# SECTION 20: EDGE-CASE TESTING
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 20: EDGE-CASE TESTING")
print("=" * 80)

test_cases = [
    ([1, 2, 3, 4], 10),
    ([-1, -2, -3, -4], -1),
    ([5], 5),
    ([-5], -5),
    ([0, 0, 0], 0),
    ([4, -1, 2, 1], 6),
    ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
]

for test_array, expected in test_cases:

    actual = kadane(test_array)

    print(
        f"Input={test_array}, "
        f"Expected={expected}, "
        f"Actual={actual}, "
        f"Correct={actual == expected}"
    )

# Always test:
#
# 1. All-positive arrays.
# 2. All-negative arrays.
# 3. Arrays containing zeros.
# 4. Single-element arrays.
# 5. Mixed positive and negative values.
# 6. Cases where the best subarray starts at index 0.
# 7. Cases where the best subarray ends at the last index.
# 8. Cases where the best subarray lies in the middle.


# =============================================================================
# SECTION 21: PRACTICE PROBLEMS
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 21: PRACTICE PROBLEMS")
print("=" * 80)

# Solve these problems without looking at the earlier implementations.
#
# PROBLEM 1:
# Find the maximum subarray sum of:
# [1, -2, 3, 4, -1, 2, -5, 4]
#
# PROBLEM 2:
# Find the maximum subarray sum of:
# [-8, -3, -6, -2, -5, -4]
#
# PROBLEM 3:
# Find the maximum subarray and its indices:
# [2, -1, 4, -5, 3, 6, -2]
#
# PROBLEM 4:
# Implement Kadane's Algorithm without using max().
#
# PROBLEM 5:
# Return the maximum subarray sum and the actual subarray.
#
# PROBLEM 6:
# Solve the maximum circular subarray sum problem for:
# [8, -1, 3, 4]
#
# PROBLEM 7:
# Find the maximum product subarray of:
# [-2, 3, -4]
#
# PROBLEM 8:
# Find the maximum sum of a subarray containing exactly 3 elements:
# [2, 1, 5, 1, 3, 2]
#
# PROBLEM 9:
# Find the maximum sum of a subarray with length at most 2:
# [3, -5, 2, 7, -2, 4]
#
# PROBLEM 10:
# Explain why ordinary Kadane's Algorithm fails for maximum product.
#
# PROBLEM 11:
# Explain why the circular subarray formula needs a special
# all-negative check.
#
# PROBLEM 12:
# Explain the difference between O(n^2) brute force and O(n)
# Kadane's Algorithm.
#
# PROBLEM 13:
# Find the maximum-sum rectangular submatrix in a given matrix.
#
# PROBLEM 14:
# Modify the algorithm to return the start and end indices.
#
# PROBLEM 15:
# Explain why the maximum-sum subarray must be contiguous.


# =============================================================================
# SECTION 22: QUICK REVISION SUMMARY
# =============================================================================

print("\n" + "=" * 80)
print("SECTION 22: QUICK REVISION SUMMARY")
print("=" * 80)

# CORE RECURRENCE:
#
# current_sum = max(arr[i], current_sum + arr[i])
#
# global_max = max(global_max, current_sum)
#
#
# INITIALISATION:
#
# current_sum = arr[0]
# global_max = arr[0]
#
#
# COMPLEXITY:
#
# Time: O(n)
# Auxiliary space: O(1)
#
#
# KEY CONCEPTS:
#
# - A subarray is contiguous.
# - At each index, either start a new subarray or extend the old one.
# - current_sum represents the best subarray ending at the current index.
# - global_max represents the best subarray found anywhere.
# - Initialising with arr[0] handles all-negative arrays correctly.
# - Track boundaries if the actual subarray is required.
#
#
# IMPORTANT VARIATIONS:
#
# Ordinary maximum subarray sum:
#     Kadane's Algorithm.
#
# Maximum circular subarray:
#     max(ordinary maximum, total sum - minimum subarray sum),
#     with an all-negative special case.
#
# Maximum product subarray:
#     Track both the maximum and minimum product.
#
# Maximum sum for exactly k elements:
#     Sliding window.
#
# Maximum sum for length at most k:
#     Prefix sums and a monotonic deque.
#
# Maximum-sum rectangular submatrix:
#     Compress rows/columns and apply Kadane's Algorithm.
#
# PRACTICAL LESSON:
#
# First understand the recurrence relation.
# Then learn the implementation.
# Then learn the variations and their edge cases.
# Finally, practise deriving the solution without memorising code.


print("\n" + "=" * 80)
print("END OF KADANE'S ALGORITHM: COMPLETE DSA REVISION")
print("=" * 80)

print("\nRevision complete!")
print("Next step: Solve the practice problems without looking at the code.")
