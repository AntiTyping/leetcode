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

        # O(n)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse
        # O(n)
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # Compare
        # O(n)
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True


