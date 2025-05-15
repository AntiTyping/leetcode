class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i, holding, cooldown
        @lru_cache
        def dp(i, holding, cooldown):
            if i == len(prices):
                return 0

            do_nothing = dp(i + 1, holding, 0)
            do_something = 0

            if holding:
                do_something = prices[i] + dp(i + 1, 0, 1)
            else:
                do_something = -prices[i] + dp(i + 1, 1, 0)

            if cooldown:
                return do_nothing
            else:
                return max(do_nothing, do_something)

        return dp(0, 0, 0)
