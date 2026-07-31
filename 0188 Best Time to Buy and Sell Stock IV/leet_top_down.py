class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # returns maximum profit
        # state
        # recurrence

        # returns max profit
        @cache
        def dp(i, intrade, remining):
            if i == len(prices):
                return 0
            if remining == 0:
                return 0

            if intrade:
                sell = prices[i] + dp(i + 1, False, remining - 1)
                hold = dp(i + 1, True, remining)

                return max(sell, hold)
            else:
                buy = -prices[i] + dp(i + 1, True, remining)
                skip = dp(i + 1, False, remining)

                return max(buy, skip)

        return dp(0, False, k)