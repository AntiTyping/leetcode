class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sort, two pointers
        # n log(n)
        s = sorted(nums, key=lambda a: a % 2)
        l, r = 1, len(nums) - 2
        # O(n)
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 2
            r -= 2

        return s
