class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]



print(Solution().rob([1,2,3,1]))