class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_penultimate = 0
        dp = 0
        for i in range(2, len(cost) + 1):
            dp_penultimate, dp = dp, min(cost[i - 1] + dp, cost[i - 2] + dp_penultimate)

        return dp