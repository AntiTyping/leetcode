class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for r in range(rows):
            for c in range(cols):
                a = float('inf')
                b = float('inf')
                if r > 0:
                    a = dp[r - 1][c]
                if c > 0:
                    b = dp[r][c - 1]

                if not (r == 0 and c == 0):
                    dp[r][c] = grid[r][c] + min(a, b)

        return dp[-1][-1]
