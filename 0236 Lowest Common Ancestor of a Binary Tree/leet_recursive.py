# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return None

            # current node is p or q
            if node == p or node == q:
                return node

            L = dfs(node.left)
            R = dfs(node.right)

            # current is the common root
            if L and R:
                return node

            # found node in the left subtree
            if L:
                return L

            # defualt to right or None (not found)
            return R

        return dfs(root)
