class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # i, holding, remaining

        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(len(prices) + 1)]

        for i in range(len(prices) -1, -1, -1):
            for holding in range(2):
                for remaining in range(1, k + 1):
                    action = dp[i+1][holding][remaining]
                    if holding:
                        action = max(action, +prices[i] + dp[i+1][0][remaining-1])
                    else:
                        action = max(action, -prices[i] + dp[i+1][1][remaining])
                    dp[i][holding][remaining] = action

        return dp[0][0][k]