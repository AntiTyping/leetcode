class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # memo = [-1] * len(nums)

        # def dp(i):
        #     if memo[i] > -1:
        #         return memo[i]

        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[:2])

        #     memo[i] = max(dp(i-1), dp(i-2) + nums[i])

        #     return memo[i]

        # return dp(len(nums)-1)

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[len(nums) - 1]