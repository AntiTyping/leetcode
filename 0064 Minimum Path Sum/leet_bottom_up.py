class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                if r + c == 0:
                    dp[r][c] = grid[0][0]
                else:
                    ans = float('inf')
                    if r > 0:
                        ans = min(ans, grid[r][c] + dp[r - 1][c])
                    if c > 0:
                        ans = min(ans, grid[r][c] + dp[r][c - 1])
                    dp[r][c] = ans

        return dp[rows - 1][cols - 1]

