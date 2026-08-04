class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # returns min sum for coordinates
        @cache
        def dp(r, c):
            if r + c == 0:
                return grid[0][0]
            ans = float('inf')
            if r > 0:
                ans = min(ans, dp(r - 1, c) + grid[r][c])
            if c > 0:
                ans = min(ans, dp(r, c - 1) + grid[r][c])
            return ans

        return dp(rows - 1, cols - 1)
