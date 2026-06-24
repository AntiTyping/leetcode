# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None
        k = 0
        fast, slow = head, head
        prev = None
        while fast.next:
            fast = fast.next
            k += 1
            if k >= n:
                prev = slow
                slow = slow.next

        if prev:
            prev.next = slow.next
        else:
            return slow.next

        return head

