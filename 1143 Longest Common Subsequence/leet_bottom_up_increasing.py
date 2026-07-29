class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for a in range(n):
            for b in range(m):
                i = a + 1
                j = b + 1
                if text1[a] == text2[b]:
                    dp[j][i] = 1 + dp[j - 1][i - 1]
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

        return dp[m][n]
