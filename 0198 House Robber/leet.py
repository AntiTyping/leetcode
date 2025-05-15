class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maximum: func
        # max for current house: state
        # 1) dp(i) = dp(i-1)
        # 2) dp(i) = nums[i] + dp(i-2)
        # dp(i) = max(dp(i-1), nums[i]+dp(i-2))
        # 0 - num[0]
        # 1 - max(num[0], num[1])

        memo = {}
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i not in memo:
                memo[i] = max(dp(i-1), nums[i] + dp(i-2))

            return memo[i]

        return dp(len(nums) -1)


print(Solution().rob([1,2,3,1]))