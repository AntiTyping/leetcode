class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = s[::-1]

        rows = cols = len(s) + 1

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in reversed(range(rows - 1)):
            for c in reversed(range(cols - 1)):
                if s[r] == q[c]:
                    dp[r][c] = max(dp[r][c], dp[r + 1][c + 1] + 1)
                else:
                    dp[r][c] = max(dp[r][c + 1], dp[r + 1][c])

        return dp[0][0]
