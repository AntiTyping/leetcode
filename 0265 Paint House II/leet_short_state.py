class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        dp = [0] * len(costs[0])

        for r in range(len(costs)):
            new_dp = [0] * len(costs[0])
            for k in range(len(new_dp)):
                a = [dp[i] for i in range(len(dp)) if i != k]
                new_dp[k] = costs[r][k] + min(a)

            dp = new_dp

        return min(dp)
