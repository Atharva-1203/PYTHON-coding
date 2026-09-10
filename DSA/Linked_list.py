"""
LINKED LISTS — COMPLETE PYTHON GUIDE
=====================================

Goal:
    Study this file from top to bottom. Every important operation is implemented
    from scratch with comments so that you can move from basic linked lists to
    LeetCode/exam problems.

Topics:
    1. Singly Linked List
       - Node creation
       - Traversal
       - Search
       - Update
       - Insert at beginning/end/index
       - Delete beginning/end/index/by value
       - Reverse
       - Length
       - Find middle
       - Detect cycle
       - Remove cycle
       - Merge two sorted lists
       - Remove duplicates
       - Useful patterns

    2. Doubly Linked List
       - prev + next
       - Traversal in both directions
       - Insert/delete at positions

    3. Circular Linked List
       - Circular singly list
       - Traversal
       - Insert/delete

    4. Interview / LeetCode patterns
       - Fast and slow pointers
       - Dummy node
       - Two pointers
       - In-place reversal
       - Merge pattern

IMPORTANT MENTAL MODEL
----------------------
A linked list is NOT an array.

Array:
    [10][5][2][7]
     ↑   ↑   ↑   ↑
    contiguous memory (conceptually)

Linked list:
    10 -> 5 -> 2 -> 7 -> None

Each node stores:
    data  +  address/reference of next node

The "head" variable points to the first node.

If:
    head = a

then:
    head.data       -> data in first node
    head.next       -> second node
    head.next.next  -> third node

Most linked-list questions become easy when you carefully track:
    1. Which node is current?
    2. Which reference points to the next node?
    3. What should each pointer point to AFTER the operation?
"""

# ============================================================
# 1. SINGLY LINKED LIST — BASIC STRUCTURE
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data       # Actual value stored in this node
        self.next = None       # Reference to the next node


# Create three separate nodes.
a = Node(10)
b = Node(5)
c = Node(2)

# Connect them.
a.next = b
b.next = c

# Now the structure is:
#
#   a                 b                 c
#   ↓                 ↓                 ↓
# [10 | next]  ->  [5 | next]  ->  [2 | None]
#
# The head is simply a reference to the first node.

head = a

print("Head:", head.data)
print("Second:", head.next.data)


# ============================================================
# 2. TRAVERSAL
# ============================================================

# Traversal means visiting every node one by one.
#
# NEVER move 'head' itself when you want to preserve the list.
# Use a temporary pointer such as curr.

curr = head

while curr is not None:
    print(curr.data)
    curr = curr.next

# IMPORTANT:
# After this loop, curr becomes None.
# head is still pointing to the first node.


# ============================================================
# 3. HELPER FUNCTIONS
# ============================================================

def print_list(head):
    """Print all values in a singly linked list."""
    curr = head

    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next

    print("None")


def length(head):
    """Return number of nodes."""
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count


def search(head, target):
    """
    Return True if target exists, otherwise False.

    Time: O(n)
    Space: O(1)
    """
    curr = head

    while curr is not None:
        if curr.data == target:
            return True

        curr = curr.next

    return False


# ============================================================
# 4. UPDATE A NODE
# ============================================================

# Updating is easy because we only change the data.
#
# Example:
#
# 10 -> 5 -> 2
#          ↑
# Change 5 to 50
#
# 10 -> 50 -> 2

def update_at_index(head, index, value):
    """
    Change data at a particular index.

    Indexing:
        0 -> first node
        1 -> second node
        2 -> third node

    Returns the (possibly unchanged) head.
    """
    curr = head
    i = 0

    while curr is not None:
        if i == index:
            curr.data = value
            return head

        curr = curr.next
        i += 1

    raise IndexError("Index out of range")


# ============================================================
# 5. INSERTION — THE MOST IMPORTANT POINTER SKILL
# ============================================================

"""
Suppose we have:

10 -> 20 -> 30 -> None

We want to insert 15 between 10 and 20.

Before:
10 -> 20

Create:
new = 15

We need:
new.next = 20
10.next = new

After:
10 -> 15 -> 20 -> 30

ORDER MATTERS.

Correct:
    new.next = curr.next
    curr.next = new

If you do curr.next = new first and then try to use curr.next,
you may lose the original next node.
"""


def insert_at_beginning(head, value):
    """
    Insert a node before the current head.

    Before:
        10 -> 20 -> None

    After:
        5 -> 10 -> 20 -> None

    The NEW node becomes the new head.

    Time: O(1)
    """
    new_node = Node(value)

    new_node.next = head
    head = new_node

    return head


def insert_at_end(head, value):
    """
    Insert after the last node.

    Time: O(n) without a tail pointer.
    """
    new_node = Node(value)

    # Empty list:
    if head is None:
        return new_node

    curr = head

    # Stop at last node.
    while curr.next is not None:
        curr = curr.next

    curr.next = new_node

    return head


def insert_at_index(head, index, value):
    """
    Insert at a zero-based index.

    Example:
        10 -> 20 -> 30

    insert_at_index(head, 1, 15)

        10 -> 15 -> 20 -> 30

    Special case:
        index == 0 means insertion before head.
    """
    if index < 0:
        raise IndexError("Index cannot be negative")

    if index == 0:
        return insert_at_beginning(head, value)

    curr = head

    # We need to reach the node BEFORE the insertion position.
    for _ in range(index - 1):
        if curr is None:
            raise IndexError("Index out of range")
        curr = curr.next

    if curr is None:
        raise IndexError("Index out of range")

    new_node = Node(value)

    # Save the old next node first.
    new_node.next = curr.next

    # Then connect previous node to new node.
    curr.next = new_node

    return head


# ============================================================
# 6. DELETION
# ============================================================

"""
Deletion is mostly about changing references.

Suppose:

10 -> 20 -> 30

Delete 20.

We want:

10 -> 30

So the node before 20 must skip 20:

10.next = 30

The node 20 no longer needs to be connected to the list.

This is the key idea:
    "previous.next = current.next"
"""


def delete_first(head):
    """
    Delete first node.

    Before:
        10 -> 20 -> 30

    After:
        20 -> 30

    Time: O(1)
    """
    if head is None:
        return None

    return head.next


def delete_last(head):
    """
    Delete last node.

    Before:
        10 -> 20 -> 30

    After:
        10 -> 20

    Time: O(n)
    """
    if head is None:
        return None

    # One-node list.
    if head.next is None:
        return None

    curr = head

    # Stop at second-last node.
    while curr.next.next is not None:
        curr = curr.next

    # Remove last node.
    curr.next = None

    return head


def delete_at_index(head, index):
    """
    Delete node at zero-based index.

    Example:
        10 -> 20 -> 30

    delete index 1

        10 -> 30
    """
    if index < 0:
        raise IndexError("Index cannot be negative")

    if head is None:
        raise IndexError("Index out of range")

    if index == 0:
        return head.next

    curr = head

    # Reach node BEFORE target.
    for _ in range(index - 1):
        if curr.next is None:
            raise IndexError("Index out of range")
        curr = curr.next

    if curr.next is None:
        raise IndexError("Index out of range")

    # Skip the node being deleted.
    curr.next = curr.next.next

    return head


def delete_first_occurrence(head, target):
    """
    Delete the first node whose data == target.

    Example:
        10 -> 20 -> 20 -> 30

    target = 20

        10 -> 20 -> 30
    """
    if head is None:
        return None

    # Target is in first node.
    if head.data == target:
        return head.next

    curr = head

    while curr.next is not None:
        if curr.next.data == target:
            curr.next = curr.next.next
            return head

        curr = curr.next

    return head


# ============================================================
# 7. REVERSE A SINGLY LINKED LIST
# ============================================================

"""
THIS IS ONE OF THE MOST IMPORTANT LINKED-LIST PROBLEMS.

Given:
    1 -> 2 -> 3 -> None

Return:
    3 -> 2 -> 1 -> None

Use three pointers:

    prev
    curr
    next_node

At each step:

    next_node = curr.next       # Save future
    curr.next = prev            # Reverse arrow
    prev = curr                 # Move prev
    curr = next_node            # Move curr

Visualization:

Initially:
    prev = None
    curr = 1

Step:
    1 -> 2 -> 3

Save 2
Make:
    1 -> None

Move:
    prev = 1
    curr = 2

Repeat.

At the end:
    prev is the NEW HEAD.
"""


def reverse(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next

        curr.next = prev

        prev = curr
        curr = next_node

    return prev


# ============================================================
# 8. FIND MIDDLE — FAST AND SLOW POINTER
# ============================================================

"""
Use two pointers:

slow -> moves 1 step
fast -> moves 2 steps

When fast reaches the end,
slow is around the middle.

Example:
    1 -> 2 -> 3 -> 4 -> 5

slow:
    1 -> 2 -> 3

fast:
    1 -> 3 -> 5 -> None

slow = 3

For an even-length list, this standard implementation returns
the SECOND middle.

Example:
    1 -> 2 -> 3 -> 4

answer = 3
"""


def find_middle(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# ============================================================
# 9. DETECT CYCLE — FLOYD'S ALGORITHM
# ============================================================

"""
A normal list ends at None:

1 -> 2 -> 3 -> 4 -> None

A cyclic list eventually points backward:

1 -> 2 -> 3 -> 4
         ↑       |
         |_______|

If we use:
    slow = slow.next
    fast = fast.next.next

then in a cycle, fast eventually catches slow.

This is called:
    Floyd's Cycle Detection Algorithm

Time: O(n)
Space: O(1)
"""


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# ============================================================
# 10. FIND START OF CYCLE
# ============================================================

"""
After slow and fast meet inside the cycle:

    Put one pointer at head.
    Keep the other at meeting point.

Move both one step at a time.

Where they meet again = cycle starting node.

This is a classic LeetCode pattern.
"""


def cycle_start(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            # Found a meeting point.

            pointer = head

            while pointer is not slow:
                pointer = pointer.next
                slow = slow.next

            return pointer

    return None


# ============================================================
# 11. REMOVE CYCLE
# ============================================================

def remove_cycle(head):
    """
    Remove a cycle if one exists.

    After finding the cycle start, walk around the cycle until
    you find the node whose next points to the cycle start.
    """
    start = cycle_start(head)

    if start is None:
        return head

    curr = start

    while curr.next is not start:
        curr = curr.next

    curr.next = None

    return head


# ============================================================
# 12. MERGE TWO SORTED LINKED LISTS
# ============================================================

"""
Example:

A:
1 -> 4 -> 7

B:
2 -> 3 -> 8

Result:
1 -> 2 -> 3 -> 4 -> 7 -> 8

Use a DUMMY NODE.

Dummy:
    dummy -> ...

tail always points to the last node in the result.

Compare:
    list1.data
    list2.data

Attach smaller node to tail.

At the end attach whatever list remains.

This pattern appears constantly in LeetCode.
"""


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 is not None and list2 is not None:

        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    # One list may still have nodes.
    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next


# ============================================================
# 13. REMOVE DUPLICATES FROM SORTED LIST
# ============================================================

"""
Example:

1 -> 1 -> 2 -> 2 -> 3

Become:

1 -> 2 -> 3

Because the list is sorted, duplicates are next to each other.
"""


def remove_duplicates_sorted(head):
    curr = head

    while curr is not None and curr.next is not None:

        if curr.data == curr.next.data:
            # Skip duplicate.
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


# ============================================================
# 14. DOUBLY LINKED LIST
# ============================================================

"""
Singly linked list node:
    data + next

Doubly linked list node:
    data + prev + next

Example:

None <- 10 <-> 20 <-> 30 -> None

Each node knows:
    previous node
    next node

This makes deletion and backwards traversal easier,
but uses extra memory.
"""


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_doubly_forward(head):
    curr = head

    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.next

    print("None")


def print_doubly_backward(tail):
    curr = tail

    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.prev

    print("None")


def doubly_insert_beginning(head, value):
    """
    Insert at beginning.

    Before:
        None <- 10 <-> 20 -> None

    After:
        None <- 5 <-> 10 <-> 20 -> None

    IMPORTANT:
    Because this is doubly linked, we must update BOTH directions.
    """
    new_node = DNode(value)

    new_node.next = head

    if head is not None:
        head.prev = new_node

    return new_node


def doubly_insert_end(head, value):
    """Insert at end in O(n) if only head is available."""
    new_node = DNode(value)

    if head is None:
        return new_node

    curr = head

    while curr.next is not None:
        curr = curr.next

    curr.next = new_node
    new_node.prev = curr

    return head


def doubly_delete_node(head, node):
    """
    Delete a given node when we already have its reference.

    Key cases:
        1. node is head
        2. node is middle
        3. node is tail

    We reconnect both sides.
    """
    if node is None:
        return head

    if node.prev is not None:
        node.prev.next = node.next
    else:
        # node was head
        head = node.next

    if node.next is not None:
        node.next.prev = node.prev

    # Optional cleanup.
    node.prev = None
    node.next = None

    return head


# ============================================================
# 15. CIRCULAR SINGLY LINKED LIST
# ============================================================

"""
Normal list:
    10 -> 20 -> 30 -> None

Circular list:
    10 -> 20 -> 30
    ↑             |
    |_____________|

The last node points back to the first node.

Therefore:
    curr is never None.

So this is WRONG for a circular list:

    while curr is not None:

Instead, stop when you return to head.
"""


class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_circular(head):
    """Print exactly one full round."""
    if head is None:
        print("Empty")
        return

    curr = head

    while True:
        print(curr.data, end=" -> ")
        curr = curr.next

        if curr is head:
            break

    print("(back to head)")


def circular_insert_end(head, value):
    """
    Insert at end.

    If list is empty:
        new.next = new
        new becomes head
    """
    new_node = CNode(value)

    if head is None:
        new_node.next = new_node
        return new_node

    curr = head

    while curr.next is not head:
        curr = curr.next

    curr.next = new_node
    new_node.next = head

    return head


def circular_insert_beginning(head, value):
    """
    Insert before head.

    The last node must now point to the NEW head.
    """
    new_node = CNode(value)

    if head is None:
        new_node.next = new_node
        return new_node

    curr = head

    while curr.next is not head:
        curr = curr.next

    new_node.next = head
    curr.next = new_node

    return new_node


def circular_delete_value(head, target):
    """
    Delete the first occurrence of target.
    """
    if head is None:
        return None

    # Case: target is at head.
    if head.data == target:

        # Only one node.
        if head.next is head:
            return None

        # Find last node.
        last = head
        while last.next is not head:
            last = last.next

        last.next = head.next
        return head.next

    # Target is not head.
    curr = head

    while curr.next is not head:
        if curr.next.data == target:
            curr.next = curr.next.next
            return head

        curr = curr.next

    return head


# ============================================================
# 16. TAIL POINTER — IMPORTANT OPTIMIZATION
# ============================================================

"""
If you store both:

    head
    tail

then insertion at the end can become O(1).

Without tail:
    walk from head to last node -> O(n)

With tail:
    tail.next = new_node
    tail = new_node

-> O(1)

This is why some linked-list implementations use:

    self.head
    self.tail
    self.size
"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self.size += 1

    def pop_front(self):
        if self.head is None:
            return None

        value = self.head.data
        self.head = self.head.next

        self.size -= 1

        if self.head is None:
            self.tail = None

        return value

    def print_list(self):
        print_list(self.head)


# ============================================================
# 17. TIME COMPLEXITY CHEAT SHEET
# ============================================================

"""
For a normal singly linked list with ONLY head:

Operation                    Time
------------------------------------------------
Access by index              O(n)
Search                       O(n)
Update by index              O(n)
Insert at beginning          O(1)
Insert at end                O(n)
Delete beginning             O(1)
Delete end                   O(n)
Reverse                      O(n)
Find middle                  O(n)
Detect cycle                 O(n)

If a tail pointer is maintained:

Insert at end                O(1)

IMPORTANT:
Linked lists are good when you frequently insert/delete nodes
and already have the relevant node/reference.

Arrays are better for random access because:
    arr[index]
is O(1).

Linked list:
    to reach index 1000, you generally walk through earlier nodes.
"""


# ============================================================
# 18. POINTER PATTERNS YOU MUST MASTER
# ============================================================

"""
PATTERN 1 — NORMAL TRAVERSAL

curr = head

while curr is not None:
    ...
    curr = curr.next


PATTERN 2 — PREVIOUS + CURRENT

prev = None
curr = head

while curr is not None:
    ...
    prev = curr
    curr = curr.next

Useful for:
    deletion
    reversal
    rearrangement


PATTERN 3 — FAST + SLOW

slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

Useful for:
    middle
    cycle detection
    cycle-related problems


PATTERN 4 — DUMMY NODE

dummy = Node(0)
tail = dummy

Useful when:
    the answer's head might change.

Examples:
    merge lists
    remove nodes
    partition lists
    add two numbers


PATTERN 5 — SAVE BEFORE CHANGING

next_node = curr.next
curr.next = prev

Whenever changing links, ask:

    "Am I about to lose access to the rest of the list?"

If yes, save the reference first.
"""


# ============================================================
# 19. CLASSIC LEETCODE PROBLEMS — HOW TO THINK
# ============================================================

"""
1. Reverse Linked List
   Pattern:
       prev + curr

2. Middle of the Linked List
   Pattern:
       slow + fast

3. Linked List Cycle
   Pattern:
       slow + fast

4. Linked List Cycle II
   Pattern:
       slow + fast + reset pointer to head

5. Merge Two Sorted Lists
   Pattern:
       dummy + tail + comparison

6. Remove Nth Node From End
   Pattern:
       two pointers with a gap of n
       often use dummy node

7. Palindrome Linked List
   Pattern:
       find middle
       reverse second half
       compare halves

8. Reorder List
   Pattern:
       find middle
       reverse second half
       merge alternating nodes

9. Intersection of Two Linked Lists
   Pattern:
       two pointers switch heads

10. Add Two Numbers
    Pattern:
       simultaneous traversal + carry

11. Sort List
    Pattern:
       merge sort
       linked lists are naturally suited to merge sort

12. Rotate List
    Pattern:
       find length + connect temporarily into a cycle
"""


# ============================================================
# 20. REMOVE NTH NODE FROM END — IMPORTANT PATTERN
# ============================================================

"""
Example:

1 -> 2 -> 3 -> 4 -> 5

Remove n = 2 from the end.

Answer:

1 -> 2 -> 3 -> 5

Use a dummy node:

dummy -> 1 -> 2 -> 3 -> 4 -> 5

Keep two pointers:
    fast
    slow

Move fast ahead by n+1 positions.

Then move both until fast reaches None.

slow will be just BEFORE the node to delete.

Then:
    slow.next = slow.next.next

The dummy node makes deletion of the head easy.
"""


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    # Create a gap of n nodes.
    for _ in range(n):
        if fast.next is None:
            raise ValueError("n is larger than list length")
        fast = fast.next

    # Move until fast is at the last node.
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    # slow is immediately before target.
    slow.next = slow.next.next

    return dummy.next


# ============================================================
# 21. PALINDROME LINKED LIST
# ============================================================

"""
Example:

1 -> 2 -> 2 -> 1

A palindrome reads the same forward and backward.

Efficient approach:
    1. Find middle.
    2. Reverse second half.
    3. Compare first half and reversed second half.

Time: O(n)
Extra space: O(1)
"""


def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find middle.
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half.
    second = reverse(slow)

    first = head
    curr_second = second

    while curr_second is not None:
        if first.data != curr_second.data:
            return False

        first = first.next
        curr_second = curr_second.next

    return True


# ============================================================
# 22. INTERSECTION OF TWO LINKED LISTS
# ============================================================

"""
Two lists may share actual nodes.

A:
    1 -> 2 \
            8 -> 9
    3 -> 4 /

IMPORTANT:
Intersection means SAME NODE OBJECT,
not merely equal data.

Elegant trick:

pA walks:
    A then B

pB walks:
    B then A

If they intersect, they meet at the intersection.
If not, both become None.
"""


def intersection_node(head_a, head_b):
    p_a = head_a
    p_b = head_b

    while p_a is not p_b:
        if p_a is None:
            p_a = head_b
        else:
            p_a = p_a.next

        if p_b is None:
            p_b = head_a
        else:
            p_b = p_b.next

    return p_a


# ============================================================
# 23. ADD TWO NUMBERS REPRESENTED BY LINKED LISTS
# ============================================================

"""
Example (digits stored in reverse):

2 -> 4 -> 3
5 -> 6 -> 4

Means:
    342 + 465 = 807

Output:
7 -> 0 -> 8

Pattern:
    digit1 + digit2 + carry

Use dummy + tail.
"""


def add_two_numbers(l1, l2):
    dummy = Node(0)
    tail = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry:

        x = l1.data if l1 is not None else 0
        y = l2.data if l2 is not None else 0

        total = x + y + carry

        carry = total // 10
        digit = total % 10

        tail.next = Node(digit)
        tail = tail.next

        if l1 is not None:
            l1 = l1.next

        if l2 is not None:
            l2 = l2.next

    return dummy.next


# ============================================================
# 24. EXAM/INTERVIEW DEBUGGING CHECKLIST
# ============================================================

"""
Whenever a linked-list solution is wrong, check:

[ ] Did I handle an empty list?
[ ] Did I handle a one-node list?
[ ] Did I handle deletion/insertion at head?
[ ] Did I handle deletion/insertion at tail?
[ ] Did I accidentally change head?
[ ] Did I save curr.next before changing curr.next?
[ ] Did I create a cycle accidentally?
[ ] Did I forget to update prev in a doubly linked list?
[ ] Does my loop terminate?
[ ] Am I comparing nodes (is) or their data (==)?
[ ] Is the requested index zero-based?
[ ] Did I return the correct head?
[ ] What happens when n == length?
[ ] What happens when one list is empty?

Most bugs come from edge cases, not from the main idea.
"""


# ============================================================
# 25. PRACTICE BUILD — DO THIS WITHOUT LOOKING
# ============================================================

"""
Try implementing these yourself in this order:

LEVEL 1
-------
1. print_list
2. length
3. search
4. insert_at_beginning
5. insert_at_end
6. delete_first
7. delete_last

LEVEL 2
-------
8. insert_at_index
9. delete_at_index
10. update_at_index
11. reverse
12. find_middle

LEVEL 3
-------
13. has_cycle
14. cycle_start
15. merge_sorted_lists
16. remove_duplicates_sorted
17. remove_nth_from_end

LEVEL 4
-------
18. is_palindrome
19. intersection_node
20. add_two_numbers
21. reorder list
22. sort linked list using merge sort

RULE:
    First draw the list on paper.
    Then draw arrows BEFORE and AFTER every pointer update.

Do not memorize code blindly.
Understand what every arrow means.
"""


# ============================================================
# 26. FINAL CHEAT SHEET
# ============================================================

"""
SINGLY NODE:
    data
    next

DOUBLY NODE:
    data
    prev
    next

NORMAL END:
    next == None

CIRCULAR END:
    next == head

TRAVERSAL:
    curr = curr.next

INSERT AFTER curr:
    new.next = curr.next
    curr.next = new

DELETE AFTER curr:
    curr.next = curr.next.next

REVERSE:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

MIDDLE:
    slow += 1 step
    fast += 2 steps

CYCLE:
    slow + fast

DUMMY:
    dummy.next = head

DELETE TARGET:
    find previous
    previous.next = target.next

DOUBLY DELETE:
    node.prev.next = node.next
    node.next.prev = node.prev

MOST IMPORTANT QUESTION:
    "After this line, where does each pointer point?"

If you can answer that for every line, you understand linked lists.
"""


# ============================================================
# 27. SMALL TEST AREA
# ============================================================

if __name__ == "__main__":
    print("\n--- BASIC TEST ---")

    head = None

    head = insert_at_end(head, 10)
    head = insert_at_end(head, 20)
    head = insert_at_end(head, 30)

    print_list(head)

    head = insert_at_beginning(head, 5)
    print_list(head)

    head = insert_at_index(head, 2, 15)
    print_list(head)

    head = update_at_index(head, 2, 100)
    print_list(head)

    head = delete_at_index(head, 2)
    print_list(head)

    print("Length:", length(head))
    print("Search 20:", search(head, 20))

    head = reverse(head)
    print("Reversed:")
    print_list(head)

    middle = find_middle(head)
    print("Middle:", middle.data if middle else None)

    print("\n--- DOUBLY TEST ---")

    dhead = None
    dhead = doubly_insert_end(dhead, 10)
    dhead = doubly_insert_end(dhead, 20)
    dhead = doubly_insert_end(dhead, 30)

    print_doubly_forward(dhead)

    tail = dhead
    while tail.next:
        tail = tail.next

    print_doubly_backward(tail)

    print("\n--- CIRCULAR TEST ---")

    chead = None
    chead = circular_insert_end(chead, 10)
    chead = circular_insert_end(chead, 20)
    chead = circular_insert_end(chead, 30)

    print_circular(chead)

    chead = circular_insert_beginning(chead, 5)
    print_circular(chead)

    chead = circular_delete_value(chead, 20)
    print_circular(chead)

    print("\n--- DONE ---")
