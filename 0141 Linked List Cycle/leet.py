# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        s = set()

        node = head

        while True:
            if node is None:
                return False
            if node in s:
                return True
            s.add(node)
            node = node.next

