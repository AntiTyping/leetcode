# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ans = 0
        stack = [(root, -float('inf'))]  # (9, -inf)

        while stack:
            node, m = stack.pop()  # 9, -inf

            if node.val >= m:  # 9 >= -inf
                ans += 1  # 1
            m = max(m, node.val)  #

            if node.left:  # 1; 3
                stack.append((node.left, m))  # (1, 3)
            if node.right:
                stack.append((node.right, m))

        return ans