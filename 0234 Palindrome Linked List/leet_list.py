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
        a = []

        p = head
        while p != None:
            a.append(p.val)
            p = p.next

        l, r = 0, len(a) - 1

        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1

        return True

