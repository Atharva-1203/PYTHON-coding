# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:
            size = len(q)
            level_sum = 0

            for i in range(size):
                node = q.popleft()

                level_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(float(level_sum) / size)

        return ans

        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        