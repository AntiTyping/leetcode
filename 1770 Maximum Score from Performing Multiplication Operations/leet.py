class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n, m = len(nums), len(multipliers)

        memo = {}

        def dp(i, left):
            if i == m:
                return 0

            if (i, left) not in memo:
                mult = multipliers[i]
                right = n - 1 - (i - left)

                memo[(i, left)] = max(mult * nums[left] + dp(i + 1, left + 1), mult * nums[right] + dp(i + 1, left))

            return memo[(i, left)]

        return dp(0, 0)