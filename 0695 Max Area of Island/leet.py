class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.curr = len(grid)

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1


        def dfs(r, c):
            grid[r][c] = 0
            self.curr += 1
            for dr, dc in directions:
                if valid(r + dr, c + dc):
                    dfs(r + dr, c + dc)

        ans = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.curr = 0
                    dfs(r, c)
                    ans = max(ans, self.curr)

        return ans
