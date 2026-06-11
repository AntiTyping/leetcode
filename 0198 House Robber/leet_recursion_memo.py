class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # top down, bottom up
        # tabulation, recursion, hybrid

        memo = {}

        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            else:
                if i in memo:
                    return memo[i]
                else:
                    p = max(dp(i - 1), dp(i - 2) + nums[i])
                    memo[i] = p
                    return p

        return dp(len(nums) - 1)