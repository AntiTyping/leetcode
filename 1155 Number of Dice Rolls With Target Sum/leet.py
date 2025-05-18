from functools import cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(i, sum):
            if i == n and sum == target:
                return 1
            if i == n and sum != target:
                return 0

            s = 0
            for j in range(1, k + 1):
                s += dp(i + 1, sum + j) % (10 ** 9 + 7)

            return s

        return dp(0, 0) % (10 ** 9 + 7)
