class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # rerurns number of unique paths
        # state: r, c
        rows = m
        cols = n

        @cache
        def dp(r, c):
            if r + c == 0:
                return 1
            ans = 0
            if r > 0:
                ans += dp(r-1, c)
            if c > 0:
                ans += dp(r, c-1)

            return ans

        return dp(rows-1, cols-1)