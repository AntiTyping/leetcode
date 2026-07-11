# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return head

        curr = head
        for i in range(left-2):
            curr = curr.next
        end = curr # 1
        l = end.next # 2
        if l == 1:
            l = head

        for i in range(right - left + 1):
            curr = curr.next
        r = curr # 4
        if curr:
            rest = curr.next # 5
        else:
            rest = None

        # reverse
        # l -> r
        prev = rest #5 -> 6
        curr = l #2 -> 3
        for i in range(right - left + 1):
            tmp = curr.next # 3 -> 4; # 4 -> 5; 5 -> None
            curr.next = prev # 2 -> 5; 3 -> 2; 4 -> 3
            prev = curr # 2 -> 5; 3 -> 2; 4 -> 3
            curr = tmp # # 3 -> 4; 4 -> 5; 5 -> None

            # 1 -> 2 -> 5  3 - > 4 -> 5
            # 1 -> 2 -> 5  3 -> 2  4 -> 5
            # 1 -> 2 -> 5  4 -> 3 -> 2

        end.next = prev

        return head