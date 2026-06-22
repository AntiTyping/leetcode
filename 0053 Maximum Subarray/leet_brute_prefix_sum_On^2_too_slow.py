class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        max_sum = prefix_sum[0]
        # O(n^2)
        for i in range(len(nums)):
            # On(n) - needs improvement
            for j in range(i, len(nums)):
                left_sum = prefix_sum[i - 1] if i > 0 else 0
                max_sum = max(max_sum, prefix_sum[j] - left_sum)
        return max_sum
