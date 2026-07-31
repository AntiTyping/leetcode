class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # returns maximum profit
        # state: i, holding, remaining
        @cache
        def dp(i, holding, remaining):
            if i == len(prices):
                return 0
            if remaining == 0:
                return 0

            if holding:
                return max(dp(i + 1, holding, remaining), +prices[i] + dp(i + 1, False, remaining - 1))
            else:
                return max(dp(i + 1, holding, remaining), -prices[i] + dp(i + 1, True, remaining))

        return dp(0, False, k)