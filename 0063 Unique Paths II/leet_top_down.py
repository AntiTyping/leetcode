class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[-1][-1] == 1:
            return 0

        @cache
        def dp(i, j):
            if i + j == 0:
                return 1

            ans = 0
            if i > 0:
                if obstacleGrid[i - 1][j] == 0:
                    ans += dp(i - 1, j)
            if j > 0:
                if obstacleGrid[i][j - 1] == 0:
                    ans += dp(i, j - 1)

            return ans

        return dp(rows - 1, cols - 1)
