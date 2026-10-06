class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))
            return memo[i]

        return dp(len(nums) - 1)