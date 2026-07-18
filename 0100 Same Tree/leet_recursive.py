# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def identical(node1, node2):
            if not node1 and not node2:
                return True

            if node1 and node2 and node1.val == node2.val:
                return True
            return False

        def dfs(node1, node2):
            if not identical(node1, node2):
                return False
            if not node1:
                return True

            L = dfs(node1.left, node2.left)
            if not L:
                return False
            R = dfs(node1.right, node2.right)
            if not R:
                return False
            return True

        return dfs(p, q)