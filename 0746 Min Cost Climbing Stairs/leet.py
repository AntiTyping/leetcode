class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # func: min
        # state: min cost to get to current step
        # rec: dp[i] = dp[i-1]+cost[i-1]
        # .     dp[i] = dp[i-2]+cost[i-2]
        #      dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # base:
        # dp[0] = 0
        # dp[1] = 0

        memo = {}

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 0

            if i not in memo:
                memo[i] = min(dp( i-1 )+cost[i-1], dp( i-2 )+cost[i-2])

            return memo[i]

        return dp(len(cost))



print(Solution().minCostClimbingStairs([10,15,20]))
