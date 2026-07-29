class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # returns maximum profit
        @lru_cache(None)
        def dp(i, holding, remaning):
            if i == len(prices):
                return 0
            if not holding:
                if remaning > 0:
                    buy = -prices[i] + dp(i + 1, True, remaning - 1)
                    skip = dp(i + 1, False, remaning)

                    return max(buy, skip)
                else:
                    return dp(i + 1, False, remaning)
            else:
                sell = prices[i] + dp(i + 1, False, remaning)
                hold = dp(i + 1, True, remaning)

                return max(sell, hold)


        return dp(0, False, k)
