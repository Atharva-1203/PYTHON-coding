
# ================================================================
#                 PYTHON STRINGS: COMPLETE DSA REVISION
# ================================================================
#
# PURPOSE:
# 1. Understand Python string fundamentals.
# 2. Learn indexing, slicing, and built-in string methods.
# 3. Master common string manipulation techniques.
# 4. Learn Two Pointers, Hashing, Sliding Window, and Stack patterns.
# 5. Solve common DSA and LeetCode-style string problems.
# 6. Understand time complexity, space complexity, and edge cases.
#
# IMPORTANT:
# Strings in Python are IMMUTABLE.
# This means that individual characters cannot be modified in place.
#
# Example:
# s = "hello"
# s[0] = "H"      # TypeError
#
# Instead:
# s = "H" + s[1:] # Creates a new string: "Hello"
#
# ================================================================


# ================================================================
# SECTION 1: STRING FUNDAMENTALS
# ================================================================

def string_fundamentals():
    """
    Demonstrates basic string operations.
    """

    # Single quotes, double quotes, and triple quotes are supported.
    s1 = 'Hello'
    s2 = "Python"
    s3 = """This is a
    multiline string."""

    print("String:", s1)
    print("Length:", len(s1))
    print("Concatenation:", s1 + " " + s2)
    print("Repetition:", "Hi " * 3)

    # Strings can contain letters, numbers, symbols, and spaces.
    s = "Python 123!"

    print("String:", s)
    print("Contains Python:", "Python" in s)
    print("Contains Java:", "Java" in s)

    # Strings are iterable.
    for character in "ABC":
        print(character)


# ================================================================
# SECTION 2: INDEXING
# ================================================================

def string_indexing():
    """
    Access individual characters using positive and negative indices.
    """

    s = "PYTHON"

    # Positive indexing starts at 0.
    print(s[0])  # P
    print(s[1])  # Y
    print(s[5])  # N

    # Negative indexing starts at -1 from the end.
    print(s[-1])  # N
    print(s[-2])  # O
    print(s[-6])  # P

    # Valid positive indices: 0 through len(s) - 1.
    # Valid negative indices: -len(s) through -1.
    #
    # Accessing an invalid index raises IndexError.
    # print(s[10])


# ================================================================
# SECTION 3: SLICING
# ================================================================

def string_slicing():
    """
    Syntax:
        s[start:stop:step]

    start: included
    stop: excluded
    step: interval between selected characters
    """

    s = "PYTHON"

    print(s[0:3])    # PYT
    print(s[2:5])    # THO
    print(s[:3])     # PYT
    print(s[3:])     # HON
    print(s[:])      # PYTHON

    # Negative slicing.
    print(s[-3:])    # HON
    print(s[:-1])    # PYTHO

    # Reverse a string.
    print(s[::-1])   # NOHTYP

    # Select every second character.
    print(s[::2])    # PTO

    # A slice with a stop beyond the string's length is allowed.
    print(s[0:100])  # PYTHON

    # Slicing does not normally raise IndexError for out-of-range
    # boundaries. Direct indexing does.


# ================================================================
# SECTION 4: STRING IMMUTABILITY
# ================================================================

def string_immutability():
    s = "hello"

    # Incorrect:
    # s[0] = "H"

    # Correct: construct a new string.
    s = "H" + s[1:]
    print(s)  # Hello

    # Another approach: convert to a list.
    characters = list("hello")
    characters[0] = "H"

    s = "".join(characters)
    print(s)  # Hello

    # Repeated string concatenation can be inefficient because
    # each concatenation may create a new string.
    #
    # For many pieces, prefer collecting them in a list and
    # joining them once with ''.join(pieces).


# ================================================================
# SECTION 5: IMPORTANT BUILT-IN STRING METHODS
# ================================================================

def string_methods():
    s = "  Hello Python World  "

    # Case conversion.
    print(s.upper())
    print(s.lower())
    print(s.title())
    print(s.capitalize())
    print("PyThOn".swapcase())

    # Removing whitespace.
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    # Searching.
    text = "programming"
    print(text.find("gram"))       # Starting index or -1
    print(text.find("xyz"))        # -1
    print(text.count("m"))         # Number of occurrences
    print(text.startswith("pro"))  # True
    print(text.endswith("ing"))    # True

    # Replacement.
    print("banana".replace("a", "o"))
    print("banana".replace("a", "o", 2))

    # Splitting and joining.
    sentence = "Python is easy"
    words = sentence.split()

    print(words)
    print("-".join(words))

    # Character classification.
    print("123".isdigit())
    print("abc".isalpha())
    print("abc123".isalnum())
    print("   ".isspace())
    print("python".islower())
    print("PYTHON".isupper())

    # Checking whether a string contains a substring.
    print("thon" in "Python")
    print("java" not in "Python")

    # IMPORTANT:
    # String methods generally return new strings.
    # They do not modify the original string in place.


# ================================================================
# SECTION 6: CHARACTER CODES AND CASE CONVERSION
# ================================================================

def character_operations():
    # ord(character) gives the Unicode code point.
    print(ord("A"))  # 65
    print(ord("a"))  # 97

    # chr(number) converts a code point into a character.
    print(chr(65))   # A
    print(chr(97))   # a

    # ASCII-based lowercase conversion for English letters.
    character = "B"

    if "A" <= character <= "Z":
        lowercase = chr(ord(character) + 32)
        print(lowercase)  # b

    # Prefer built-in methods for normal text processing.
    print("HELLO".lower())


# ================================================================
# SECTION 7: COUNT CHARACTERS USING A DICTIONARY
# ================================================================

def character_frequency(s):
    """
    Count the frequency of each character.

    Time Complexity: O(n) average
    Space Complexity: O(k)

    n = length of string
    k = number of distinct characters
    """

    frequency = {}

    for character in s:
        # Add a new character with frequency 1.
        # Otherwise, increase its existing frequency.
        frequency[character] = frequency.get(character, 0) + 1

    return frequency


# ================================================================
# SECTION 8: COUNT CHARACTERS USING COLLECTIONS.COUNTER
# ================================================================

from collections import Counter


def character_frequency_counter(s):
    """
    Counter is a convenient built-in tool for frequency counting.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    return Counter(s)


# ================================================================
# SECTION 9: REVERSE A STRING
# ================================================================

def reverse_string(s):
    """
    Approach 1: Slicing.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    return s[::-1]


def reverse_string_two_pointers(s):
    """
    Approach 2: Two pointers on a character list.

    A Python string is immutable, so we convert it to a list.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    characters = list(s)

    left = 0
    right = len(characters) - 1

    while left < right:
        characters[left], characters[right] = (
            characters[right],
            characters[left]
        )

        left += 1
        right -= 1

    return "".join(characters)


# ================================================================
# SECTION 10: CHECK WHETHER A STRING IS A PALINDROME
# ================================================================

def is_palindrome(s):
    """
    A palindrome reads the same forward and backward.

    Examples:
        "madam" -> True
        "racecar" -> True
        "hello" -> False

    Time Complexity: O(n)
    Space Complexity: O(1) auxiliary space
    """

    left = 0
    right = len(s) - 1

    while left < right:

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_ignore_case_and_spaces(s):
    """
    Ignore case and non-alphanumeric characters.

    Examples:
        "A man, a plan, a canal: Panama" -> True
        "race a car" -> False

    This version creates a cleaned string.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    cleaned = "".join(
        character.lower()
        for character in s
        if character.isalnum()
    )

    return cleaned == cleaned[::-1]


# ================================================================
# SECTION 11: COUNT VOWELS AND CONSONANTS
# ================================================================

def count_vowels_consonants(s):
    """
    Count English vowels and consonants.

    Non-English letters, digits, spaces, and symbols are ignored.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    vowels = set("aeiou")
    vowel_count = 0
    consonant_count = 0

    for character in s.lower():

        if "a" <= character <= "z":

            if character in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# ================================================================
# SECTION 12: REMOVE DUPLICATE CHARACTERS
# ================================================================

def remove_duplicate_characters(s):
    """
    Keep the first occurrence of each character.

    Example:
        "programming" -> "progamin"

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    seen = set()
    result = []

    for character in s:

        if character not in seen:
            seen.add(character)
            result.append(character)

    return "".join(result)


# ================================================================
# SECTION 13: CHECK WHETHER TWO STRINGS ARE ANAGRAMS
# ================================================================

def are_anagrams(s1, s2):
    """
    Anagrams contain exactly the same characters with the same
    frequencies, regardless of order.

    Examples:
        "listen", "silent" -> True
        "hello", "world" -> False

    This implementation is case-sensitive and treats spaces
    as ordinary characters.

    Time Complexity: O(n + m) average
    Space Complexity: O(k)
    """

    return Counter(s1) == Counter(s2)


def are_anagrams_ignore_case_and_spaces(s1, s2):
    """
    Case-insensitive anagram check that ignores non-alphanumeric
    characters.

    Time Complexity: O(n + m)
    Space Complexity: O(k)
    """

    cleaned1 = "".join(
        c.lower() for c in s1 if c.isalnum()
    )

    cleaned2 = "".join(
        c.lower() for c in s2 if c.isalnum()
    )

    return Counter(cleaned1) == Counter(cleaned2)


# ================================================================
# SECTION 14: FIRST NON-REPEATING CHARACTER
# ================================================================

def first_non_repeating_character(s):
    """
    Return the first character that appears exactly once.
    Return None if no such character exists.

    Example:
        "aabbcdd" -> "c"
        "aabb" -> None

    Approach:
        1. Count every character.
        2. Scan the string again in original order.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    frequency = Counter(s)

    for character in s:

        if frequency[character] == 1:
            return character

    return None


def first_unique_character_index(s):
    """
    Return the index of the first non-repeating character.
    Return -1 if no unique character exists.

    This is a common interview problem.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    frequency = Counter(s)

    for index, character in enumerate(s):

        if frequency[character] == 1:
            return index

    return -1


# ================================================================
# SECTION 15: REVERSE WORDS IN A SENTENCE
# ================================================================

def reverse_words(s):
    """
    Reverse the order of words.

    Example:
        "Python is very useful"
        -> "useful very is Python"

    Extra spaces are removed and words are separated by one space.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    words = s.split()
    words.reverse()

    return " ".join(words)


def reverse_each_word(s):
    """
    Reverse every word without changing the word order.

    Example:
        "hello world" -> "olleh dlrow"

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    words = s.split()

    reversed_words = [
        word[::-1]
        for word in words
    ]

    return " ".join(reversed_words)


# ================================================================
# SECTION 16: LONGEST COMMON PREFIX
# ================================================================

def longest_common_prefix(strings):
    """
    Find the longest prefix shared by every string.

    Example:
        ["flower", "flow", "flight"] -> "fl"

    Approach:
        Start with the first string as the candidate prefix.
        Shorten it until every string begins with that prefix.

    Let:
        n = number of strings
        m = length of the shortest string

    Time Complexity: O(n * m) worst case
    Space Complexity: O(1) auxiliary space
    """

    if not strings:
        return ""

    prefix = strings[0]

    for word in strings[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix


# ================================================================
# SECTION 17: CHECK WHETHER ONE STRING IS A SUBSEQUENCE OF ANOTHER
# ================================================================

def is_subsequence(s, t):
    """
    Check whether s is a subsequence of t.

    A subsequence preserves character order but does not need
    to preserve adjacency.

    Example:
        s = "ace"
        t = "abcde"
        Result: True

    Example:
        s = "aec"
        t = "abcde"
        Result: False

    Time Complexity: O(len(t))
    Space Complexity: O(1)
    """

    i = 0

    for character in t:

        if i < len(s) and s[i] == character:
            i += 1

    return i == len(s)


# ================================================================
# SECTION 18: STRING COMPRESSION
# ================================================================

def compress_string(s):
    """
    Compress consecutive repeated characters.

    Example:
        "aaabbcccc" -> "a3b2c4"
        "abcd" -> "a1b1c1"

    Note:
        This function always includes counts, including 1.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            count += 1

        else:
            result.append(s[i - 1])
            result.append(str(count))

            count = 1

    # Process the final group, which the loop does not emit.
    result.append(s[-1])
    result.append(str(count))

    return "".join(result)


# ================================================================
# SECTION 19: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ================================================================

def length_of_longest_substring(s):
    """
    Find the length of the longest substring with unique characters.

    Examples:
        "abcabcbb" -> 3
        "bbbbb" -> 1
        "pwwkew" -> 3
        "" -> 0

    A substring must consist of consecutive characters.

    Technique: Sliding Window + Hash Map.

    Maintain:
        left  = start of the current window
        right = current character index
        last_seen = most recent index of each character

    If a character repeats inside the current window,
    move left just beyond its previous occurrence.

    IMPORTANT:
        left = max(left, last_seen[character] + 1)

        The max prevents the window's left boundary from
        moving backward.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """

    left = 0
    longest = 0
    last_seen = {}

    for right, character in enumerate(s):

        if character in last_seen:
            left = max(
                left,
                last_seen[character] + 1
            )

        last_seen[character] = right

        current_length = right - left + 1
        longest = max(longest, current_length)

    return longest


# ================================================================
# SECTION 20: LONGEST SUBSTRING WITH AT MOST K DISTINCT CHARACTERS
# ================================================================

def longest_substring_at_most_k_distinct(s, k):
    """
    Return the length of the longest substring containing
    at most k distinct characters.

    Example:
        s = "eceba", k = 2
        Result: 3, because "ece" is valid.

    Technique: Sliding Window + Frequency Map.

    Expand the right boundary.
    If the number of distinct characters exceeds k,
    shrink the left boundary until the window is valid.

    Time Complexity: O(n) average
    Space Complexity: O(k) for a bounded window's frequency map,
    up to O(n) in general if k is not bounded by a constant.
    """

    if k <= 0:
        return 0

    left = 0
    longest = 0
    frequency = {}

    for right, character in enumerate(s):

        frequency[character] = (
            frequency.get(character, 0) + 1
        )

        while len(frequency) > k:

            left_character = s[left]
            frequency[left_character] -= 1

            if frequency[left_character] == 0:
                del frequency[left_character]

            left += 1

        longest = max(
            longest,
            right - left + 1
        )

    return longest


# ================================================================
# SECTION 21: CHECK WHETHER TWO STRINGS ARE ISOMORPHIC
# ================================================================

def are_isomorphic(s, t):
    """
    Two strings are isomorphic if characters can be mapped
    consistently from one string to the other.

    Examples:
        "egg", "add" -> True
        "foo", "bar" -> False
        "paper", "title" -> True

    A character must always map to the same character.
    Two different source characters cannot map to the same
    target character.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """

    if len(s) != len(t):
        return False

    mapping = {}
    reverse_mapping = {}

    for c1, c2 in zip(s, t):

        if c1 in mapping and mapping[c1] != c2:
            return False

        if c2 in reverse_mapping and reverse_mapping[c2] != c1:
            return False

        mapping[c1] = c2
        reverse_mapping[c2] = c1

    return True


# ================================================================
# SECTION 22: GROUP ANAGRAMS
# ================================================================

def group_anagrams(words):
    """
    Group words that are anagrams of one another.

    Example:
        ["eat", "tea", "tan", "ate", "nat", "bat"]

    Possible result:
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    Approach:
        Sort each word to produce a canonical key.

        "eat" -> "aet"
        "tea" -> "aet"
        "ate" -> "aet"

        Words with the same key belong to the same group.

    Let:
        n = number of words
        m = maximum word length

    Time Complexity: O(n * m log m)
    Space Complexity: O(n * m), including stored groups and keys.
    """

    groups = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# ================================================================
# SECTION 23: VALID PARENTHESES
# ================================================================

def is_valid_parentheses(s):
    """
    Check whether brackets are correctly matched and nested.

    Examples:
        "()" -> True
        "()[]{}" -> True
        "(]" -> False
        "([)]" -> False
        "{[]}" -> True

    Technique: Stack.

    Why a stack?
        The most recently opened bracket must be closed first.
        This is a Last-In, First-Out (LIFO) requirement.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    stack = []

    matching_open = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    opening = set("([{")

    for character in s:

        if character in opening:
            stack.append(character)

        elif character in matching_open:

            if not stack:
                return False

            if stack[-1] != matching_open[character]:
                return False

            stack.pop()

        else:
            # This version expects only bracket characters.
            return False

    # An empty stack means all brackets were matched.
    return len(stack) == 0


# ================================================================
# SECTION 24: LONGEST PALINDROMIC SUBSTRING
# ================================================================

def longest_palindromic_substring(s):
    """
    Return the longest contiguous substring that is a palindrome.

    Examples:
        "babad" -> "bab" or "aba"
        "cbbd" -> "bb"
        "a" -> "a"

    Technique: Expand Around Center.

    A palindrome can have:
        1. One center character: "racecar"
        2. Two center characters: "abba"

    There are 2*n - 1 possible centers.

    Time Complexity: O(n^2)
    Space Complexity: O(1) auxiliary space
    """

    if not s:
        return ""

    start = 0
    longest_length = 1

    def expand(left, right):
        """
        Expand while both characters match.

        Return the boundaries of the palindrome.
        """

        while (
            left >= 0
            and right < len(s)
            and s[left] == s[right]
        ):
            left -= 1
            right += 1

        # The last expansion went one position too far
        # on each side.
        return left + 1, right - 1

    for center in range(len(s)):

        # Odd-length palindrome.
        left1, right1 = expand(center, center)

        length1 = right1 - left1 + 1

        if length1 > longest_length:
            start = left1
            longest_length = length1

        # Even-length palindrome.
        left2, right2 = expand(center, center + 1)

        length2 = right2 - left2 + 1

        if length2 > longest_length:
            start = left2
            longest_length = length2

    return s[start:start + longest_length]


# ================================================================
# SECTION 25: LONGEST COMMON SUBSEQUENCE (LCS)
# ================================================================

def longest_common_subsequence(s1, s2):
    """
    Return the length of the longest common subsequence.

    Example:
        s1 = "abcde"
        s2 = "ace"
        Result: 3

    The common subsequence is "ace".

    A subsequence preserves order but need not be contiguous.

    Dynamic Programming:
        dp[i][j] = LCS length using the first i characters
                   of s1 and the first j characters of s2.

    Recurrence:
        If s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        Otherwise:
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i][j - 1]
            )

    Time Complexity: O(n * m)
    Space Complexity: O(n * m)
    """

    n = len(s1)
    m = len(s2)

    # An extra row and column represent empty prefixes.
    dp = [
        [0] * (m + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):

        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:

                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[n][m]


# ================================================================
# SECTION 26: EDIT DISTANCE
# ================================================================

def edit_distance(s1, s2):
    """
    Find the minimum number of operations needed to transform
    s1 into s2.

    Allowed operations:
        1. Insert a character.
        2. Delete a character.
        3. Replace a character.

    Examples:
        "horse", "ros" -> 3
        "intention", "execution" -> 5

    Dynamic Programming:
        dp[i][j] = minimum operations to transform the first
                   i characters of s1 into the first j
                   characters of s2.

    If characters match:
        dp[i][j] = dp[i - 1][j - 1]

    Otherwise:
        dp[i][j] = 1 + min(
            dp[i - 1][j],     # Delete
            dp[i][j - 1],     # Insert
            dp[i - 1][j - 1]  # Replace
        )

    Time Complexity: O(n * m)
    Space Complexity: O(n * m)
    """

    n = len(s1)
    m = len(s2)

    dp = [
        [0] * (m + 1)
        for _ in range(n + 1)
    ]

    # Transforming a string into an empty string requires
    # deleting all its characters.
    for i in range(n + 1):
        dp[i][0] = i

    # Transforming an empty string requires inserting
    # every character of the target string.
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):

        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1]

            else:

                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )

    return dp[n][m]


# ================================================================
# SECTION 27: RUN-LENGTH ENCODING
# ================================================================

def run_length_encoding(s):
    """
    Encode consecutive repeated characters as character + count.

    Example:
        "aaabbcccc" -> "a3b2c4"

    This resembles string compression, but it is presented
    separately as a standard encoding pattern.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            count += 1

        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1

    result.append(f"{s[-1]}{count}")

    return "".join(result)


# ================================================================
# SECTION 28: CHECK WHETHER A STRING CONTAINS ONLY DIGITS
# ================================================================

def contains_only_digits(s):
    """
    Check whether a non-empty string contains only decimal digits.

    Examples:
        "12345" -> True
        "12a45" -> False
        "" -> False

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    return bool(s) and s.isdigit()


# ================================================================
# SECTION 29: STRING TO INTEGER (BASIC VERSION)
# ================================================================

def string_to_integer(s):
    """
    Convert a string containing an optional sign and digits
    into an integer.

    Examples:
        "123" -> 123
        "-42" -> -42
        "+17" -> 17

    This is a basic parser:
        - Leading and trailing whitespace are removed.
        - An optional + or - sign is allowed.
        - At least one digit is required.
        - Other characters cause ValueError.

    Python's int() already handles this use case. This function
    demonstrates the underlying digit-by-digit logic.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    s = s.strip()

    if not s:
        raise ValueError("Empty string is not a valid integer")

    sign = 1
    index = 0

    if s[0] == "-":
        sign = -1
        index = 1

    elif s[0] == "+":
        index = 1

    if index == len(s):
        raise ValueError("Sign must be followed by digits")

    number = 0

    for character in s[index:]:

        if not ("0" <= character <= "9"):
            raise ValueError("Invalid integer string")

        digit = ord(character) - ord("0")

        number = number * 10 + digit

    return sign * number


# ================================================================
# SECTION 30: CHECK WHETHER A STRING IS A ROTATION OF ANOTHER
# ================================================================

def is_rotation(s1, s2):
    """
    Check whether s2 is a rotation of s1.

    Example:
        "abcd", "cdab" -> True
        "abcd", "acbd" -> False

    Key observation:
        If s2 is a rotation of s1, it must appear inside s1 + s1.

    Example:
        s1 = "abcd"
        s1 + s1 = "abcdabcd"
        "cdab" appears inside it.

    Time Complexity: O(n) average with Python's substring search
    Space Complexity: O(n)
    """

    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)


# ================================================================
# SECTION 31: FIND THE FIRST OCCURRENCE OF A SUBSTRING
# ================================================================

def find_substring(text, pattern):
    """
    Return the first index where pattern occurs in text.
    Return -1 if it does not occur.

    This implementation uses Python's built-in find().

    Time complexity:
        Depends on the implementation of Python's substring search.
        Do not assume that every substring search is O(n).

    Space Complexity: O(1) auxiliary space in typical use.
    """

    return text.find(pattern)


# ================================================================
# SECTION 32: BASIC SUBSTRING SEARCH USING NAIVE ALGORITHM
# ================================================================

def naive_substring_search(text, pattern):
    """
    Find the first occurrence of pattern in text.

    Try every possible starting position and compare characters.

    Example:
        text = "hello world"
        pattern = "world"
        Result: 6

    Let:
        n = len(text)
        m = len(pattern)

    Time Complexity: O(n * m) worst case
    Space Complexity: O(1) auxiliary space

    Empty-pattern convention:
        Return 0, matching Python's find() behavior.
    """

    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    if m > n:
        return -1

    for start in range(n - m + 1):

        matched = True

        for j in range(m):

            if text[start + j] != pattern[j]:
                matched = False
                break

        if matched:
            return start

    return -1


# ================================================================
# SECTION 33: KMP STRING SEARCH
# ================================================================

def build_lps(pattern):
    """
    Build the Longest Proper Prefix which is also a Suffix array.

    lps[i] is the length of the longest proper prefix of
    pattern[0:i+1] that is also a suffix of that substring.

    "Proper prefix" means the prefix cannot be the entire string.

    Example:
        pattern = "ababaca"

    The LPS array is:
        [0, 0, 1, 2, 3, 0, 1]

    Time Complexity: O(m)
    Space Complexity: O(m)
    """

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length
            i += 1

        elif length > 0:

            # Fall back to a shorter prefix that is also
            # a suffix of the matched portion.
            length = lps[length - 1]

        else:

            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    """
    Knuth-Morris-Pratt substring search.

    Returns the first index where pattern occurs in text,
    or -1 if it does not occur.

    Why KMP?
        When a mismatch occurs, KMP uses the LPS array to avoid
        comparing characters that are already known to match.

    Time Complexity: O(n + m)
    Space Complexity: O(m)
    """

    if pattern == "":
        return 0

    lps = build_lps(pattern)

    i = 0  # Index in text.
    j = 0  # Index in pattern.

    while i < len(text):

        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j

        elif j > 0:

            # Keep i in place; reuse previous match information.
            j = lps[j - 1]

        else:

            # No prefix matched, so move to the next text character.
            i += 1

    return -1


# ================================================================
# SECTION 34: COMMON STRING PATTERNS — SUMMARY
# ================================================================

def string_patterns_summary():
    """
    Quick reference for choosing an algorithm.

    1. Two Pointers
       - Palindrome checking
       - Reversing a character list
       - Comparing from both ends

    2. Hash Map / Frequency Counter
       - Anagrams
       - Character frequencies
       - First unique character
       - Isomorphic strings

    3. Sliding Window
       - Longest substring without repeating characters
       - Longest substring with at most k distinct characters
       - Fixed-size substring problems

    4. Stack
       - Valid parentheses
       - Nested brackets
       - Parsing nested structures

    5. Dynamic Programming
       - Longest common subsequence
       - Edit distance
       - Other sequence-comparison problems

    6. Expand Around Center
       - Longest palindromic substring

    7. String Matching
       - Naive substring search
       - KMP

    8. Sorting / Canonical Keys
       - Grouping anagrams

    9. Built-in String Operations
       - split(), join(), strip(), replace(), find()

    IMPORTANT:
        Select the pattern based on the problem's requirements,
        not merely because the input is a string.
    """
    pass


# ================================================================
# SECTION 35: EDGE-CASE TESTING
# ================================================================

def run_edge_case_tests():
    """
    Test empty strings, single characters, repeated characters,
    and other boundary cases.
    """

    # Reverse string.
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("abc") == "cba"

    # Palindrome.
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("abc") is False

    # Character frequency.
    assert character_frequency("") == {}
    assert character_frequency("aab") == {
        "a": 2,
        "b": 1
    }

    # Anagrams.
    assert are_anagrams("", "") is True
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("hello", "world") is False

    # First unique character.
    assert first_unique_character_index("leetcode") == 0
    assert first_unique_character_index("aabb") == -1
    assert first_unique_character_index("") == -1

    # Longest substring without repeating characters.
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3

    # At most k distinct characters.
    assert longest_substring_at_most_k_distinct("eceba", 2) == 3
    assert longest_substring_at_most_k_distinct("abc", 0) == 0
    assert longest_substring_at_most_k_distinct("", 2) == 0

    # Longest common prefix.
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    # Subsequence.
    assert is_subsequence("", "abc") is True
    assert is_subsequence("ace", "abcde") is True
    assert is_subsequence("aec", "abcde") is False

    # String rotation.
    assert is_rotation("abcd", "cdab") is True
    assert is_rotation("abcd", "acbd") is False
    assert is_rotation("", "") is True

    # Longest palindromic substring.
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("cbbd") == "bb"

    # Dynamic programming.
    assert longest_common_subsequence("abcde", "ace") == 3
    assert edit_distance("horse", "ros") == 3

    # Substring search.
    assert naive_substring_search("hello", "ll") == 2
    assert naive_substring_search("hello", "xyz") == -1
    assert kmp_search("hello", "ll") == 2
    assert kmp_search("hello", "xyz") == -1

    print("All edge-case tests passed!")


# ================================================================
# SECTION 36: DEMONSTRATION
# ================================================================

if __name__ == "__main__":

    print("=" * 60)
    print("          PYTHON STRINGS: DSA REVISION")
    print("=" * 60)

    text = "programming"

    print("\n1. Basic String Operations")
    print("Original:", text)
    print("Length:", len(text))
    print("Reverse:", reverse_string(text))

    print("\n2. Character Frequency")
    print(character_frequency(text))

    print("\n3. Palindrome")
    print("madam:", is_palindrome("madam"))
    print("hello:", is_palindrome("hello"))

    print("\n4. Vowels and Consonants")
    print(count_vowels_consonants("Hello Python"))

    print("\n5. Remove Duplicates")
    print(remove_duplicate_characters("programming"))

    print("\n6. Anagrams")
    print(are_anagrams("listen", "silent"))

    print("\n7. First Non-Repeating Character")
    print(first_non_repeating_character("aabbcdd"))

    print("\n8. Reverse Words")
    print(reverse_words("Python is very useful"))

    print("\n9. Longest Common Prefix")
    print(longest_common_prefix(
        ["flower", "flow", "flight"]
    ))

    print("\n10. Subsequence")
    print(is_subsequence("ace", "abcde"))

    print("\n11. String Compression")
    print(compress_string("aaabbcccc"))

    print("\n12. Longest Substring Without Repetition")
    print(length_of_longest_substring("abcabcbb"))

    print("\n13. At Most K Distinct Characters")
    print(longest_substring_at_most_k_distinct("eceba", 2))

    print("\n14. Isomorphic Strings")
    print(are_isomorphic("egg", "add"))

    print("\n15. Group Anagrams")
    print(group_anagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ))

    print("\n16. Valid Parentheses")
    print(is_valid_parentheses("({[]})"))

    print("\n17. Longest Palindromic Substring")
    print(longest_palindromic_substring("babad"))

    print("\n18. Longest Common Subsequence")
    print(longest_common_subsequence("abcde", "ace"))

    print("\n19. Edit Distance")
    print(edit_distance("horse", "ros"))

    print("\n20. String to Integer")
    print(string_to_integer("-12345"))

    print("\n21. String Rotation")
    print(is_rotation("abcd", "cdab"))

    print("\n22. Naive Substring Search")
    print(naive_substring_search("hello world", "world"))

    print("\n23. KMP Search")
    print(kmp_search("ababcabcabababd", "ababd"))

    print("\n24. Edge-Case Tests")
    run_edge_case_tests()

    print("\n" + "=" * 60)
    print("             REVISION COMPLETED")
    print("=" * 60)
