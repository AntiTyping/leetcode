class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rows = m
        cols = n

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

        def dp(r, c):
            if r == 0 and c == 0:
                return 1

            s = 0
            for r1, c1 in neighbours(r, c):
                s += dp(r1, c1)
            return s

        return dp(rows - 1, cols - 1)

# I forget it is ways not how many cells to reach the end