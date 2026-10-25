
# ================================================================
#             PYTHON DICTIONARIES: COMPLETE DSA REVISION
# ================================================================
#
# PURPOSE:
# 1. Understand dictionary fundamentals and key-value pairs.
# 2. Learn creation, access, insertion, updating, and deletion.
# 3. Master dictionary methods and dictionary comprehensions.
# 4. Understand hashing and average-case time complexity.
# 5. Learn frequency counting using dictionaries.
# 6. Solve common DSA and interview-style problems.
# 7. Master prefix sums, hashing, and sliding-window patterns.
# 8. Understand defaultdict, Counter, and nested dictionaries.
#
# ================================================================
# IMPORTANT PROPERTIES
# ================================================================
#
# 1. A dictionary stores key-value pairs.
# 2. Keys must be hashable.
# 3. Values can be of any type.
# 4. Keys are unique: assigning an existing key replaces its value.
# 5. Dictionaries are mutable.
# 6. Dictionaries preserve insertion order in modern Python.
# 7. Key lookup, insertion, and deletion are O(1) on average.
# 8. Dictionary keys can be strings, integers, tuples, etc.
#    provided the keys are hashable.
#
# Example:
#
# student = {
#     "name": "Atharva",
#     "roll": 22114,
#     "marks": 95
# }
#
# "name"  -> key
# "Atharva" -> value
#
# ================================================================


# ================================================================
# SECTION 1: CREATING DICTIONARIES
# ================================================================

def dictionary_creation():

    # Method 1: Using curly braces.
    student = {
        "name": "Atharva",
        "roll": 22114,
        "marks": 95
    }

    print("Student:", student)

    # Method 2: Using dict().
    another_student = dict(
        name="Rahul",
        roll=22115,
        marks=90
    )

    print("Another student:", another_student)

    # Method 3: Create an empty dictionary.
    empty_dictionary = {}

    # Equivalent:
    another_empty_dictionary = dict()

    print("Empty dictionary:", empty_dictionary)

    # Dictionary keys must be unique.
    # If a key is repeated, its last assigned value remains.
    data = {
        "a": 10,
        "b": 20,
        "a": 30
    }

    print("Repeated key:", data)
    # Result: {'a': 30, 'b': 20}

    # Dictionary values can have different data types.
    mixed = {
        "name": "Atharva",
        "age": 19,
        "percentage": 92.5,
        "passed": True,
        "subjects": ["Maths", "Python"],
        "address": None
    }

    print("Mixed dictionary:", mixed)


# ================================================================
# SECTION 2: ACCESSING VALUES
# ================================================================

def accessing_values():

    student = {
        "name": "Atharva",
        "roll": 22114,
        "marks": 95
    }

    # Method 1: Square brackets.
    print(student["name"])
    print(student["marks"])

    # If the key does not exist, square brackets raise KeyError.
    #
    # print(student["age"])  # KeyError

    # Method 2: get().
    # Returns None when the key is absent, unless a default
    # value is supplied.
    print(student.get("age"))

    # Supply a default value.
    print(student.get("age", 0))

    # get() does not insert a missing key into the dictionary.
    print(student)

    # Membership testing checks KEYS, not values.
    print("name" in student)       # True
    print("Atharva" in student)    # False
    print("Atharva" in student.values())  # True


# ================================================================
# SECTION 3: INSERTING AND UPDATING VALUES
# ================================================================

def inserting_and_updating():

    student = {
        "name": "Atharva",
        "marks": 85
    }

    # Add a new key-value pair.
    student["roll"] = 22114

    print("After insertion:", student)

    # Update an existing value.
    student["marks"] = 95

    print("After updating:", student)

    # update() inserts or replaces multiple key-value pairs.
    student.update({
        "marks": 98,
        "city": "Pune"
    })

    print("After update():", student)

    # setdefault():
    # If the key exists, return its current value.
    # If the key is absent, insert it with the given default.
    result = student.setdefault("age", 19)

    print("Returned value:", result)
    print("After setdefault():", student)

    # Calling setdefault() for an existing key does not replace
    # its value.
    student.setdefault("marks", 0)

    print("Marks remain unchanged:", student["marks"])


# ================================================================
# SECTION 4: REMOVING KEY-VALUE PAIRS
# ================================================================

def removing_elements():

    student = {
        "name": "Atharva",
        "roll": 22114,
        "marks": 95,
        "city": "Pune"
    }

    # pop(key):
    # Removes the key and returns its value.
    removed_marks = student.pop("marks")

    print("Removed marks:", removed_marks)
    print("Dictionary:", student)

    # pop(key, default):
    # Returns the default if the key is missing.
    result = student.pop("age", 0)

    print("Missing key result:", result)

    # popitem():
    # Removes and returns the last inserted key-value pair.
    removed_pair = student.popitem()

    print("Removed pair:", removed_pair)
    print("Dictionary:", student)

    # del:
    # Removes a specific key.
    del student["roll"]

    print("After del:", student)

    # clear():
    # Removes all entries.
    student.clear()

    print("After clear:", student)


# ================================================================
# SECTION 5: DICTIONARY METHODS
# ================================================================

def dictionary_methods():

    student = {
        "name": "Atharva",
        "roll": 22114,
        "marks": 95
    }

    # keys(): view of all keys.
    print("Keys:", student.keys())

    # values(): view of all values.
    print("Values:", student.values())

    # items(): view of key-value pairs.
    print("Items:", student.items())

    # len(): number of key-value pairs.
    print("Length:", len(student))

    # Copy the dictionary.
    copied = student.copy()

    print("Copied:", copied)

    # Membership checks keys.
    print("roll" in student)
    print("Pune" in student)

    # Convert keys into a list if indexed access is needed.
    keys_list = list(student.keys())

    print("Keys list:", keys_list)

    # Dictionary views reflect changes to the dictionary.
    # A list made from a view is a separate list.


# ================================================================
# SECTION 6: ITERATING THROUGH A DICTIONARY
# ================================================================

def dictionary_iteration():

    student = {
        "name": "Atharva",
        "roll": 22114,
        "marks": 95
    }

    # Method 1: Iterate through keys.
    for key in student:
        print(key)

    # Equivalent:
    for key in student.keys():
        print(key)

    # Method 2: Iterate through values.
    for value in student.values():
        print(value)

    # Method 3: Iterate through keys and values.
    for key, value in student.items():
        print(key, "->", value)

    # enumerate() can be used when a position is useful.
    for index, (key, value) in enumerate(student.items()):
        print(index, key, value)


# ================================================================
# SECTION 7: DICTIONARY COMPREHENSION
# ================================================================

def dictionary_comprehension():

    numbers = [1, 2, 3, 4, 5]

    # Syntax:
    # {key_expression: value_expression for item in iterable}

    squares = {
        number: number * number
        for number in numbers
    }

    print("Squares:", squares)

    # Result:
    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # Keep only even numbers.
    even_squares = {
        number: number * number
        for number in numbers
        if number % 2 == 0
    }

    print("Even squares:", even_squares)

    # Convert a list of words into a length dictionary.
    words = ["Python", "Java", "C++"]

    lengths = {
        word: len(word)
        for word in words
    }

    print("Word lengths:", lengths)

    # IMPORTANT:
    # If two generated keys are equal, the later value replaces
    # the earlier value.


# ================================================================
# SECTION 8: MERGING DICTIONARIES
# ================================================================

def merging_dictionaries():

    A = {
        "a": 10,
        "b": 20
    }

    B = {
        "b": 99,
        "c": 30
    }

    # Method 1: Dictionary unpacking.
    merged = {**A, **B}

    print("Merged:", merged)

    # If keys overlap, the rightmost dictionary wins.
    # Here, B's value for "b" replaces A's value.

    # Method 2: Union operator, Python 3.9+.
    merged_again = A | B

    print("Union operator:", merged_again)

    # Method 3: update().
    updated = A.copy()
    updated.update(B)

    print("Updated copy:", updated)

    # A remains unchanged because update() was applied to a copy.
    print("Original A:", A)


# ================================================================
# SECTION 9: REVERSE A DICTIONARY
# ================================================================

def reverse_dictionary(data):
    """
    Reverse a dictionary's keys and values.

    Original:
        {"a": 1, "b": 2}

    Result:
        {1: "a", 2: "b"}

    IMPORTANT:
    This requires the original values to be hashable.
    If multiple keys share the same value, earlier entries
    can be overwritten.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    reversed_dictionary = {}

    for key, value in data.items():
        reversed_dictionary[value] = key

    return reversed_dictionary


def reverse_dictionary_grouped(data):
    """
    Reverse a dictionary while preserving all keys that share
    the same value.

    Example:
        {"A": 90, "B": 80, "C": 90}

    Result:
        {90: ["A", "C"], 80: ["B"]}

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    result = {}

    for key, value in data.items():

        if value not in result:
            result[value] = []

        result[value].append(key)

    return result


# ================================================================
# SECTION 10: FREQUENCY COUNTING
# ================================================================

def frequency_count(values):
    """
    Count the occurrences of each value.

    Example:
        [1, 2, 2, 3, 1, 1]

    Result:
        {1: 3, 2: 2, 3: 1}

    Time Complexity: O(n) average
    Space Complexity: O(k)

    n = number of input elements
    k = number of distinct elements
    """

    frequency = {}

    for value in values:

        # If value exists, increase its count.
        # Otherwise, begin its count at 1.
        frequency[value] = frequency.get(value, 0) + 1

    return frequency


# ================================================================
# SECTION 11: CHARACTER FREQUENCY
# ================================================================

def character_frequency(text):
    """
    Count each character in a string.

    Example:
        "banana" -> {"b": 1, "a": 3, "n": 2}

    Case-sensitive:
        "A" and "a" are different characters.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    frequency = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    return frequency


# ================================================================
# SECTION 12: FIRST NON-REPEATING CHARACTER
# ================================================================

def first_non_repeating_character(text):
    """
    Return the first character that appears exactly once.

    Example:
        "aabbcdd" -> "c"

    Return None if every character repeats.

    Step 1: Count all characters.
    Step 2: Scan the original string in order.
    Step 3: Return the first character with frequency 1.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    frequency = character_frequency(text)

    for character in text:

        if frequency[character] == 1:
            return character

    return None


# ================================================================
# SECTION 13: CHECK WHETHER TWO STRINGS ARE ANAGRAMS
# ================================================================

def are_anagrams(text1, text2):
    """
    Two strings are anagrams if every character occurs the
    same number of times in both strings.

    Examples:
        "listen", "silent" -> True
        "hello", "world" -> False

    This implementation is case-sensitive and includes spaces.

    Time Complexity: O(n + m) average
    Space Complexity: O(k)
    """

    return character_frequency(text1) == character_frequency(text2)


# ================================================================
# SECTION 14: GROUP ANAGRAMS
# ================================================================

def group_anagrams(words):
    """
    Group words containing the same characters with the
    same frequencies.

    Example:
        ["eat", "tea", "tan", "ate", "nat", "bat"]

    Possible result:
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    Strategy:
        Sort each word to create a common key.

        "eat" -> "aet"
        "tea" -> "aet"
        "ate" -> "aet"

        Words sharing a key belong to the same group.

    Let:
        n = number of words
        m = maximum word length

    Time Complexity: O(n * m log m)
    Space Complexity: O(n * m)
    """

    groups = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# ================================================================
# SECTION 15: TWO SUM — RETURN INDICES
# ================================================================

def two_sum(numbers, target):
    """
    Return indices of two DIFFERENT positions whose values
    sum to target.

    Example:
        numbers = [2, 7, 11, 15]
        target = 9

        Result: [0, 1]

    Strategy:
        For every number x, calculate:
            complement = target - x

        If the complement has already appeared, its stored
        index and the current index form the answer.

    Why store indices?
        A dictionary maps each number to an earlier position.

    Time Complexity: O(n) average
    Space Complexity: O(n)

    Assumption:
        Exactly one valid pair exists.
    """

    index_map = {}

    for index, number in enumerate(numbers):

        complement = target - number

        if complement in index_map:
            return [index_map[complement], index]

        # Store the current index only after checking.
        # This prevents reusing the same element twice.
        index_map[number] = index

    return []


# ================================================================
# SECTION 16: FIND ALL PAIRS THAT SUM TO A TARGET
# ================================================================

def all_unique_pairs(numbers, target):
    """
    Return all unique VALUE pairs that sum to target.

    Example:
        numbers = [1, 2, 3, 4, 3, 2]
        target = 5

    Result:
        [(1, 4), (2, 3)]

    Duplicate pairs are returned only once.

    Time Complexity: O(n + p), average, where p is the
                     number of unique pairs returned.
    Space Complexity: O(n + p)
    """

    seen = set()
    pairs = set()

    for number in numbers:

        complement = target - number

        if complement in seen:

            # Sorting the pair gives it a canonical representation.
            pair = tuple(sorted((number, complement)))
            pairs.add(pair)

        seen.add(number)

    return sorted(pairs)


# ================================================================
# SECTION 17: CHECK WHETHER AN ARRAY HAS DUPLICATES
# ================================================================

def contains_duplicates(numbers):
    """
    Return True if any value occurs more than once.

    Example:
        [1, 2, 3, 1] -> True
        [1, 2, 3, 4] -> False

    Time Complexity: O(n) average
    Space Complexity: O(n)
    """

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False


# ================================================================
# SECTION 18: TOP K FREQUENT ELEMENTS
# ================================================================

def top_k_frequent(numbers, k):
    """
    Return the k most frequent elements.

    Example:
        numbers = [1, 1, 1, 2, 2, 3]
        k = 2

        Result: [1, 2]

    Strategy:
        1. Count frequencies.
        2. Sort distinct elements by descending frequency.
        3. Return the first k elements.

    Time Complexity: O(n + u log u)
    Space Complexity: O(u)

    u = number of unique elements

    Tie-breaking:
        When frequencies tie, this implementation uses the
        smaller numeric value first.
    """

    frequency = frequency_count(numbers)

    ordered = sorted(
        frequency,
        key=lambda number: (-frequency[number], number)
    )

    return ordered[:k]


# ================================================================
# SECTION 19: MERGE TWO DICTIONARIES BY ADDING VALUES
# ================================================================

def merge_sum(dictionary1, dictionary2):
    """
    Merge dictionaries by adding values for common keys.

    Example:
        A = {"a": 10, "b": 20}
        B = {"b": 5, "c": 30}

        Result:
        {"a": 10, "b": 25, "c": 30}

    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """

    result = dictionary1.copy()

    for key, value in dictionary2.items():

        result[key] = result.get(key, 0) + value

    return result


# ================================================================
# SECTION 20: PREFIX SUM + HASH MAP
# ================================================================

def subarray_sum_equals_k(numbers, k):
    """
    Count contiguous subarrays whose sum equals k.

    Example:
        numbers = [1, 1, 1]
        k = 2

        Result: 2

    The valid subarrays are:
        [1, 1] at indices 0-1
        [1, 1] at indices 1-2

    Prefix sum:
        prefix[i] = sum of elements from index 0 through i.

    If the current prefix sum is S, a previous prefix sum
    equal to S - k means the intervening subarray sums to k.

    Therefore:
        answer += frequency[prefix_sum - k]

    IMPORTANT:
        This works even when the array contains negative values.
        A sliding window based only on the sum is not generally
        valid when negative numbers are allowed.

    Time Complexity: O(n) average
    Space Complexity: O(n)
    """

    prefix_sum = 0
    count = 0

    # An empty prefix has sum zero and occurs once.
    prefix_frequency = {0: 1}

    for number in numbers:

        prefix_sum += number

        required = prefix_sum - k

        # Count previous prefixes that produce a sum of k.
        count += prefix_frequency.get(required, 0)

        # Record the current prefix for future subarrays.
        prefix_frequency[prefix_sum] = (
            prefix_frequency.get(prefix_sum, 0) + 1
        )

    return count


# ================================================================
# SECTION 21: LONGEST SUBARRAY WITH SUM K
# ================================================================

def longest_subarray_sum_k(numbers, k):
    """
    Find the length of the longest contiguous subarray whose
    sum equals k.

    Example:
        numbers = [1, -1, 5, -2, 3]
        k = 3

        Result: 4

    The longest valid subarray is:
        [1, -1, 5, -2]

    Strategy:
        Store the earliest index at which each prefix sum occurs.

        If the current prefix sum is S, look for:
            S - k

        If that prefix occurred at index j, the subarray after
        j through the current index has sum k.

    Why keep the earliest index?
        An earlier prefix produces a longer candidate subarray.

    Time Complexity: O(n) average
    Space Complexity: O(n)
    """

    prefix_sum = 0
    longest = 0

    # Prefix sum zero exists before the array begins.
    first_index = {0: -1}

    for index, number in enumerate(numbers):

        prefix_sum += number

        required = prefix_sum - k

        if required in first_index:

            length = index - first_index[required]
            longest = max(longest, length)

        # Only store the earliest index of each prefix sum.
        if prefix_sum not in first_index:
            first_index[prefix_sum] = index

    return longest


# ================================================================
# SECTION 22: LONGEST CONSECUTIVE SEQUENCE
# ================================================================

def longest_consecutive_sequence(numbers):
    """
    Find the length of the longest consecutive integer sequence.

    Example:
        [100, 4, 200, 1, 3, 2] -> 4

    Longest sequence:
        1, 2, 3, 4

    Strategy:
        1. Store all unique numbers in a set.
        2. Start counting only if number - 1 is absent.
        3. Count forward while consecutive numbers exist.

    Although this uses a set for membership, a dictionary can
    also be used when extra information per value is needed.

    Time Complexity: O(n) average
    Space Complexity: O(n)
    """

    number_set = set(numbers)
    longest = 0

    for number in number_set:

        if number - 1 not in number_set:

            current = number
            length = 1

            while current + 1 in number_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# ================================================================
# SECTION 23: SLIDING WINDOW — DISTINCT ELEMENT COUNTS
# ================================================================

def distinct_elements_in_windows(numbers, k):
    """
    Count distinct elements in every contiguous window of size k.

    Example:
        numbers = [1, 2, 1, 3, 4, 2, 3]
        k = 4

        Result: [3, 4, 4, 3]

    Strategy:
        Maintain a frequency dictionary for the current window.

        When a number leaves the window:
            Decrease its frequency.
            Delete the key if its frequency becomes zero.

        When a number enters:
            Increase its frequency.

        len(frequency) gives the distinct count.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    n = len(numbers)

    if k <= 0 or k > n:
        return []

    frequency = {}

    # Build the first window.
    for i in range(k):
        number = numbers[i]

        frequency[number] = frequency.get(number, 0) + 1

    result = [len(frequency)]

    # Slide the window.
    for right in range(k, n):

        outgoing = numbers[right - k]
        incoming = numbers[right]

        frequency[outgoing] -= 1

        if frequency[outgoing] == 0:
            del frequency[outgoing]

        frequency[incoming] = (
            frequency.get(incoming, 0) + 1
        )

        result.append(len(frequency))

    return result


# ================================================================
# SECTION 24: GROUP RECORDS USING A DICTIONARY
# ================================================================

def group_by_department(employees):
    """
    Group employees by department.

    Example:
        employees = [
            {"name": "A", "department": "IT"},
            {"name": "B", "department": "HR"},
            {"name": "C", "department": "IT"}
        ]

    Result:
        {
            "IT": [employee_A, employee_C],
            "HR": [employee_B]
        }

    This demonstrates a common real-world dictionary pattern:
    mapping a category to a list of records.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    grouped = {}

    for employee in employees:

        department = employee["department"]

        if department not in grouped:
            grouped[department] = []

        grouped[department].append(employee)

    return grouped


# ================================================================
# SECTION 25: NESTED DICTIONARIES
# ================================================================

def nested_dictionary_demo():

    students = {
        22114: {
            "name": "Atharva",
            "marks": 95,
            "city": "Pune"
        },

        22115: {
            "name": "Rahul",
            "marks": 90,
            "city": "Mumbai"
        }
    }

    # Access an outer key and then an inner key.
    print(students[22114]["name"])
    print(students[22115]["marks"])

    # Update a nested value.
    students[22114]["marks"] = 98

    print(students[22114])

    # Insert a new nested field.
    students[22114]["department"] = "ENTC"

    print(students[22114])

    # Iterate over records.
    for roll, details in students.items():

        print("Roll:", roll)

        for key, value in details.items():
            print(" ", key, ":", value)


# ================================================================
# SECTION 26: DEFAULTDICT
# ================================================================

from collections import defaultdict


def defaultdict_demo():

    # defaultdict(list):
    # A missing key automatically gets an empty list.

    grouped = defaultdict(list)

    grouped["IT"].append("Atharva")
    grouped["IT"].append("Rahul")
    grouped["HR"].append("Priya")

    print("Grouped:", dict(grouped))

    # defaultdict(int):
    # A missing key automatically starts at zero.

    frequency = defaultdict(int)

    for character in "banana":
        frequency[character] += 1

    print("Frequency:", dict(frequency))

    # defaultdict(set):
    # A missing key automatically gets an empty set.

    graph = defaultdict(set)

    graph["A"].add("B")
    graph["A"].add("C")
    graph["B"].add("A")

    print("Graph:", dict(graph))

    # Difference from ordinary dict:
    #
    # normal = {}
    # normal["x"] += 1  # KeyError
    #
    # counts = defaultdict(int)
    # counts["x"] += 1  # Works; missing value begins at 0.


# ================================================================
# SECTION 27: COUNTER
# ================================================================

from collections import Counter


def counter_demo():

    numbers = [1, 2, 2, 3, 3, 3, 4]

    # Counter is a specialised dictionary for counting.
    counts = Counter(numbers)

    print("Counts:", counts)

    # Access a frequency.
    print("Frequency of 3:", counts[3])

    # Most common elements.
    print("Two most common:", counts.most_common(2))

    # Counter also works with strings.
    letters = Counter("banana")

    print("Letter counts:", letters)

    # Compare two frequency distributions.
    print(
        "Anagrams:",
        Counter("listen") == Counter("silent")
    )

    # Note:
    # Counter is convenient, but a regular dictionary is useful
    # when learning the underlying counting pattern.


# ================================================================
# SECTION 28: LRU CACHE CONCEPT
# ================================================================

def lru_cache_demo():
    """
    Demonstrate a built-in LRU cache.

    LRU means Least Recently Used.

    This is not implemented from scratch here. The example
    demonstrates how dictionaries and caching relate to
    algorithm performance.
    """

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n <= 1:
            return n

        return fibonacci(n - 1) + fibonacci(n - 2)

    print("Fibonacci(10):", fibonacci(10))
    print("Cache information:", fibonacci.cache_info())

    # Memoization stores previously computed results.
    # A dictionary is the underlying idea:
    # input -> previously computed output


# ================================================================
# SECTION 29: COMMON DICTIONARY MISTAKES
# ================================================================

def common_mistakes():

    data = {
        "a": 1,
        "b": 2
    }

    # ------------------------------------------------------------
    # MISTAKE 1: Accessing a missing key with square brackets.
    # ------------------------------------------------------------

    # data["c"]  # Raises KeyError.

    # Safer when the key may be missing:
    print(data.get("c", 0))

    # ------------------------------------------------------------
    # MISTAKE 2: Confusing key membership with value membership.
    # ------------------------------------------------------------

    print("a" in data)             # True: checks keys
    print(1 in data)               # False: checks keys
    print(1 in data.values())      # True: checks values

    # ------------------------------------------------------------
    # MISTAKE 3: Assuming duplicate keys are preserved.
    # ------------------------------------------------------------

    repeated = {
        "x": 1,
        "x": 2
    }

    print(repeated)  # Only the last value remains.

    # ------------------------------------------------------------
    # MISTAKE 4: Using mutable keys.
    # ------------------------------------------------------------

    # invalid = {[1, 2]: "value"}  # TypeError

    # Tuples of hashable elements can be keys.
    valid = {
        (1, 2): "value"
    }

    print(valid[(1, 2)])

    # ------------------------------------------------------------
    # MISTAKE 5: Modifying dictionary size during iteration.
    # ------------------------------------------------------------

    values = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    # Risky:
    #
    # for key in values:
    #     if values[key] % 2 == 0:
    #         del values[key]
    #
    # This can raise RuntimeError because the dictionary's
    # size changes during iteration.

    # Safer: collect keys to delete first.
    keys_to_delete = [
        key
        for key, value in values.items()
        if value % 2 == 0
    ]

    for key in keys_to_delete:
        del values[key]

    print("After safe deletion:", values)

    # ------------------------------------------------------------
    # MISTAKE 6: Confusing shallow copy with deep copy.
    # ------------------------------------------------------------

    original = {
        "numbers": [1, 2, 3]
    }

    copied = original.copy()

    # The outer dictionary was copied, but the nested list
    # is shared between both dictionaries.
    copied["numbers"].append(4)

    print("Original after nested modification:", original)

    # Use copy.deepcopy() when a fully independent nested copy
    # is required.


# ================================================================
# SECTION 30: TIME COMPLEXITY SUMMARY
# ================================================================

def complexity_summary():

    """
    Typical average-case dictionary operation complexities.

    Operation                       Average Time
    ------------------------------------------------
    data[key]                       O(1)
    data[key] = value               O(1)
    key in data                     O(1)
    data.get(key)                   O(1)
    data.pop(key)                   O(1)
    data.update(other)              O(len(other))
    len(data)                       O(1)
    Iterating over keys             O(n)
    Iterating over values           O(n)
    Iterating over items            O(n)
    Copying a dictionary            O(n)
    Building a frequency map        O(n) average
    Two Sum using a dictionary      O(n) average
    Prefix sum + hash map           O(n) average

    n = number of dictionary entries or input elements.

    IMPORTANT:
    These are typical average-case complexities.
    Hash collisions can cause worse worst-case behavior.
    """

    pass


# ================================================================
# SECTION 31: EDGE-CASE TESTS
# ================================================================

def run_edge_case_tests():

    # Frequency counting.
    assert frequency_count([]) == {}
    assert frequency_count([1, 1, 2]) == {
        1: 2,
        2: 1
    }

    # Character frequency.
    assert character_frequency("") == {}
    assert character_frequency("aaa") == {
        "a": 3
    }

    # First non-repeating character.
    assert first_non_repeating_character("aabbcdd") == "c"
    assert first_non_repeating_character("aabb") is None
    assert first_non_repeating_character("") is None

    # Anagrams.
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("hello", "world") is False
    assert are_anagrams("", "") is True

    # Reverse dictionary.
    assert reverse_dictionary({
        "a": 1,
        "b": 2
    }) == {
        1: "a",
        2: "b"
    }

    # Group repeated values when reversing.
    assert reverse_dictionary_grouped({
        "A": 90,
        "B": 80,
        "C": 90
    }) == {
        90: ["A", "C"],
        80: ["B"]
    }

    # Two Sum.
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3], 10) == []

    # Duplicate detection.
    assert contains_duplicates([1, 2, 3, 1]) is True
    assert contains_duplicates([1, 2, 3]) is False
    assert contains_duplicates([]) is False

    # Unique value pairs.
    assert all_unique_pairs(
        [1, 2, 3, 4, 3, 2],
        5
    ) == [(1, 4), (2, 3)]

    # Top frequent elements.
    assert top_k_frequent(
        [1, 1, 1, 2, 2, 3],
        2
    ) == [1, 2]

    # Dictionary merge.
    assert merge_sum(
        {"a": 10, "b": 20},
        {"b": 5, "c": 30}
    ) == {
        "a": 10,
        "b": 25,
        "c": 30
    }

    # Prefix sum: count subarrays.
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    assert subarray_sum_equals_k([1, -1, 0], 0) == 3
    assert subarray_sum_equals_k([], 0) == 0

    # Prefix sum: longest subarray.
    assert longest_subarray_sum_k(
        [1, -1, 5, -2, 3],
        3
    ) == 4

    assert longest_subarray_sum_k([], 0) == 0

    # Longest consecutive sequence.
    assert longest_consecutive_sequence(
        [100, 4, 200, 1, 3, 2]
    ) == 4

    assert longest_consecutive_sequence([]) == 0
    assert longest_consecutive_sequence([5, 5, 5]) == 1

    # Sliding-window distinct counts.
    assert distinct_elements_in_windows(
        [1, 2, 1, 3, 4, 2, 3],
        4
    ) == [3, 4, 4, 3]

    assert distinct_elements_in_windows([1, 2], 3) == []
    assert distinct_elements_in_windows([1, 2], 0) == []

    print("All edge-case tests passed!")


# ================================================================
# SECTION 32: PRACTICE PROBLEMS
# ================================================================

def practice_problems():

    """
    BEGINNER:
        1. Create a dictionary of student records.
        2. Count the frequency of elements in a list.
        3. Count the frequency of characters in a string.
        4. Find the first non-repeating character.
        5. Merge two dictionaries.

    INTERMEDIATE:
        6. Check whether two strings are anagrams.
        7. Group words into anagram groups.
        8. Solve Two Sum and return indices.
        9. Find the top k frequent elements.
        10. Find the longest subarray with sum k.
        11. Count subarrays with sum k.
        12. Count distinct elements in every window.

    ADVANCED:
        13. Implement an LRU cache using a dictionary and
            a doubly linked list.
        14. Implement a trie for prefix-based string searching.
        15. Solve a frequency-based sliding-window problem.
        16. Use prefix sums and a dictionary to optimise
            a quadratic subarray algorithm.
        17. Implement a graph using an adjacency dictionary.

    For each problem:
        - Start with brute force.
        - Identify repeated searches.
        - Determine what the key should represent.
        - Decide what value must be stored for each key.
        - Analyse time and space complexity.
    """

    pass


# ================================================================
# SECTION 33: MAIN DEMONSTRATION
# ================================================================

if __name__ == "__main__":

    print("=" * 65)
    print("             PYTHON DICTIONARIES: DSA REVISION")
    print("=" * 65)

    print("\n1. Creating Dictionaries")
    dictionary_creation()

    print("\n2. Accessing Values")
    accessing_values()

    print("\n3. Inserting and Updating")
    inserting_and_updating()

    print("\n4. Removing Elements")
    removing_elements()

    print("\n5. Dictionary Methods")
    dictionary_methods()

    print("\n6. Dictionary Iteration")
    dictionary_iteration()

    print("\n7. Dictionary Comprehension")
    dictionary_comprehension()

    print("\n8. Merging Dictionaries")
    merging_dictionaries()

    print("\n9. Reverse Dictionary")
    print(reverse_dictionary({
        "a": 1,
        "b": 2,
        "c": 3
    }))

    print("\n10. Reverse Dictionary with Duplicate Values")
    print(reverse_dictionary_grouped({
        "A": 90,
        "B": 80,
        "C": 90
    }))

    print("\n11. Frequency Counting")
    print(frequency_count([1, 2, 2, 3, 1, 1]))

    print("\n12. Character Frequency")
    print(character_frequency("banana"))

    print("\n13. First Non-Repeating Character")
    print(first_non_repeating_character("aabbcdd"))

    print("\n14. Anagrams")
    print(are_anagrams("listen", "silent"))

    print("\n15. Group Anagrams")
    print(group_anagrams([
        "eat", "tea", "tan", "ate", "nat", "bat"
    ]))

    print("\n16. Two Sum")
    print(two_sum([2, 7, 11, 15], 9))

    print("\n17. All Unique Pairs")
    print(all_unique_pairs(
        [1, 2, 3, 4, 3, 2],
        5
    ))

    print("\n18. Duplicate Detection")
    print(contains_duplicates([1, 2, 3, 1]))

    print("\n19. Top K Frequent Elements")
    print(top_k_frequent(
        [1, 1, 1, 2, 2, 3],
        2
    ))

    print("\n20. Merge Dictionaries by Adding Values")
    print(merge_sum(
        {"a": 10, "b": 20},
        {"b": 5, "c": 30}
    ))

    print("\n21. Count Subarrays with Sum K")
    print(subarray_sum_equals_k([1, 1, 1], 2))

    print("\n22. Longest Subarray with Sum K")
    print(longest_subarray_sum_k(
        [1, -1, 5, -2, 3],
        3
    ))

    print("\n23. Longest Consecutive Sequence")
    print(longest_consecutive_sequence(
        [100, 4, 200, 1, 3, 2]
    ))

    print("\n24. Distinct Elements in Sliding Windows")
    print(distinct_elements_in_windows(
        [1, 2, 1, 3, 4, 2, 3],
        4
    ))

    print("\n25. Group Records by Department")

    employees = [
        {"name": "Atharva", "department": "IT"},
        {"name": "Rahul", "department": "HR"},
        {"name": "Priya", "department": "IT"}
    ]

    print(group_by_department(employees))

    print("\n26. Nested Dictionaries")
    nested_dictionary_demo()

    print("\n27. defaultdict")
    defaultdict_demo()

    print("\n28. Counter")
    counter_demo()

    print("\n29. LRU Cache")
    lru_cache_demo()

    print("\n30. Common Mistakes")
    common_mistakes()

    print("\n31. Edge-Case Tests")
    run_edge_case_tests()

    print("\n" + "=" * 65)
    print("                 REVISION COMPLETED")
    print("=" * 65)
