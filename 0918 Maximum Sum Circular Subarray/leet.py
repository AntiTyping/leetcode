class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current = nums[0]
        min_current = nums[0]
        max_sum = nums[0]
        min_sum = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            total += nums[i]
            max_current = max(max_current + num, num)
            max_sum = max(max_sum, max_current)
            min_current = min(min_current + num, num)
            min_sum = min(min_sum, min_current)

        if max_sum < 0:
            return max_sum

        return max(total - min_sum, max_sum)
