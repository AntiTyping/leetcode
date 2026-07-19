# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.diff = float('inf')
        self.targetVal = None

        def dfs(node):
            if not node:
                return

            if abs(node.val - target) == self.diff:
                self.diff = abs(node.val - target)
                self.targetVal = min(node.val, self.targetVal)

            if abs(node.val - target) < self.diff:
                self.diff = abs(node.val - target)
                self.targetVal = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.targetVal
