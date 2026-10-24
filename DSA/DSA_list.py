"""
===============================================================================
                    PYTHON LISTS: COMPLETE DSA REVISION
===============================================================================

Purpose:
    A complete, systematic revision of Python lists from basic concepts
    to Data Structures and Algorithms (DSA).

Topics covered:
    1. List fundamentals and properties
    2. Creating lists
    3. Indexing and accessing elements
    4. len(), min(), max(), sum(), sorted(), any(), all()
    5. Slicing
    6. append(), extend(), insert()
    7. remove(), pop(), clear()
    8. index(), count()
    9. sort(), reverse()
    10. copy(), aliases, id(), shallow copies
    11. List concatenation, repetition, membership
    12. Iteration and traversal
    13. List comprehensions
    14. Nested lists and 2D lists
    15. Lists and memory references
    16. Important DSA algorithms
    17. Time and space complexity
    18. Common mistakes
    19. Practice problems

Requirements:
    Python 3.x

How to run:
    python python_lists_dsa.py

===============================================================================
"""


# =============================================================================
# SECTION 1: WHAT IS A LIST?
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 1: INTRODUCTION TO PYTHON LISTS")
print("=" * 75)

# A list is an ordered, mutable collection of elements.
# In Python, lists are created using square brackets [].

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Type:", type(numbers))

# IMPORTANT PROPERTIES OF LISTS:
#
# 1. Ordered:
#    Elements maintain their sequence.
#
# 2. Mutable:
#    Elements can be modified after the list is created.
#
# 3. Indexed:
#    Elements can be accessed using their positions.
#
# 4. Allows duplicates:
#    The same value can appear multiple times.
#
# 5. Heterogeneous:
#    A list can contain different data types.
#
# 6. Dynamic:
#    A list can grow or shrink during program execution.
#
# 7. Can contain nested lists:
#    A list can contain other lists as elements.

mixed_list = [10, "Python", 3.14, True, 10]

print("Mixed list:", mixed_list)
print("Duplicates are allowed:", [1, 2, 2, 3, 3, 3])


# =============================================================================
# SECTION 2: DIFFERENT WAYS TO CREATE A LIST
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 2: CREATING LISTS")
print("=" * 75)

# 1. An ordinary list.

a = [10, 20, 30]
print("Ordinary list:", a)

# 2. An empty list.

empty_list = []
print("Empty list:", empty_list)

# Another way to create an empty list.

empty_list_2 = list()
print("Empty list using list():", empty_list_2)

# 3. A list containing repeated values.

repeated = [0] * 5
print("Repeated values:", repeated)

# 4. Creating a list from a range.

sequence = list(range(1, 6))
print("Numbers from 1 to 5:", sequence)

# range(1, 6) generates 1, 2, 3, 4, 5.
# The stopping value 6 is excluded.

# 5. Creating a list from a string.

characters = list("PYTHON")
print("Characters:", characters)

# 6. A list containing different data types.

different_types = [100, 2.5, "Hello", False]
print("Different data types:", different_types)

# 7. A nested list.

nested = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested)


# =============================================================================
# SECTION 3: INDEXING AND ACCESSING ELEMENTS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 3: INDEXING")
print("=" * 75)

values = [10, 20, 30, 40, 50]

# Python uses ZERO-BASED INDEXING.
#
# Element:  10   20   30   40   50
# Index:     0    1    2    3    4
# Negative: -5   -4   -3   -2   -1

print("Original list:", values)

print("First element:", values[0])
print("Second element:", values[1])
print("Last element:", values[-1])
print("Second-last element:", values[-2])

# len() returns the number of elements.
# The last valid positive index is len(list) - 1.

print("Length:", len(values))
print("Last valid positive index:", len(values) - 1)

# Accessing an invalid index raises IndexError.
#
# Example:
# print(values[10])  # IndexError
#
# Safe access when a list might be empty:

if values:
    print("Safe access to first element:", values[0])
else:
    print("The list is empty.")

# Lists are mutable, so an element can be replaced.

values[0] = 100
print("After changing the first element:", values)

# Modifying an existing index does not insert a new element.
# It replaces the element at that position.


# =============================================================================
# SECTION 4: len(), min(), max(), sum(), sorted(), any(), all()
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 4: BUILT-IN FUNCTIONS")
print("=" * 75)

data = [15, 5, 25, 10, 20]

print("Data:", data)

# len(list)
# Returns the number of elements.

print("len():", len(data))

# min(list)
# Returns the smallest element.

print("min():", min(data))

# max(list)
# Returns the largest element.

print("max():", max(data))

# sum(list)
# Returns the sum of numeric elements.

print("sum():", sum(data))

# Average = sum / number of elements.
# Always handle an empty list to avoid division by zero.

if data:
    average = sum(data) / len(data)
    print("Average:", average)

# sorted(list)
# Returns a NEW sorted list.
# It does not modify the original list.

sorted_data = sorted(data)

print("Original after sorted():", data)
print("New sorted list:", sorted_data)

# Reverse sorting.

descending_data = sorted(data, reverse=True)
print("Descending order:", descending_data)

# any(iterable)
# True if at least one element is truthy.

print("any([0, 0, 5]):", any([0, 0, 5]))
print("any([0, 0, 0]):", any([0, 0, 0]))

# all(iterable)
# True if every element is truthy.
# For an empty iterable, all() returns True.

print("all([1, 2, 3]):", all([1, 2, 3]))
print("all([1, 0, 3]):", all([1, 0, 3]))
print("all([]):", all([]))

# IMPORTANT:
# min(), max(), and sorted() need elements that can be compared.
# For example, mixing integers and strings generally raises TypeError.
#
# min([]) and max([]) raise ValueError.
# sum() is intended primarily for numeric values.


# =============================================================================
# SECTION 5: LIST SLICING
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 5: SLICING")
print("=" * 75)

items = [10, 20, 30, 40, 50, 60, 70]

print("Original:", items)

# General syntax:
#
# list[start:stop:step]
#
# start: index where slicing begins; included.
# stop:  index where slicing ends; excluded.
# step:  interval between selected elements.

print("First three:", items[0:3])
print("First three, shortened:", items[:3])

print("From index 2 onward:", items[2:])
print("From index 1 to 4:", items[1:5])

# Negative slicing.

print("Last three:", items[-3:])
print("Everything except the last two:", items[:-2])

# Step slicing.

print("Every second element:", items[::2])
print("Every second element from index 1:", items[1::2])

# Reverse a list using slicing.

print("Reversed copy:", items[::-1])

# A slice produces a new list.
# Changing the slice does not replace elements in the original list.

part = items[1:4]
part[0] = 999

print("Modified slice:", part)
print("Original remains unchanged:", items)

# Slice assignment modifies the original list.

items[1:3] = [200, 300]
print("After slice assignment:", items)

# Deleting a slice.

del items[1:3]
print("After deleting a slice:", items)

# Slicing is useful for:
# - Extracting a sublist
# - Reversing a sequence
# - Copying a list
# - Dividing data into portions
# - Implementing some DSA algorithms


# =============================================================================
# SECTION 6: append(), extend(), insert()
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 6: ADDING ELEMENTS")
print("=" * 75)

# ---------------------------------------------------------------------------
# 6.1 append()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.append(element)
#
# Adds ONE element to the end of the list.
# Returns None.

numbers = [10, 20, 30]

result = numbers.append(40)

print("After append(40):", numbers)
print("Return value of append():", result)

# Appending another list adds that entire list as ONE element.

numbers.append([50, 60])

print("After appending a list:", numbers)

# The nested list is a single element of the outer list.

print("Last element:", numbers[-1])


# ---------------------------------------------------------------------------
# 6.2 extend()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.extend(iterable)
#
# Adds each element of an iterable to the end.
# Returns None.

numbers = [10, 20, 30]

numbers.extend([40, 50])

print("After extend([40, 50]):", numbers)

# Compare append() and extend().

a = [1, 2]
b = [1, 2]

a.append([3, 4])
b.extend([3, 4])

print("Using append():", a)
print("Using extend():", b)

# append([3, 4]) -> [1, 2, [3, 4]]
# extend([3, 4]) -> [1, 2, 3, 4]

# extend() also accepts other iterables.

letters = ["A", "B"]
letters.extend("CD")

print("Extending with a string:", letters)

# Be careful: a string is an iterable of characters.


# ---------------------------------------------------------------------------
# 6.3 insert()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.insert(index, element)
#
# Inserts an element at a specified position.
# Existing elements at that position and beyond shift right.

numbers = [10, 20, 30]

numbers.insert(1, 15)

print("After insert(1, 15):", numbers)

numbers.insert(0, 5)

print("After inserting at the beginning:", numbers)

numbers.insert(len(numbers), 40)

print("After inserting at the end:", numbers)

# An index larger than the list length inserts at the end.
# Negative indices are also accepted, with insertion positions
# adjusted according to Python's list.insert() rules.

numbers.insert(100, 50)

print("After insert(100, 50):", numbers)


# =============================================================================
# SECTION 7: remove(), pop(), clear()
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 7: REMOVING ELEMENTS")
print("=" * 75)

# ---------------------------------------------------------------------------
# 7.1 remove()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.remove(value)
#
# Removes the FIRST occurrence of a value.
# Returns None.
# Raises ValueError if the value is not present.

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print("After remove(20):", numbers)

# Only the first occurrence of 20 was removed.

# Safe removal when the value may not exist.

target = 100

if target in numbers:
    numbers.remove(target)
else:
    print(target, "is not present; nothing removed.")


# ---------------------------------------------------------------------------
# 7.2 pop()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.pop()
# list.pop(index)
#
# Removes and RETURNS an element.
# Without an index, removes the last element.
# With an index, removes the element at that position.
# Raises IndexError when called on an empty list without a valid index.

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("Removed last element:", removed)
print("List after pop():", numbers)

removed = numbers.pop(1)

print("Removed element at index 1:", removed)
print("List after pop(1):", numbers)

# Safe pop when the list may be empty.

if numbers:
    print("Safely removed:", numbers.pop())
else:
    print("Cannot pop from an empty list.")


# ---------------------------------------------------------------------------
# 7.3 clear()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.clear()
#
# Removes all elements from the existing list.
# Returns None.
# The list object itself still exists.

numbers = [10, 20, 30]

numbers.clear()

print("After clear():", numbers)
print("Length after clear():", len(numbers))


# =============================================================================
# SECTION 8: index() AND count()
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 8: SEARCHING WITH index() AND count()")
print("=" * 75)

numbers = [10, 20, 30, 20, 40, 20]

# ---------------------------------------------------------------------------
# 8.1 index()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.index(value)
# list.index(value, start)
# list.index(value, start, stop)
#
# Returns the index of the FIRST matching value.
# Raises ValueError if the value is not found.

print("List:", numbers)

print("Index of 30:", numbers.index(30))
print("First index of 20:", numbers.index(20))

# Search within a specified range.

print("Index of 20 starting at index 2:", numbers.index(20, 2))

# Safe index search.

target = 100

if target in numbers:
    print("Target index:", numbers.index(target))
else:
    print("Target not found.")


# ---------------------------------------------------------------------------
# 8.2 count()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.count(value)
#
# Returns the number of occurrences of a value.
# Returns 0 when the value is not present.

print("Count of 20:", numbers.count(20))
print("Count of 10:", numbers.count(10))
print("Count of 100:", numbers.count(100))


# =============================================================================
# SECTION 9: sort() AND reverse()
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 9: SORTING AND REVERSING")
print("=" * 75)

numbers = [50, 10, 40, 20, 30]

# ---------------------------------------------------------------------------
# 9.1 sort()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.sort()
# list.sort(reverse=True)
#
# Sorts the existing list in place.
# Returns None.

numbers.sort()

print("Ascending order:", numbers)

numbers.sort(reverse=True)

print("Descending order:", numbers)

# sort() can also use a key function.

words = ["banana", "kiwi", "apple", "watermelon"]

words.sort(key=len)

print("Sorted by word length:", words)

# Sorting by length in descending order.

words.sort(key=len, reverse=True)

print("Length descending:", words)

# IMPORTANT:
# list.sort() modifies the original list.
# sorted(list) returns a new list.
#
# Do not write:
# numbers = numbers.sort()
#
# This assigns None to numbers because sort() returns None.


# ---------------------------------------------------------------------------
# 9.2 reverse()
# ---------------------------------------------------------------------------
#
# Syntax:
# list.reverse()
#
# Reverses the order of elements in place.
# Does NOT sort the elements.
# Returns None.

numbers = [10, 40, 20, 30]

numbers.reverse()

print("After reverse():", numbers)

# To reverse a sorted list:
# 1. Sort it.
# 2. Reverse it.
#
# Or use:
# sorted(numbers, reverse=True)
#
# Or use:
# numbers[::-1]  # Creates a new list.


# =============================================================================
# SECTION 10: copy(), ALIASES, AND id()
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 10: COPYING AND MEMORY REFERENCES")
print("=" * 75)

# ---------------------------------------------------------------------------
# 10.1 Assignment creates an alias, not a copy
# ---------------------------------------------------------------------------

original = [10, 20, 30]
alias = original

print("Original:", original)
print("Alias:", alias)

print("Same object?", original is alias)
print("Original object ID:", id(original))
print("Alias object ID:", id(alias))

alias[0] = 999

print("Original after modifying alias:", original)
print("Alias after modification:", alias)

# Both names refer to the SAME list object.
# Therefore, changes through one name are visible through the other.


# ---------------------------------------------------------------------------
# 10.2 copy()
# ---------------------------------------------------------------------------
#
# Syntax:
# new_list = old_list.copy()
#
# Creates a SHALLOW COPY.
# The outer list is a new object.

original = [10, 20, 30]
copied = original.copy()

print("Original:", original)
print("Copied:", copied)
print("Same outer object?", original is copied)

copied[0] = 500

print("Original after changing copy:", original)
print("Copied after modification:", copied)

# A shallow copy is sufficient for a list of immutable elements
# when you only need to change or replace the outer list's elements.


# ---------------------------------------------------------------------------
# 10.3 Other ways to make a shallow copy
# ---------------------------------------------------------------------------

a = [1, 2, 3]

b = a.copy()
c = a[:]
d = list(a)

print("copy():", b)
print("Slicing:", c)
print("list():", d)


# ---------------------------------------------------------------------------
# 10.4 Shallow copy with nested lists
# ---------------------------------------------------------------------------

original = [[1, 2], [3, 4]]
copied = original.copy()

print("Original nested list:", original)
print("Copied nested list:", copied)

# The outer lists differ, but the inner lists are shared.

print("Same outer list?", original is copied)
print("Same first inner list?", original[0] is copied[0])

copied[0][0] = 999

print("Original after nested modification:", original)
print("Copied after nested modification:", copied)

# Both outer lists show the nested change because the inner list
# is shared between them.


# ---------------------------------------------------------------------------
# 10.5 Deep copy
# ---------------------------------------------------------------------------

import copy

original = [[1, 2], [3, 4]]

deep_copied = copy.deepcopy(original)

deep_copied[0][0] = 999

print("Original after deep-copy modification:", original)
print("Deep copy after modification:", deep_copied)

# deepcopy() recursively copies nested objects in common cases.
# It is useful when independent copies of nested mutable structures
# are required. Some custom objects may have special copying behaviour.


# ---------------------------------------------------------------------------
# 10.6 What does id() mean?
# ---------------------------------------------------------------------------

a = [1, 2, 3]
b = a
c = a.copy()

print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))

# id() returns an identity value that uniquely identifies an object
# during that object's lifetime.
#
# In CPython, id() is commonly the object's memory address.
# Python does NOT guarantee that id() is always a physical memory
# address on every implementation.
#
# If two variables refer to the same object:
#     a is b  -> True
#
# If two separate lists have the same contents:
#     a == c  -> True
#     a is c  -> False


# =============================================================================
# SECTION 11: CONCATENATION, REPETITION, AND MEMBERSHIP
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 11: LIST OPERATORS")
print("=" * 75)

# ---------------------------------------------------------------------------
# 11.1 Concatenation using +
# ---------------------------------------------------------------------------

a = [1, 2, 3]
b = [4, 5, 6]

combined = a + b

print("Concatenated:", combined)
print("Original a:", a)
print("Original b:", b)

# + creates a new list rather than modifying either operand.


# ---------------------------------------------------------------------------
# 11.2 Repetition using *
# ---------------------------------------------------------------------------

repeated = [1, 2] * 3

print("Repeated list:", repeated)

# CAUTION with nested lists:
#
# This creates several references to the SAME inner list.

bad_matrix = [[0] * 3] * 2

bad_matrix[0][0] = 99

print("Repeated-reference matrix:", bad_matrix)

# Both rows change because they reference the same inner list.


# Correct way to create independent rows:

good_matrix = [[0] * 3 for _ in range(2)]

good_matrix[0][0] = 99

print("Independent-row matrix:", good_matrix)


# ---------------------------------------------------------------------------
# 11.3 Membership using in and not in
# ---------------------------------------------------------------------------

numbers = [10, 20, 30, 40]

print("20 in numbers:", 20 in numbers)
print("100 in numbers:", 100 in numbers)
print("100 not in numbers:", 100 not in numbers)

# Membership testing on a list takes O(n) time in the worst case.
# Python may need to compare the target with each element.


# =============================================================================
# SECTION 12: ITERATION AND TRAVERSAL
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 12: ITERATING THROUGH A LIST")
print("=" * 75)

numbers = [10, 20, 30, 40, 50]

# ---------------------------------------------------------------------------
# 12.1 Direct iteration
# ---------------------------------------------------------------------------

print("Direct iteration:")

for value in numbers:
    print(value)


# ---------------------------------------------------------------------------
# 12.2 Iteration using an index
# ---------------------------------------------------------------------------

print("Index-based iteration:")

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])


# ---------------------------------------------------------------------------
# 12.3 enumerate()
# ---------------------------------------------------------------------------

print("Iteration using enumerate():")

for index, value in enumerate(numbers):
    print(index, "->", value)


# ---------------------------------------------------------------------------
# 12.4 Traversal with a condition
# ---------------------------------------------------------------------------

print("Even numbers:")

for value in numbers:
    if value % 2 == 0:
        print(value)


# ---------------------------------------------------------------------------
# 12.5 Searching through traversal
# ---------------------------------------------------------------------------

target = 30
found = False

for value in numbers:
    if value == target:
        found = True
        break

print("Target found?", found)

# Traversal is one of the most fundamental DSA operations.
# It means visiting the elements of a data structure systematically.


# =============================================================================
# SECTION 13: LIST COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 13: LIST COMPREHENSIONS")
print("=" * 75)

# General syntax:
#
# [expression for item in iterable]
#
# With a condition:
#
# [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6]

# 1. Generate squares.

squares = [x ** 2 for x in numbers]

print("Squares:", squares)

# Equivalent ordinary loop:

squares_loop = []

for x in numbers:
    squares_loop.append(x ** 2)

print("Squares using a loop:", squares_loop)

# 2. Filter even numbers.

evens = [x for x in numbers if x % 2 == 0]

print("Even numbers:", evens)

# 3. Transform and filter.

even_squares = [x ** 2 for x in numbers if x % 2 == 0]

print("Squares of even numbers:", even_squares)

# 4. Convert words to uppercase.

words = ["python", "list", "dsa"]

uppercase_words = [word.upper() for word in words]

print("Uppercase:", uppercase_words)

# 5. Conditional expression.

labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print("Parity:", labels)

# Comprehensions are concise, but ordinary loops may be easier
# to read when the logic is complicated.


# =============================================================================
# SECTION 14: NESTED LISTS AND 2D LISTS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 14: NESTED LISTS AND MATRICES")
print("=" * 75)

# A nested list contains other lists.
# A two-dimensional list can represent a matrix or table.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")

for row in matrix:
    print(row)

# Access a specific element.
#
# matrix[row_index][column_index]

print("Element at row 0, column 1:", matrix[0][1])
print("Element at row 2, column 2:", matrix[2][2])

# Modify an element.

matrix[1][1] = 500

print("After modification:")

for row in matrix:
    print(row)

# Traverse every element.

print("All matrix elements:")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")

    print()

# Create a 3 x 4 matrix of zeros.

rows = 3
columns = 4

zero_matrix = [[0 for _ in range(columns)] for _ in range(rows)]

print("3 x 4 zero matrix:")

for row in zero_matrix:
    print(row)

# The comprehension creates independent rows.
# This is safer than [[0] * columns] * rows when rows will be modified.


# =============================================================================
# SECTION 15: LISTS AND MEMORY REFERENCES
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 15: MEMORY AND REFERENCES")
print("=" * 75)

# Python variables are names bound to objects.
# A list variable does not simply contain a separate copy of every value
# in the way a beginner might imagine.

a = [10, 20, 30]

# b becomes another reference to the same list.

b = a

print("a is b:", a is b)

# Replacing an element mutates the shared list.

b[0] = 999

print("a:", a)
print("b:", b)

# Rebinding a name is different from mutating the object.

b = [1, 2, 3]

print("After rebinding b:")
print("a:", a)
print("b:", b)
print("a is b:", a is b)

# Now b refers to a different list.
# Rebinding b did not replace a's list.

# Python manages memory automatically.
# Do not use id() to perform pointer arithmetic or manipulate memory.


# =============================================================================
# SECTION 16: DSA ALGORITHMS USING LISTS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 16: DSA ALGORITHMS")
print("=" * 75)


# ---------------------------------------------------------------------------
# 16.1 LINEAR SEARCH
# ---------------------------------------------------------------------------
#
# Problem:
# Find the position of a target value.
#
# Approach:
# Visit elements one by one until the target is found.
#
# Time complexity:
# Best case:  O(1)
# Worst case: O(n)
#
# Auxiliary space: O(1)

def linear_search(arr, target):
    """
    Return the index of the first occurrence of target.
    Return -1 if target is not found.
    """

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


data = [15, 25, 35, 45, 55]

print("Linear search result:", linear_search(data, 35))
print("Missing target result:", linear_search(data, 100))


# ---------------------------------------------------------------------------
# 16.2 FIND MINIMUM AND MAXIMUM WITHOUT min() OR max()
# ---------------------------------------------------------------------------
#
# Time complexity: O(n)
# Auxiliary space: O(1)

def find_min_max(arr):
    """
    Return (minimum, maximum) using one traversal.
    Return None for an empty list.
    """

    if not arr:
        return None

    smallest = arr[0]
    largest = arr[0]

    for value in arr[1:]:
        if value < smallest:
            smallest = value

        if value > largest:
            largest = value

    return smallest, largest


data = [35, 12, 78, 4, 56]

print("Minimum and maximum:", find_min_max(data))


# ---------------------------------------------------------------------------
# 16.3 COUNT ELEMENTS WITHOUT count()
# ---------------------------------------------------------------------------
#
# Time complexity: O(n)
# Auxiliary space: O(1)

def count_occurrences(arr, target):
    """Count how many times target occurs in arr."""

    count = 0

    for value in arr:
        if value == target:
            count += 1

    return count


data = [1, 2, 2, 3, 2, 4, 2]

print("Occurrences of 2:", count_occurrences(data, 2))


# ---------------------------------------------------------------------------
# 16.4 REVERSE A LIST IN PLACE
# ---------------------------------------------------------------------------
#
# Two-pointer technique:
# - One pointer starts at the beginning.
# - Another starts at the end.
# - Swap elements and move inward.
#
# Time complexity: O(n)
# Auxiliary space: O(1)

def reverse_in_place(arr):
    """Reverse the list without creating another list."""

    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    # The input list has been modified.
    # No return statement is necessary.


data = [10, 20, 30, 40, 50]

reverse_in_place(data)

print("Reversed in place:", data)


# ---------------------------------------------------------------------------
# 16.5 REMOVE DUPLICATES WHILE PRESERVING ORDER
# ---------------------------------------------------------------------------
#
# This version uses a set for efficient membership checks.
# It works when the elements are hashable, such as integers and strings.
#
# Expected time complexity: O(n)
# Auxiliary space: O(n)

def remove_duplicates(arr):
    """Return unique elements in their original order."""

    result = []
    seen = set()

    for value in arr:
        if value not in seen:
            result.append(value)
            seen.add(value)

    return result


data = [1, 2, 2, 3, 1, 4, 3, 5]

print("Without duplicates:", remove_duplicates(data))

# If the list contains unhashable elements, such as lists or dictionaries,
# this set-based approach will not work directly.


# ---------------------------------------------------------------------------
# 16.6 FREQUENCY COUNTING
# ---------------------------------------------------------------------------
#
# A dictionary stores each distinct value and its frequency.
#
# Expected time complexity: O(n) for ordinary hashable elements.

def frequency_count(arr):
    """Return a dictionary mapping each value to its frequency."""

    frequency = {}

    for value in arr:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    return frequency


data = [1, 2, 2, 3, 1, 2, 4, 3]

print("Frequency dictionary:", frequency_count(data))


# ---------------------------------------------------------------------------
# 16.7 SECOND-LARGEST DISTINCT ELEMENT
# ---------------------------------------------------------------------------
#
# This version finds the second-largest DISTINCT value.
# It does not sort the entire list.
#
# Time complexity: O(n)
# Auxiliary space: O(1)

def second_largest(arr):
    """
    Return the second-largest distinct value.
    Return None if fewer than two distinct values exist.
    """

    largest = None
    second = None

    for value in arr:

        if largest is None or value > largest:
            second = largest
            largest = value

        elif value != largest and (second is None or value > second):
            second = value

    return second


print("Second largest:", second_largest([10, 50, 30, 50, 40]))
print("Second largest with duplicates:", second_largest([5, 5, 5]))
print("Second largest with negatives:", second_largest([-10, -5, -20]))


# ---------------------------------------------------------------------------
# 16.8 CHECK WHETHER A LIST IS SORTED
# ---------------------------------------------------------------------------
#
# Time complexity: O(n)
# Auxiliary space: O(1)

def is_sorted(arr):
    """Return True if arr is in non-decreasing order."""

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False

    return True


print("Is [1, 2, 3, 4] sorted?", is_sorted([1, 2, 3, 4]))
print("Is [1, 3, 2, 4] sorted?", is_sorted([1, 3, 2, 4]))


# ---------------------------------------------------------------------------
# 16.9 BINARY SEARCH
# ---------------------------------------------------------------------------
#
# IMPORTANT:
# Binary search requires a sorted list.
#
# At each step, half of the remaining search interval is discarded.
#
# Time complexity: O(log n)
# Auxiliary space: O(1) for this iterative implementation.

def binary_search(arr, target):
    """
    Search for target in an ascending sorted list.
    Return its index or -1 if not found.
    """

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


sorted_numbers = [10, 20, 30, 40, 50, 60, 70]

print("Binary search for 40:", binary_search(sorted_numbers, 40))
print("Binary search for 25:", binary_search(sorted_numbers, 25))


# ---------------------------------------------------------------------------
# 16.10 TWO-SUM: FIND TWO INDICES WHOSE VALUES ADD TO A TARGET
# ---------------------------------------------------------------------------
#
# Example:
# arr = [2, 7, 11, 15]
# target = 9
# Answer = (0, 1), because 2 + 7 = 9.
#
# Expected time complexity: O(n)
# Auxiliary space: O(n)

def two_sum(arr, target):
    """
    Return indices of two distinct elements that sum to target.
    Return None if no solution is found.
    """

    seen = {}

    for i, value in enumerate(arr):

        needed = target - value

        if needed in seen:
            return seen[needed], i

        # Store the first index for each value.
        if value not in seen:
            seen[value] = i

    return None


data = [2, 7, 11, 15]

print("Two-sum indices:", two_sum(data, 9))
print("Two-sum when absent:", two_sum(data, 100))


# =============================================================================
# SECTION 17: TIME COMPLEXITY OF PYTHON LIST OPERATIONS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 17: TIME COMPLEXITY")
print("=" * 75)

# n = number of elements in the list.
#
# O(1)       -> Constant time
# O(log n)   -> Logarithmic time
# O(n)       -> Linear time
# O(n log n) -> Common efficient comparison-sorting time
#
# The following table describes typical CPython list behaviour.
#
# OPERATION                         TYPICAL TIME COMPLEXITY
# ---------------------------------------------------------------------------
# len(arr)                          O(1)
# arr[i]                            O(1)
# arr[i] = value                    O(1)
# arr.append(value)                 O(1) amortized
# arr.pop()                         O(1) amortized
# arr.pop(0)                        O(n)
# arr.insert(0, value)              O(n)
# arr.insert(i, value)              O(n) in general
# arr.remove(value)                 O(n)
# arr.index(value)                  O(n)
# arr.count(value)                  O(n)
# value in arr                      O(n) in the worst case
# min(arr)                          O(n)
# max(arr)                          O(n)
# sum(arr)                          O(n)
# arr.reverse()                     O(n)
# arr.copy()                        O(n)
# arr[:]                            O(n)
# sorted(arr)                       O(n log n) worst case
# arr.sort()                        O(n log n) worst case
# Linear search                     O(n)
# Binary search on sorted list      O(log n)
#
# Important qualifications:
#
# 1. append() is amortized O(1), not necessarily O(1) for every append.
#    Occasional resizing can take O(n).
#
# 2. Inserting or deleting near the beginning requires shifting elements.
#
# 3. Inserting near the middle is O(n) in the general case.
#
# 4. Binary search is O(log n), but sorting an unsorted list first
#    costs O(n log n). Whether that is worthwhile depends on the problem.
#
# 5. Complexity describes how work grows with input size; it is not
#    an exact measurement of elapsed time.
#
# 6. These are typical complexities for Python's built-in list
#    implementation, not universal guarantees for every Python runtime.


# =============================================================================
# SECTION 18: ADVANTAGES AND DISADVANTAGES OF LISTS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 18: ADVANTAGES AND DISADVANTAGES")
print("=" * 75)

# ADVANTAGES:
#
# 1. Ordered:
#    Elements preserve their sequence.
#
# 2. Mutable:
#    Elements can be changed, added, and removed.
#
# 3. Dynamic:
#    Lists can grow and shrink.
#
# 4. Indexed access:
#    Reading an element by index is O(1).
#
# 5. Flexible:
#    Lists can hold different Python object types.
#
# 6. Rich built-in operations:
#    Python provides many useful methods and functions.
#
# 7. Useful for DSA:
#    Lists are convenient for arrays, stacks, heaps, dynamic programming,
#    adjacency lists, and many other algorithms.
#
#
# DISADVANTAGES:
#
# 1. Insertion at the beginning or middle is generally O(n).
#
# 2. Searching by value is O(n) in the worst case.
#
# 3. A Python list stores references to Python objects, so its memory
#    overhead can be higher than that of a compact numeric array.
#
# 4. A list can contain mixed types, which may make data processing
#    less predictable.
#
# 5. A shallow copy does not independently copy nested mutable objects.
#
# 6. Lists are not ideal for every workload:
#    - Frequent membership tests may favour a set.
#    - Frequent removal from both ends may favour collections.deque.
#    - Large homogeneous numeric arrays may favour array or NumPy.
#
# 7. Python lists do not enforce a fixed size or a single element type.
#
# A list is often the right default for general-purpose sequences,
# but the best structure depends on the operations your algorithm needs.


# =============================================================================
# SECTION 19: COMMON MISTAKES
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 19: COMMON MISTAKES")
print("=" * 75)


# ---------------------------------------------------------------------------
# MISTAKE 1: Assigning the result of append()
# ---------------------------------------------------------------------------

numbers = [1, 2, 3]

result = numbers.append(4)

print("Correct list after append:", numbers)
print("append() return value:", result)

# WRONG:
# numbers = numbers.append(4)
#
# append() returns None, so this would replace numbers with None.


# ---------------------------------------------------------------------------
# MISTAKE 2: Confusing append() and extend()
# ---------------------------------------------------------------------------

a = [1, 2]
a.append([3, 4])

print("append():", a)

b = [1, 2]
b.extend([3, 4])

print("extend():", b)


# ---------------------------------------------------------------------------
# MISTAKE 3: Confusing remove() and pop()
# ---------------------------------------------------------------------------

numbers = [10, 20, 30, 20]

numbers.remove(20)

print("remove(value):", numbers)

removed = numbers.pop(1)

print("pop(index) removed:", removed)
print("List after pop:", numbers)


# ---------------------------------------------------------------------------
# MISTAKE 4: Modifying a list while iterating over it
# ---------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

# Avoid doing this:
#
# for value in numbers:
#     if value % 2 == 0:
#         numbers.remove(value)
#
# Removing elements shifts later elements and can cause some values
# to be skipped during iteration.

# Better: create a new filtered list.

numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = [value for value in numbers if value % 2 != 0]

print("Original:", numbers)
print("Odd numbers:", odd_numbers)

# If you need to modify the original list in place:

numbers[:] = [value for value in numbers if value % 2 != 0]

print("Original modified in place:", numbers)


# ---------------------------------------------------------------------------
# MISTAKE 5: Shallow copy versus deep copy
# ---------------------------------------------------------------------------

original = [[1, 2], [3, 4]]
copied = original.copy()

copied[0][0] = 999

print("Original after shallow-copy change:", original)

# Remember:
# copied = original.copy()       -> shallow copy
# copied = copy.deepcopy(original) -> deep copy


# ---------------------------------------------------------------------------
# MISTAKE 6: Accessing an empty list
# ---------------------------------------------------------------------------

empty = []

# WRONG:
# print(empty[0])
# This raises IndexError.

if empty:
    print(empty[0])
else:
    print("Cannot access index 0: the list is empty.")


# ---------------------------------------------------------------------------
# MISTAKE 7: sort() versus sorted()
# ---------------------------------------------------------------------------

numbers = [4, 1, 3, 2]

new_sorted_list = sorted(numbers)

print("Original:", numbers)
print("sorted() result:", new_sorted_list)

sort_result = numbers.sort()

print("Original after sort():", numbers)
print("sort() return value:", sort_result)


# ---------------------------------------------------------------------------
# MISTAKE 8: Using == and is interchangeably
# ---------------------------------------------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)  # Same contents
print("a is b:", a is b)  # Different list objects
print("a is c:", a is c)  # Same object

# Use == to compare values.
# Use is to test object identity.


# =============================================================================
# SECTION 20: PRACTICE PROBLEMS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 20: PRACTICE PROBLEMS")
print("=" * 75)

# Try solving these without looking at the answers first.
#
# PROBLEM 1:
# Given [10, 20, 30, 40, 50], print the first and last elements.
#
# PROBLEM 2:
# Given [1, 2, 3, 4, 5], create a list of squares.
#
# PROBLEM 3:
# Count how many times 7 appears in [7, 2, 7, 4, 7, 5].
#
# PROBLEM 4:
# Find the largest number in [12, 45, 7, 89, 23].
#
# PROBLEM 5:
# Reverse [10, 20, 30, 40] in place.
#
# PROBLEM 6:
# Remove duplicates from [1, 2, 2, 3, 3, 4].
#
# PROBLEM 7:
# Find the second-largest distinct value in [10, 50, 20, 50, 40].
#
# PROBLEM 8:
# Check whether [1, 2, 3, 4, 5] is sorted.
#
# PROBLEM 9:
# Use binary search to find 30 in [10, 20, 30, 40, 50].
#
# PROBLEM 10:
# Find two indices in [2, 7, 11, 15] whose values add up to 9.
#
# PROBLEM 11:
# Explain the difference between append(), extend(), and insert().
#
# PROBLEM 12:
# Explain the difference between remove(), pop(), and clear().
#
# PROBLEM 13:
# Explain the difference between copy() and assignment.
#
# PROBLEM 14:
# Why is inserting an element at index 0 generally O(n)?
#
# PROBLEM 15:
# Why is binary search not directly applicable to an unsorted list?


# =============================================================================
# SECTION 21: QUICK REVISION SUMMARY
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 21: QUICK REVISION SUMMARY")
print("=" * 75)

# METHOD / FUNCTION             PURPOSE
# ---------------------------------------------------------------------------
# len(arr)                      Number of elements
# arr[i]                        Access an element
# arr[a:b:c]                    Extract a slice
# min(arr)                      Smallest element
# max(arr)                      Largest element
# sum(arr)                      Sum of numeric elements
# sorted(arr)                   Return a new sorted list
# arr.append(x)                 Add one element at the end
# arr.extend(iterable)          Add elements from an iterable
# arr.insert(i, x)              Insert an element at a position
# arr.remove(x)                 Remove the first matching value
# arr.pop()                     Remove and return the last element
# arr.pop(i)                    Remove and return the element at i
# arr.clear()                   Remove all elements
# arr.index(x)                  First matching index
# arr.count(x)                  Number of occurrences
# arr.sort()                    Sort the original list
# arr.reverse()                 Reverse the original list
# arr.copy()                    Shallow copy
# id(arr)                       Object identity value
# x in arr                      Membership test
# arr1 + arr2                   Concatenation
# arr * n                       Repetition
# arr[::-1]                     Reversed copy
# enumerate(arr)                Iterate with indices and values
# [f(x) for x in arr]           List comprehension
#
# IMPORTANT DISTINCTIONS:
#
# append(x)  -> Adds x as one element.
# extend(xs) -> Adds each element from xs.
# insert(i,x)-> Inserts x at position i.
#
# remove(x)  -> Removes by value.
# pop(i)     -> Removes by index and returns the removed element.
# clear()    -> Removes all elements.
#
# sort()     -> Modifies the original list; returns None.
# sorted()   -> Returns a new sorted list.
#
# reverse()  -> Reverses the original list; returns None.
# [::-1]     -> Creates a reversed shallow copy.
#
# b = a      -> Creates another reference to the same list.
# b = a.copy()-> Creates a shallow copy of the outer list.
#
# Linear search  -> O(n)
# Binary search  -> O(log n), provided the list is sorted.
#
# append()       -> Amortized O(1)
# pop()          -> O(1) amortized for the last element
# pop(0)         -> O(n)
# insert(0, x)   -> O(n)
#
# Lists are ordered, mutable, indexed, dynamic, and allow duplicates.


print("\n" + "=" * 75)
print("END OF PYTHON LISTS: COMPLETE DSA REVISION")
print("=" * 75)

print("\nRevision complete!")
print("Next step: Modify the examples and solve the practice problems.")