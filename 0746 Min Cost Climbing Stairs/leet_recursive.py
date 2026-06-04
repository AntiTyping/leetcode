class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(n):
            if n == 0:
                return cost[n]
            elif n == 1:
                return cost[n]
            elif n < len(cost):
                return min(dp(n - 1), dp(n - 2)) + cost[n]
            else:
                return min(dp(n - 1), dp(n - 2))

        return dp(len(cost) + 1)
