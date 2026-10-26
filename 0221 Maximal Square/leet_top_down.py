class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        @cache
        def dp(r, c):
            if r == 0 or c == 0:
                return int(matrix[r][c])
            if matrix[r][c] == "1":
                return 1 + min(dp(r, c - 1), dp(r - 1, c - 1), dp(r - 1, c))
            else:
                return 0

        best = max([dp(r, c) for r in range(rows) for c in range(cols)])
        return best * best
