# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        stack = [(root, 1)]

        while stack:
            node, h = stack.pop()
            ans = max(ans, h)
            if node.left:
                stack.append((node.left, h + 1))
            if node.right:
                stack.append((node.right, h + 1))

        return ans

