class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [1] * len(nums)

        for r in range(1, len(nums)):
            for l in range(0, r):
                if nums[r] > nums[l]:
                    dp[r] = max(dp[r], 1 + dp[l])

        return max(dp)

