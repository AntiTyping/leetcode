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

            if low < node.val:
                ans += dfs(node.left)
            if node.val < high:
                ans += dfs(node.right)

            return ans

        return dfs(root)