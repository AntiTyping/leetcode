class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        def cost(i):
            if i == 0:
                return 0
            return costs[i-1]

        def jump(i, j):
            return cost(j)+(j-i)**2

        @cache
        def dp(i):
            if i == 0:
                return 0
            a = b = c = float("inf")

            if i > 0:
                a = dp(i-1) + jump(i-1, i)
            if i > 1:
                b = dp(i-2) + jump(i-2, i)
            if i > 2:
                c = dp(i-3) + jump(i-3, i)

            return min(a, b, c)

        return dp(n)