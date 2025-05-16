class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count
        # index into string i
        # count of ways to decode string up to i
        # dp(i) = 1 + dp(i-1)
        # dp(i) = 1 + dp(i-2) last 2 chars <= 26

        memo = {}

        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            if i == len(s) - 1:
                return 1

            if i in memo:
                return memo[i]

            ans = dp(i + 1)
            if int(s[i:i + 2]) <= 26:
                ans += dp(i + 2)

            memo[i] = ans
            return ans

        return dp(0)



