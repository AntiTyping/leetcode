# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0

        def height(node):
            if not node:
                return 0

            l = height(node.left)
            r = height(node.right)

            nonlocal max_height
            max_height = max(max_height, l + r)

            return 1 + max(l, r)

        height(root)

        return max_height