# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(n, d):
            if not n:
                return d
            return max(dfs(n.left, d + 1), dfs(n.right, d + 1))

        return dfs(root, 0)
