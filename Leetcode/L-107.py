# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        q=deque([root])
        ans=[]
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
                
            ans.append(level)
        return ans[::-1]



        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        