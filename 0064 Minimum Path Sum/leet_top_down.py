class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def neighbours(r, c):
            n = []
            dirs = [(-1, 0), (0, -1)]
            for dr, dc in dirs:
                r1, c1 = r + dr, c + dc
                if valid(r1, c1):
                    n.append((r1, c1))
            return n

        cache = {}

        def dp(r, c):
            if r == 0 and c == 0:
                return grid[0][0]

            sums = []

            for r1, c1 in neighbours(r, c):
                if (r1, c1) not in cache:
                    cache[(r1, c1)] = dp(r1, c1)
                sums.append(cache[(r1, c1)])

            return min(sums) + grid[r][c]

        return dp(rows - 1, cols - 1)