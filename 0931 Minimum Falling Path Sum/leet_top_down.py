class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        @cache
        def dp(r, c):
            if r == rows - 1:
                return matrix[r][c]

            ans = inf

            if c > 0:
                ans = min(ans, dp(r + 1, c - 1))
            ans = min(ans, dp(r + 1, c))

            if c < cols - 1:
                ans = min(ans, dp(r + 1, c + 1))

            return ans + matrix[r][c]

        ans = inf
        for c in range(0, cols):
            ans = min(ans, dp(0, c))

        return ans
