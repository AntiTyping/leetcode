# 31 ms Beats 80.49%
# 15.80 MB Beats 11.85%
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cols = defaultdict(int)
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            cols[tuple(col)] += 1

        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        ans = 0

        for c in cols:
            if c in rows:
                ans += rows[c] * cols[c]

        return ans
