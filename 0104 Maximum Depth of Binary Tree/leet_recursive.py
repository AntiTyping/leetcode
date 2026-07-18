# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, h):
            if not node:
                return 0

            return max(h, dfs(node.left, h + 1), dfs(node.right, h + 1))

        return dfs(root, 1)