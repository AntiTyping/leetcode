# 27 ms Beats 85.89%
# 15.74 MB Beats 11.85%
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cols = []
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            cols.append(col)

        h = defaultdict(int)
        for row in grid:
            h[tuple(row)] += 1

        ans = 0

        for col in cols:
            if tuple(col) in h:
                ans += h[tuple(col)]

        return ans
