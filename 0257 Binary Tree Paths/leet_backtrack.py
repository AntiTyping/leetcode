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

        def backtrack(curr):
            if not curr[-1].left and not curr[-1].right:
                vals = []
                for n in curr:
                    vals.append(str(n.val))
                out.append("->".join(vals))

            n = curr[-1]
            if n.left:
                curr.append(n.left)
                backtrack(curr)
                curr.pop()
            if n.right:
                curr.append(n.right)
                backtrack(curr)
                curr.pop()

        backtrack([root])
        return out

