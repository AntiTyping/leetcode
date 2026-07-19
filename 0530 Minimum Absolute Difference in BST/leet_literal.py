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
                return

            dfs(node.left, stack)
            stack.append(node.val)
            dfs(node.right, stack)

        stack = []
        dfs(root, stack)

        ans = float('inf')
        for i in range(1, len(stack)):
            ans = min(ans, stack[i] - stack[i-1])

        return ans
