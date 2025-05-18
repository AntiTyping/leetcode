class Solution:
    def minCost(self, costs):
        # min
        # ith house
        # min cost to paint ith house
        dp = [0,  0, 0]

        for r in range(len(costs)):
            print(r)
            dp0 = costs[r][0] + min(dp[1], dp[2])
            dp1 = costs[r][1] + min(dp[0], dp[2])
            dp2 = costs[r][2] + min(dp[0], dp[1])

            dp = [dp0, dp1, dp2]

        return min(dp)

print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))