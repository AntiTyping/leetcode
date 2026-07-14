# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(ancestor, node): # None, 1; 1, 2
            if not node:
                return

            nonlocal ans

            if not ancestor:
                ancestor = root # 1

            if ancestor and node:
                ans = max(ans, abs(ancestor.val - node.val)) # 0

            dfs(ancestor, node.left) # 1, None
            dfs(ancestor, node.right) # 1, 2

        dfs(None, root)

        return ans
