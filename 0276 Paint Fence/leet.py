from functools import cache
class Solution:
    def numWays(self, n: int, k: int) -> int:

        @cache
        def dp(i):
            if i == 1:
                return k
            if i == 2:
                return k * k

            ways = (k - 1) * (dp(i - 1) + dp(i - 2))

            return ways

        return dp(n)

print(Solution().numWays(7, 2))