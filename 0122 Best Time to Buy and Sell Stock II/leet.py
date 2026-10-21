class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def dp(i, holding):
            if i == len(prices):
                return 0
            if holding:
                # sell
                sell = prices[i] + dp(i + 1, False)
                # hold
                hold = dp(i + 1, holding)
                return max(sell, hold)
            else:
                # buy
                buy = -prices[i] + dp(i + 1, True)
                # skip
                skip = dp(i + 1, holding)
                return max(buy, skip)

        return dp(0, False)