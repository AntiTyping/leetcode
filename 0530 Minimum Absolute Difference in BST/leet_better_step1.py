# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def dfs(node, stack):
            if not node:
                return float('inf')

            ans = dfs(node.left, stack)
            if stack:
                ans = min(ans, node.val - stack[-1])
            stack.append(node.val)
            ans = min(ans, dfs(node.right, stack))

            return ans

        stack = []
        return dfs(root, stack)
