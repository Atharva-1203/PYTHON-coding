# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, ret):
        if root is None:
            return
        self.inorder(root.left, ret)
        ret.append(root.val)
        self.inorder(root.right, ret)

    def inorderTraversal(self, root):
        ans=[]
        self.inorder(root, ans)
        return ans

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        