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
        if not head:
            return False
        s, f = head, head

        while s and s.next and f and f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True

        return False
