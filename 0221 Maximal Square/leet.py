class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dp(r, c):
            if r >= rows or c >= cols:
                return 0

            if (r, c) not in memo:
                right = dp(r, c + 1)
                down = dp(r + 1, c)
                diag = dp(r + 1, c + 1)

                memo[(r, c)] = 0
                if matrix[r][c] == "1":
                    memo[(r, c)] = 1 + min(right, down, diag)

            return memo[(r, c)]

        dp(0, 0)
        return max(memo.values()) ** 2