# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        q = [root]
        v = []

        # O(n)
        while len(q) > 0:
            n = q.pop()
            v.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        s = set()
        # O(n)
        for n in v:
            diff = k - n
            if diff in s:
                return True
            s.add(n)
        return False

