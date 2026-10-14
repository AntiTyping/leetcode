class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dp(n: int) -> int:
            if n <= 1:
                return 1
            ans = 0
            for i in range(0, n):
                ans += dp(i) * dp(n - i - 1)
            return ans

        return dp(n)
