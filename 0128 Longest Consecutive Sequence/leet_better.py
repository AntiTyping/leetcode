class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[ijjnt]
        :rtype: int
        """
        s = set(nums)
        max_ = 0

        for n in nums:
            if (n - 1) not in s:
                l = 0
                while n + l in s:
                    l += 1
                max_ = max(l, max_)
                if max_ > len(nums) // 2:
                    return max_

        return max_
