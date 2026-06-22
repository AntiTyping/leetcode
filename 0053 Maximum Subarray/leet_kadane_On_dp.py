class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_sum = nums[0]
        max_sum = nums[0]
        l, r = 0, 1
        # O(n)
        while r < len(nums):
            if prev_sum < 0:
                prev_sum = 0
                l = r
            prev_sum += nums[r]
            max_sum = max(max_sum, prev_sum)
            r += 1
        return max_sum