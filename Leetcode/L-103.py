# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q=deque([root])
        ans=[]
        j=0
        while q:
            size=len(q)
            level=[]
            for i in range(size):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if(j%2==0):
                ans.append(level)
            else:
                ans.append(level[::-1])
            j=j+1
        return ans

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        