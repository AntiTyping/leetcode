# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        # func: returns max profit
        # state: node, bool
        # orders: forward
        # rec:
        #    if parent robbed: skip both childere
        #.   if parent not robbed:
        #.       skip
        #.       rob
        @cache
        def dp(root, robbed_parent):
            if root is None:
                return 0
            skip = 0
            rob = 0
            if robbed_parent:
                skip = dp(root.left, False) +  dp(root.right, False)
            else:
                skip = dp(root.left, False) +  dp(root.right, False)
                rob = root.val + dp(root.left, True) + dp(root.right, True)
            return max(skip, rob)

        return max(dp(root, True), dp(root, False))