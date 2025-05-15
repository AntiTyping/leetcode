class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        @cache
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 0

            return min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2))

        return dp(len(cost))