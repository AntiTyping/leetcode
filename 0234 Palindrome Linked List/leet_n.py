# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow, fast = head, head

        # find middle
        # n
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse right
        # n
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        l, r = head, prev

        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True


