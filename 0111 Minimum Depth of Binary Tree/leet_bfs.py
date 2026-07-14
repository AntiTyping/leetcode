# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        d = deque([root])

        n = 1
        while d:
            for i in range(len(d)):
                node = d.popleft()
                if node:
                    if not node.left and not node.right:
                        return n
                    d.append(node.left)
                    d.append(node.right)
            n += 1

        return 0