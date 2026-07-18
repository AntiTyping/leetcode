# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            node, sum = stack.pop()

            if not node.left and not node.right:
                if sum + node.val == targetSum:
                    return True

            if node.left:
                stack.append((node.left, sum + node.val))
            if node.right:
                stack.append((node.right, sum + node.val))
        return False
