class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        # O(m^3)
        for i in range(len(nums)):
            # O(n^2) - room for improvement
            for j in range(i, len(nums)):
                # O(n)
                max_sum = max(max_sum, sum(nums[i:j+1]))
        return max_sum