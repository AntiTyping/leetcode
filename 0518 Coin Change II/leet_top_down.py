class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # func: number of ways to make the amount for state
        # state: amount
        # order: backward
        # reccurence:
        #   dp(amount) = 
        #    dp(amount - c) for c in coins if c < amount
        # base: 
        # a == 0 return 1
        # a < 0 return 0
        # coins = sorted(coins)

        # @cache
        # def dp(a, coin):
        #     if a == 0:
        #         return 1
        #     ans = 0
        #     for c in coins:
        #         if c > coin:
        #             break
        #         if c <= a:
        #             ans = ans + dp(a - c, c)
        #         else:
        #             break
        #     return ans

        # return dp(amount, coins[-1])
        # too slow^

        # faster way

        @cache
        def dp(a, i):
            if a == 0:
                return 1
            if a < 0 or i < 0:
                return 0
            return dp(a, i - 1) + dp(a - coins[i], i)
        return dp(amount, len(coins) - 1)