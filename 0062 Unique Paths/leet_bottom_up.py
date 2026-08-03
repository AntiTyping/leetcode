class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # rerurns number of unique paths
        # state: r, c
        rows = m
        cols = n
        dp = [[0] * n for _ in range(m)]

        for c in range(cols):
            for r in range(rows):
                if c == 0 and r == 0:
                    dp[r][c] = 1
                else:
                    if r > 0:
                        dp[r][c] +=  dp[r-1][c]
                    if c > 0:
                        dp[r][c] +=  dp[r][c-1]

        return dp[rows-1][cols-1]