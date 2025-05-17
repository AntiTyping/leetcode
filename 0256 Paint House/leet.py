class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # min
        # ith house
        # min cost to paint ith house
        dp = [[0] * 3 for _ in range(len(costs))]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for r in range(1, len(costs)):
            dp[r][0] = costs[r][0] + min(dp[r - 1][1], dp[r - 1][2])
            dp[r][1] = costs[r][1] + min(dp[r - 1][0], dp[r - 1][2])
            dp[r][2] = costs[r][2] + min(dp[r - 1][0], dp[r - 1][1])

        return min(dp[-1])
