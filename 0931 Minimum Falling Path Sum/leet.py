from functools import cache
class Solution:
    def minFallingPathSum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        @cache
        def dp(r, c):
            if r > rows - 1:
                return 0
            if c < 0 or c > cols - 1:
                return 0

            left = float('inf')
            right = float('inf')
            if c > 0:
                left = dp(r + 1, c - 1)
            if c < cols - 1:
                right = dp(r + 1, c + 1)
            down = dp(r + 1, c)

            return matrix[r][c] + min(left, down, right)

        m = float('inf')
        for c in range(cols):
            m = min(m, dp(0, c))

        return m

print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))