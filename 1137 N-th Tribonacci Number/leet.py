class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # func: sum
        # state: current tribonacci
        # dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
        # dp[0] = 0
        # dp[1] = 1

        memo = {}

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1

            if i not in memo:
                memo[i] = dp(i-3)+dp(i-2)+dp(i-1)

            return memo[i]

        return dp(n)