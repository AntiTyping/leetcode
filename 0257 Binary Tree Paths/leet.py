# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        out = []

        def dfs(node, p):
            p += str(node.val)

            if not node.left and not node.right:
                out.append(p)

            p += "->"

            if node.left:
                dfs(node.left, p)
            if node.right:
                dfs(node.right, p)

        dfs(root, "")

        return out

