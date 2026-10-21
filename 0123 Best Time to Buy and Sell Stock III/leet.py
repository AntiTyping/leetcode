class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def dp(i, holding, remining):
            if i == len(prices):
                return 0
            if remining == 0:
                return 0

            if holding:
                # sell
                sell = prices[i] + dp(i + 1, False, remining - 1)
                # hold
                hold = dp(i + 1, holding, remining)
                return max(sell, hold)
            else:
                # buy
                if remining > 0:
                    # buy
                    buy = -prices[i] + dp(i + 1, True, remining)
                    # skip
                    skip = dp(i + 1, holding, remining)
                    return max(buy, skip)
                else:
                    # skip
                    return dp(i + 1, holding, remining)

        return dp(0, False, 2)
