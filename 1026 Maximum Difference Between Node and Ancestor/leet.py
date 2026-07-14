# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(max_val, min_val, node): # None, None, 1; 1, 1, 2; 2, 1, 0; 2, 0, 3
            if not node:
                return

            if max_val is None: # do not: if max_val because it can be 0!
                max_val = root.val # 1

            if min_val is None: # do not: if min_val because it can be 0!
                min_val = root.val # 1


            self.ans = max(self.ans, abs(min_val - node.val), abs(max_val - node.val))
            # 0, 0, 0 -> 0; 0, 1, 1 -> 1; 1, 1, 2 -> 2; 2, 3, 1 -> 3

            max_val = max(max_val, node.val) # 1, 1 -> 1; 1, 2 -> 2; 2, 0 -> 2
            min_val = min(min_val, node.val) # 1, 1 -> 1; 1, 2 -> 1; 1, 0 -> 0

            dfs(max_val, min_val, node.left) # 1, 1, None; 2, 1, None; 2, 0, 3
            dfs(max_val, min_val, node.right) # 1, 1, 2; 2, 1, 0

        dfs(None, None, root)

        return self.ans
