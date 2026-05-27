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

        s = set()
        # O(n)
        while len(q) > 0:
            n = q.pop()
            diff = k - n.val
            if diff in s:
                return True
            else:
                s.add(n.val)
            v.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return False

