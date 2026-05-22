# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB

        s = set()

        while a != None:
            s.add(a)
            a = a.next
        while b != None:
            if b in s:
                return b
            b = b.next

        return None


