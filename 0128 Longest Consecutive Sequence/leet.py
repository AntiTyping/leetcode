class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()

        max_ = 1
        n = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                n += 1
                if n > max_:
                    max_ = n
            elif nums[i - 1] == nums[i]:
                None
            else:
                n = 1

        return max_
