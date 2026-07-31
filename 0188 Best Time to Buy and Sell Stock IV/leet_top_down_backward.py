class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # returns maximum profit
        # state: i, holding, remaining
        @cache
        def dp(i, holding, remaining):
            if i == -1 or remaining == 0:
                return 0 if not holding else float('-inf')

            if holding:
                return max(dp(i - 1, holding, remaining), -prices[i] + dp(i - 1, False, remaining - 1))
            else:
                return max(dp(i - 1, holding, remaining), +prices[i] + dp(i - 1, True, remaining))

        return dp(len(prices) - 1, False, k)