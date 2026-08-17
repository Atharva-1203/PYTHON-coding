from collections import defaultdict
import heapq 
graph=defaultdict(list)
graph = {
    0: [(1, 4), (2, 1)],
    1: [(0, 4), (3, 2)],
    2: [(0, 1), (3, 3)],
    3: [(1, 2), (2, 3)]
}