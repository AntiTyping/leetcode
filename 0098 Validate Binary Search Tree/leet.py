# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # arrya
        # min/max
        # params

        def dfs(node, small, large):
            if not node:
                return True

            L = dfs(node.left, small, node.val)
            R = dfs(node.right, node.val, large)
            if L and R and small < node.val and node.val < large:
                return True
            return False


        return dfs(root, -float('inf'), float('inf'))