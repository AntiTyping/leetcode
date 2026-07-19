# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if not node:
                return 0
            ans = 0
            if low <= node.val and node.val <= high:
                ans += node.val

            L = dfs(node.left)
            R = dfs(node.right)

            return ans + L + R

        return dfs(root)