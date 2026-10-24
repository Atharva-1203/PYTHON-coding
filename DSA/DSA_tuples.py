
"""
===============================================================================
                    PYTHON TUPLES: COMPLETE DSA REVISION
===============================================================================

Purpose:
    A systematic revision of Python tuples, from basic syntax to DSA.

Requirements:
    Python 3.x

How to run:
    python python_tuples_dsa.py

Topics:
    1. Tuple fundamentals and properties
    2. Creating tuples
    3. Indexing and accessing elements
    4. Built-in functions
    5. Slicing
    6. count() and index()
    7. Tuple operators
    8. Tuple unpacking
    9. Immutability
    10. Mutable objects inside tuples
    11. References, identity, and memory
    12. Nested tuples
    13. Tuples versus lists
    14. Returning multiple values
    15. Tuples in dictionaries and sets
    16. DSA applications
    17. Time and space complexity
    18. Common mistakes
    19. Practice problems

===============================================================================
"""


# =============================================================================
# SECTION 1: WHAT IS A TUPLE?
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 1: INTRODUCTION TO TUPLES")
print("=" * 75)

# A tuple is an ordered collection of elements.
# Unlike a list, a tuple cannot have its elements added, removed, or
# replaced through ordinary item assignment after it has been created.

student = ("Atharva", 19, "Electronics", 9.25)

print("Student tuple:", student)
print("Type:", type(student))

# IMPORTANT PROPERTIES:
#
# 1. Ordered:
#    Elements preserve their sequence.
#
# 2. Immutable:
#    Existing tuple elements cannot be reassigned.
#
# 3. Indexed:
#    Elements can be accessed using positive and negative indices.
#
# 4. Duplicates allowed:
#    The same value can appear multiple times.
#
# 5. Heterogeneous:
#    Different data types can be stored together.
#
# 6. Can contain nested collections:
#    A tuple can contain other tuples, lists, dictionaries, etc.
#
# 7. Supports iteration:
#    Elements can be processed using loops.
#
# 8. Does not provide list-style mutating methods:
#    For example, tuples have no append(), extend(), remove(), or pop().


# =============================================================================
# SECTION 2: CREATING TUPLES
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 2: CREATING TUPLES")
print("=" * 75)

# 1. Tuple using parentheses.

numbers = (10, 20, 30, 40)
print("Ordinary tuple:", numbers)

# 2. Empty tuple.

empty_tuple = ()
print("Empty tuple:", empty_tuple)
print("Empty tuple type:", type(empty_tuple))

# Another way to create an empty tuple.

empty_tuple_2 = tuple()
print("Using tuple():", empty_tuple_2)

# 3. Single-element tuple.
#
# IMPORTANT:
# The comma creates the tuple, not the parentheses alone.

single = (10,)
print("Single-element tuple:", single)
print("Type:", type(single))

# Without the comma, this is an integer, not a tuple.

not_a_tuple = (10)
print("Without comma:", not_a_tuple)
print("Type:", type(not_a_tuple))

# Correct single-element tuples with other values.

one_string = ("Python",)
one_boolean = (True,)

print(one_string)
print(one_boolean)

# 4. Parentheses are optional in many tuple assignments.

tuple_without_parentheses = 10, 20, 30

print("Without parentheses:", tuple_without_parentheses)
print("Type:", type(tuple_without_parentheses))

# 5. Creating a tuple from a list.

from_list = tuple([1, 2, 3, 4])

print("From list:", from_list)

# 6. Creating a tuple from a string.

from_string = tuple("PYTHON")

print("From string:", from_string)

# 7. Creating a tuple from a range.

from_range = tuple(range(1, 6))

print("From range:", from_range)

# 8. Tuple containing mixed types.

mixed = (10, 3.14, "Python", True)

print("Mixed tuple:", mixed)

# 9. Tuple containing another tuple.

nested = ((1, 2), (3, 4))

print("Nested tuple:", nested)


# =============================================================================
# SECTION 3: INDEXING AND ACCESSING ELEMENTS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 3: INDEXING")
print("=" * 75)

values = (10, 20, 30, 40, 50)

# Positive indices:
#
# Element:  10   20   30   40   50
# Index:     0    1    2    3    4
#
# Negative indices:
#
# Element: -5   -4   -3   -2   -1

print("Tuple:", values)

print("First element:", values[0])
print("Second element:", values[1])
print("Last element:", values[-1])
print("Second-last element:", values[-2])

print("Length:", len(values))
print("Last positive index:", len(values) - 1)

# Tuples support indexing just like lists.

# Accessing an invalid index raises IndexError.
#
# Example:
# print(values[10])

# Safe access.

if values:
    print("First element safely accessed:", values[0])
else:
    print("Tuple is empty.")

# IMPORTANT:
# This assignment is NOT allowed:
#
# values[0] = 100
#
# It raises TypeError because tuples do not support item assignment.


# =============================================================================
# SECTION 4: BUILT-IN FUNCTIONS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 4: BUILT-IN FUNCTIONS")
print("=" * 75)

numbers = (15, 5, 25, 10, 20)

print("Tuple:", numbers)

# len(): Number of elements.

print("len():", len(numbers))

# min(): Smallest element.

print("min():", min(numbers))

# max(): Largest element.

print("max():", max(numbers))

# sum(): Sum of numeric elements.

print("sum():", sum(numbers))

# Average.

if numbers:
    average = sum(numbers) / len(numbers)
    print("Average:", average)

# sorted():
# Returns a NEW LIST, not a tuple.

sorted_result = sorted(numbers)

print("Original tuple:", numbers)
print("sorted() result:", sorted_result)
print("Result type:", type(sorted_result))

# Convert the sorted result back into a tuple if needed.

sorted_tuple = tuple(sorted(numbers))

print("Sorted tuple:", sorted_tuple)

# Reverse sorting.

descending = tuple(sorted(numbers, reverse=True))

print("Descending tuple:", descending)

# any():
# True if at least one element is truthy.

print("any((0, 0, 5)):", any((0, 0, 5)))
print("any((0, 0, 0)):", any((0, 0, 0)))

# all():
# True if every element is truthy.
# all(()) is True because there is no false element.

print("all((1, 2, 3)):", all((1, 2, 3)))
print("all((1, 0, 3)):", all((1, 0, 3)))
print("all(()):", all(()))

# IMPORTANT:
# min(), max(), and sorted() require mutually comparable elements.
# sum() is intended primarily for numeric values.
#
# min(()) and max(()) raise ValueError because the tuple is empty.


# =============================================================================
# SECTION 5: TUPLE SLICING
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 5: SLICING")
print("=" * 75)

items = (10, 20, 30, 40, 50, 60, 70)

print("Original:", items)

# Syntax:
#
# tuple[start:stop:step]
#
# start is included.
# stop is excluded.
# step determines the interval.

print("First three:", items[:3])
print("From index 2:", items[2:])
print("Index 1 to 4:", items[1:5])

# Negative slicing.

print("Last three:", items[-3:])
print("Everything except the last two:", items[:-2])

# Step slicing.

print("Every second element:", items[::2])
print("Every second element from index 1:", items[1::2])

# Reverse a tuple using slicing.

reversed_tuple = items[::-1]

print("Reversed tuple:", reversed_tuple)
print("Original remains unchanged:", items)

# Slicing returns a new tuple.
# Since tuples are immutable, slicing cannot be used to modify
# the original tuple.


# =============================================================================
# SECTION 6: count() AND index()
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 6: count() AND index()")
print("=" * 75)

numbers = (10, 20, 30, 20, 40, 20)

print("Tuple:", numbers)

# count(value):
# Returns the number of occurrences of a value.

print("Count of 20:", numbers.count(20))
print("Count of 10:", numbers.count(10))
print("Count of 100:", numbers.count(100))

# index(value):
# Returns the index of the FIRST occurrence.
# Raises ValueError if the value is not found.

print("First index of 20:", numbers.index(20))
print("Index of 30:", numbers.index(30))

# index(value, start)
# Search from a specified starting index.

print("Index of 20 starting from index 2:", numbers.index(20, 2))

# index(value, start, stop)
# Search within a specified range.

print(
    "Index of 20 within the specified range:",
    numbers.index(20, 2, 5)
)

# Safe search.

target = 100

if target in numbers:
    print("Target index:", numbers.index(target))
else:
    print("Target not found.")

# Tuples provide only two built-in data methods:
#
# 1. count()
# 2. index()
#
# They do not provide list-mutating methods such as append() or pop().


# =============================================================================
# SECTION 7: TUPLE OPERATORS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 7: TUPLE OPERATORS")
print("=" * 75)

# ---------------------------------------------------------------------------
# 7.1 Concatenation using +
# ---------------------------------------------------------------------------

a = (1, 2, 3)
b = (4, 5, 6)

combined = a + b

print("Concatenated tuple:", combined)
print("Original a:", a)
print("Original b:", b)

# + creates a new tuple containing the combined elements.


# ---------------------------------------------------------------------------
# 7.2 Repetition using *
# ---------------------------------------------------------------------------

repeated = (1, 2) * 3

print("Repeated tuple:", repeated)

# Repetition repeats the references to the elements.
# If the elements are mutable objects, those objects are not copied.


# ---------------------------------------------------------------------------
# 7.3 Membership using in and not in
# ---------------------------------------------------------------------------

numbers = (10, 20, 30, 40)

print("20 in numbers:", 20 in numbers)
print("100 in numbers:", 100 in numbers)
print("100 not in numbers:", 100 not in numbers)

# Membership testing takes O(n) time in the worst case.


# ---------------------------------------------------------------------------
# 7.4 Comparison
# ---------------------------------------------------------------------------

print("(1, 2) == (1, 2):", (1, 2) == (1, 2))
print("(1, 2) == (1, 3):", (1, 2) == (1, 3))

# Tuples are compared lexicographically.
# Python compares corresponding elements from left to right.
# The first unequal pair determines the result.


# =============================================================================
# SECTION 8: TUPLE UNPACKING
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 8: TUPLE UNPACKING")
print("=" * 75)

student = ("Atharva", 19, "Electronics")

# Unpacking assigns each element to a separate variable.

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# The number of targets must match the number of elements
# unless extended unpacking is used.

# WRONG:
# name, age = student
#
# This raises ValueError because there are three elements.

# ---------------------------------------------------------------------------
# 8.1 Swapping variables
# ---------------------------------------------------------------------------

a = 10
b = 20

a, b = b, a

print("After swapping:")
print("a:", a)
print("b:", b)

# Python evaluates the right-hand side before assigning the values.
# Tuple packing and unpacking make this possible without a temporary
# variable written explicitly.


# ---------------------------------------------------------------------------
# 8.2 Extended unpacking
# ---------------------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)

# The starred target receives a LIST, even though the source is a tuple.

print("Type of middle:", type(middle))


# ---------------------------------------------------------------------------
# 8.3 Unpacking in a loop
# ---------------------------------------------------------------------------

students = (
    ("Aarav", 85),
    ("Riya", 92),
    ("Kabir", 78)
)

for student_name, marks in students:
    print(student_name, "scored", marks)


# =============================================================================
# SECTION 9: TUPLE IMMUTABILITY
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 9: IMMUTABILITY")
print("=" * 75)

numbers = (10, 20, 30)

print("Original tuple:", numbers)

# The following operations are NOT allowed:
#
# numbers[0] = 100       # Item assignment
# numbers.append(40)     # No append() method
# numbers.remove(20)     # No remove() method
# numbers.pop()          # No pop() method
#
# These operations raise errors.

# How can we produce a modified tuple?
#
# Create a new tuple.

numbers = (10, 20, 30)

modified = (100,) + numbers[1:]

print("New tuple:", modified)
print("Original tuple:", numbers)

# The original tuple remains unchanged.
# The name 'modified' refers to a new tuple.


# ---------------------------------------------------------------------------
# 9.1 Deleting a tuple variable
# ---------------------------------------------------------------------------

numbers = (1, 2, 3)

del numbers

# del numbers removes the name binding.
# It does not provide a way to delete an individual tuple element.
#
# Uncommenting the following line would raise NameError:
#
# print(numbers)


# =============================================================================
# SECTION 10: MUTABLE OBJECTS INSIDE TUPLES
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 10: MUTABLE OBJECTS INSIDE TUPLES")
print("=" * 75)

# IMPORTANT CONCEPT:
#
# A tuple is immutable, but an object stored inside it might be mutable.
# Immutability prevents replacing the tuple's element references.
# It does not automatically make nested objects immutable.

data = ([1, 2], [3, 4])

print("Original:", data)

# This is allowed because the inner list is mutable.

data[0].append(99)

print("After modifying an inner list:", data)

# This is NOT allowed:
#
# data[0] = [100, 200]
#
# The assignment tries to replace an element of the tuple.

# A tuple containing a dictionary can also have its dictionary modified.

record = ("Student", {"marks": 90})

record[1]["marks"] = 95

print("Modified nested dictionary:", record)

# However, a tuple is hashable only when its elements are hashable.
# A tuple containing a list or dictionary cannot be used as a dictionary
# key because lists and dictionaries are unhashable.


# =============================================================================
# SECTION 11: REFERENCES, IDENTITY, AND COPYING
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 11: REFERENCES AND IDENTITY")
print("=" * 75)

a = (1, 2, 3)
b = a

print("a:", a)
print("b:", b)

print("a is b:", a is b)
print("a == b:", a == b)

print("id(a):", id(a))
print("id(b):", id(b))

# b = a does not explicitly create a new tuple.
# Both names refer to the same object.

# Because tuples are immutable, there is no need to copy a tuple
# simply to prevent element reassignment through another variable.

# However, nested mutable objects may still be shared.

a = ([1, 2], [3, 4])
b = a

b[0].append(99)

print("a after modifying a shared inner list:", a)
print("b after modifying a shared inner list:", b)

# Shallow copying a tuple can be done using tuple slicing or tuple().
# However, Python may reuse the same tuple object when the input
# is already a tuple. Do not rely on identity changing after copying.

original = (10, 20, 30)
copied = tuple(original)

print("Original:", original)
print("Copied:", copied)
print("Equal values:", original == copied)

# The important concept is immutability, not whether a copy has
# a different id.


# =============================================================================
# SECTION 12: NESTED TUPLES
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 12: NESTED TUPLES")
print("=" * 75)

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Nested tuple:")

for row in matrix:
    print(row)

# Accessing a nested element.

print("Element at row 0, column 1:", matrix[0][1])
print("Element at row 2, column 2:", matrix[2][2])

# Traverse every element.

print("All elements:")

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")

    print()

# Tuples can represent fixed records, coordinates, and immutable
# collections of rows.
#
# A tuple of tuples is not automatically a mathematical matrix.
# It is simply a nested sequence of tuples.


# =============================================================================
# SECTION 13: TUPLES VERSUS LISTS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 13: TUPLES VERSUS LISTS")
print("=" * 75)

# FEATURE                  LIST                 TUPLE
# ---------------------------------------------------------------------------
# Syntax                   [1, 2, 3]             (1, 2, 3)
# Ordered                  Yes                   Yes
# Indexed                  Yes                   Yes
# Mutable                  Yes                   No
# Duplicates               Allowed               Allowed
# Mixed data types         Allowed               Allowed
# append()                 Available             Not available
# remove()                 Available             Not available
# pop()                    Available             Not available
# count()                  Available             Available
# index()                  Available             Available
# Slice result             List                  Tuple
# Hashable                 No                    Sometimes
# Fixed record             Possible              Often suitable
# Dynamic sequence         Often suitable        Less suitable
#
# MEMORY:
# Python lists and tuples both store references to objects.
# Tuples may have less overhead than lists for some workloads,
# but exact memory use depends on the Python implementation and data.
#
# SPEED:
# Do not assume tuples are always faster than lists.
# Performance depends on the operation, implementation, and workload.
#
# CHOOSE A LIST WHEN:
# - Elements need to be added, removed, or replaced.
# - You are building a dynamic collection.
# - Your algorithm needs stack-like append/pop behaviour.
#
# CHOOSE A TUPLE WHEN:
# - The collection represents a fixed record.
# - You want to prevent reassignment of its elements.
# - You need a hashable collection of hashable elements.
# - You want to return several values together.
#
# Examples:
# Coordinate: (x, y)
# RGB colour: (255, 100, 50)
# Database record: ("Atharva", 19, "PICT")
# Graph edge: (source, destination, weight)


# =============================================================================
# SECTION 14: RETURNING MULTIPLE VALUES FROM FUNCTIONS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 14: FUNCTIONS AND TUPLES")
print("=" * 75)

def calculate_statistics(numbers):
    """
    Return the minimum, maximum, and sum of a non-empty numeric sequence.

    The return statement uses commas to pack the values into a tuple.
    """

    if not numbers:
        raise ValueError("The input sequence must not be empty.")

    smallest = min(numbers)
    largest = max(numbers)
    total = sum(numbers)

    return smallest, largest, total


values = [10, 20, 30, 40, 50]

result = calculate_statistics(values)

print("Returned object:", result)
print("Type:", type(result))

# Unpack the returned tuple.

minimum, maximum, total = calculate_statistics(values)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)

# Python functions can return tuples, including tuples of mixed types.
# This is useful when an algorithm must return multiple related results.


# =============================================================================
# SECTION 15: TUPLES IN DICTIONARIES AND SETS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 15: TUPLES AS DICTIONARY KEYS")
print("=" * 75)

# Tuples can be dictionary keys when all their elements are hashable.

locations = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B"
}

print("Location at (0, 0):", locations[(0, 0)])
print("Location at (1, 2):", locations[(1, 2)])

# Tuples are useful for coordinates and states in grid-based problems.

visited = set()

visited.add((0, 0))
visited.add((1, 2))
visited.add((0, 0))

print("Visited coordinates:", visited)

# The repeated coordinate (0, 0) appears only once in the set.

# IMPORTANT:
# A tuple containing a list is not hashable.

# invalid_key = ([1, 2], 3)
# dictionary = {invalid_key: "value"}
#
# This raises TypeError because the tuple contains an unhashable list.


# =============================================================================
# SECTION 16: DSA APPLICATIONS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 16: DSA APPLICATIONS")
print("=" * 75)


# ---------------------------------------------------------------------------
# 16.1 LINEAR SEARCH IN A TUPLE
# ---------------------------------------------------------------------------
#
# Time complexity: O(n)
# Auxiliary space: O(1)

def tuple_linear_search(data, target):
    """Return the first index of target, or -1 if absent."""

    for i, value in enumerate(data):
        if value == target:
            return i

    return -1


numbers = (10, 20, 30, 40, 50)

print("Index of 30:", tuple_linear_search(numbers, 30))
print("Index of 100:", tuple_linear_search(numbers, 100))


# ---------------------------------------------------------------------------
# 16.2 FIND MINIMUM AND MAXIMUM
# ---------------------------------------------------------------------------
#
# Time complexity: O(n)
# Auxiliary space: O(1)

def tuple_min_max(data):
    """Find the minimum and maximum in one traversal."""

    if not data:
        return None

    smallest = data[0]
    largest = data[0]

    for value in data[1:]:

        if value < smallest:
            smallest = value

        if value > largest:
            largest = value

    return smallest, largest


numbers = (35, 12, 78, 4, 56)

print("Minimum and maximum:", tuple_min_max(numbers))


# ---------------------------------------------------------------------------
# 16.3 FREQUENCY COUNTING
# ---------------------------------------------------------------------------
#
# The tuple remains unchanged.
# The dictionary stores each element's frequency.
#
# Expected time complexity: O(n) for hashable elements.

def tuple_frequency(data):
    """Return a dictionary of element frequencies."""

    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    return frequency


numbers = (1, 2, 2, 3, 1, 2, 4, 3)

print("Frequencies:", tuple_frequency(numbers))


# ---------------------------------------------------------------------------
# 16.4 REMOVE DUPLICATES WHILE PRESERVING ORDER
# ---------------------------------------------------------------------------
#
# Returns a new tuple.
# Expected time complexity: O(n) for hashable elements.

def tuple_remove_duplicates(data):
    """Return a tuple containing unique elements in original order."""

    seen = set()
    result = []

    for value in data:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return tuple(result)


numbers = (1, 2, 2, 3, 1, 4, 3)

print("Unique tuple:", tuple_remove_duplicates(numbers))


# ---------------------------------------------------------------------------
# 16.5 BINARY SEARCH IN A SORTED TUPLE
# ---------------------------------------------------------------------------
#
# The tuple must be sorted in ascending order.
#
# Time complexity: O(log n)
# Auxiliary space: O(1)

def tuple_binary_search(data, target):
    """Return the index of target, or -1 if it is absent."""

    left = 0
    right = len(data) - 1

    while left <= right:

        mid = (left + right) // 2

        if data[mid] == target:
            return mid

        elif data[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


numbers = (10, 20, 30, 40, 50, 60)

print("Binary search for 40:", tuple_binary_search(numbers, 40))
print("Binary search for 25:", tuple_binary_search(numbers, 25))


# ---------------------------------------------------------------------------
# 16.6 TWO-SUM USING A TUPLE
# ---------------------------------------------------------------------------
#
# Return two indices whose values sum to the target.
#
# Expected time complexity: O(n)
# Auxiliary space: O(n)

def tuple_two_sum(data, target):
    """Return a pair of indices, or None if no solution exists."""

    seen = {}

    for i, value in enumerate(data):

        needed = target - value

        if needed in seen:
            return seen[needed], i

        if value not in seen:
            seen[value] = i

    return None


numbers = (2, 7, 11, 15)

print("Two-sum result:", tuple_two_sum(numbers, 9))


# ---------------------------------------------------------------------------
# 16.7 SORT A TUPLE
# ---------------------------------------------------------------------------
#
# Tuples cannot be sorted in place.
# sorted() creates a list, which can then be converted to a tuple.
#
# Time complexity: O(n log n) worst case.

numbers = (50, 10, 40, 20, 30)

sorted_numbers = tuple(sorted(numbers))

print("Original tuple:", numbers)
print("Sorted tuple:", sorted_numbers)


# =============================================================================
# SECTION 17: TIME COMPLEXITY
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 17: TIME COMPLEXITY")
print("=" * 75)

# n = number of elements.
#
# OPERATION                       TYPICAL TIME COMPLEXITY
# ---------------------------------------------------------------------------
# len(t)                          O(1)
# t[i]                            O(1)
# t[i:j]                          O(k), where k is slice length
# t.count(x)                      O(n)
# t.index(x)                      O(n)
# x in t                          O(n) worst case
# min(t)                          O(n)
# max(t)                          O(n)
# sum(t)                          O(n)
# sorted(t)                       O(n log n) worst case
# t + other_tuple                 O(n + m)
# t * k                           O(n * k), for positive repetition k
# tuple_linear_search(t, x)       O(n)
# tuple_binary_search(t, x)       O(log n), if sorted
# tuple_min_max(t)                O(n)
#
# Here:
# n = number of elements in the first tuple.
# m = number of elements in the second tuple.
# k = number of repetitions.
#
# NOTES:
#
# 1. Indexing is O(1).
#
# 2. A slice generally requires O(k) time and storage for k selected
#    elements, although implementations can optimise certain cases.
#
# 3. Concatenation creates a new tuple and copies element references.
#
# 4. Tuples do not support append(), insert(), or pop().
#
# 5. To change tuple contents, a new tuple must generally be constructed.
#
# 6. Complexity describes growth in work, not exact elapsed time.


# =============================================================================
# SECTION 18: COMMON MISTAKES
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 18: COMMON MISTAKES")
print("=" * 75)


# MISTAKE 1: Forgetting the comma in a single-element tuple.

a = (10)
b = (10,)

print("Without comma:", type(a))
print("With comma:", type(b))


# MISTAKE 2: Trying to modify a tuple.

numbers = (1, 2, 3)

# This is invalid:
# numbers[0] = 100
#
# Create a new tuple instead.

numbers = (100,) + numbers[1:]

print("New tuple:", numbers)


# MISTAKE 3: Assuming sorted() returns a tuple.

numbers = (3, 1, 2)

result = sorted(numbers)

print("sorted() result:", result)
print("Result type:", type(result))

# Convert it explicitly if a tuple is needed.

result_tuple = tuple(sorted(numbers))

print("Tuple result:", result_tuple)


# MISTAKE 4: Assuming a tuple makes nested lists immutable.

data = ([1, 2], [3, 4])

data[0].append(5)

print("Nested mutable objects:", data)


# MISTAKE 5: Assuming all tuples can be dictionary keys.

valid = (1, 2, 3)
dictionary = {valid: "valid key"}

print("Dictionary:", dictionary)

# invalid = ([1, 2], 3)
# dictionary = {invalid: "invalid key"}
#
# This raises TypeError because the tuple contains an unhashable list.


# MISTAKE 6: Unpacking the wrong number of values.

student = ("Atharva", 19, "Electronics")

# This raises ValueError:
# name, age = student

# Correct:
name, age, branch = student

print(name, age, branch)


# =============================================================================
# SECTION 19: PRACTICE PROBLEMS
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 19: PRACTICE PROBLEMS")
print("=" * 75)

# Try solving these without looking at earlier examples.
#
# PROBLEM 1:
# Create an empty tuple.
#
# PROBLEM 2:
# Create a single-element tuple containing 100.
#
# PROBLEM 3:
# Access the last element of (10, 20, 30, 40, 50).
#
# PROBLEM 4:
# Extract the last three elements using slicing.
#
# PROBLEM 5:
# Count the occurrences of 5 in (5, 2, 5, 3, 5, 4).
#
# PROBLEM 6:
# Find the first index of 30 in (10, 20, 30, 40, 30).
#
# PROBLEM 7:
# Sort (50, 10, 40, 20, 30) and return a tuple.
#
# PROBLEM 8:
# Unpack ("Atharva", 19, "PICT") into three variables.
#
# PROBLEM 9:
# Explain why a tuple cannot have an element reassigned.
#
# PROBLEM 10:
# Explain why a tuple containing a list is not necessarily deeply immutable.
#
# PROBLEM 11:
# Find the minimum and maximum in one traversal.
#
# PROBLEM 12:
# Implement linear search for a tuple.
#
# PROBLEM 13:
# Implement binary search for a sorted tuple.
#
# PROBLEM 14:
# Use a tuple coordinate as a dictionary key.
#
# PROBLEM 15:
# Explain the difference between a tuple and a list.
#
# PROBLEM 16:
# Explain why sorted(tuple_value) returns a list.
#
# PROBLEM 17:
# Explain the difference between == and is.
#
# PROBLEM 18:
# Return three statistics from a function using a tuple.


# =============================================================================
# SECTION 20: QUICK REVISION SUMMARY
# =============================================================================

print("\n" + "=" * 75)
print("SECTION 20: QUICK REVISION SUMMARY")
print("=" * 75)

# CONCEPT / METHOD              PURPOSE
# ---------------------------------------------------------------------------
# (1, 2, 3)                     Create a tuple
# ()                            Create an empty tuple
# (10,)                         Create a single-element tuple
# tuple(iterable)               Construct a tuple from an iterable
# len(t)                        Number of elements
# t[i]                          Access an element
# t[a:b:c]                      Slice a tuple
# min(t)                        Smallest element
# max(t)                        Largest element
# sum(t)                        Sum of numeric elements
# sorted(t)                     Return a sorted list
# tuple(sorted(t))              Return a sorted tuple
# t.count(x)                    Count occurrences
# t.index(x)                    Find the first matching index
# x in t                        Membership test
# t1 + t2                       Concatenate tuples
# t * n                         Repeat tuple elements
# a, b = (10, 20)               Unpack tuple elements
# id(t)                         Get object identity value
# t[::-1]                       Create a reversed tuple
#
# IMPORTANT:
#
# - Tuples are ordered and immutable.
# - Tuples allow duplicates and mixed types.
# - A single-element tuple requires a trailing comma.
# - Tuples support indexing, slicing, and iteration.
# - Tuples have count() and index() methods.
# - Tuples do not have append(), remove(), pop(), or clear().
# - sorted() returns a list, even when the input is a tuple.
# - Immutable tuples can be hashable, provided their elements are hashable.
# - A tuple containing a mutable object is not deeply immutable.
# - Binary search requires sorted data.
# - Tuples are useful for fixed records, coordinates, and multiple returns.


print("\n" + "=" * 75)
print("END OF PYTHON TUPLES: COMPLETE DSA REVISION")
print("=" * 75)

print("\nRevision complete!")
print("Next step: Solve the practice problems without looking at the code.")
