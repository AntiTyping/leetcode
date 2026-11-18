"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return

        q = [root]

        while q:
            level = len(q)

            for i in range(level - 1):
                q[i].next = q[i + 1]

            for i in range(level):
                a = q.pop(0)
                if a.left is not None:
                    q.append(a.left)
                if a.right is not None:
                    q.append(a.right)

        return root
