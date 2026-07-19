# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')

        def dfs(node): # 100000, 0
            if not node:
                return float('inf')

            dfs(node.left) # 0
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev) # 100000
            self.prev = node.val # 0
            dfs(node.right)

        dfs(root)
        return self.ans
