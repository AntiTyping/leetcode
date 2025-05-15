class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i <= 2:
                return i
            if i not in memo:
                memo[i] = dp(i-1)+dp(i-2)

            return memo[i]

        return dp(n)

print(Solution().climbStairs(10))