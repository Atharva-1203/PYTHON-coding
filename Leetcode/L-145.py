# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def post(self, root, ret):
        if root is None:
            return 
        self.post(root.left,ret)
        self.post(root.right,ret)
        ret.append(root.val)

    def postorderTraversal(self, root):
        ans=[]
        self.post(root,ans)
        return ans

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        