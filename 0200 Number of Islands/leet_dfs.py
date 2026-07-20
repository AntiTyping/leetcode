class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def neighbors(r, c):
            n = []
            if c > 0 and c < len(grid[0]):
                n.append([r, c-1])
            if r > 0 and r < len(grid):
                n.append([r-1, c])
            if c < len(grid[0])-1:
                n.append([r, c+1])
            if r < len(grid)-1:
                n.append([r+1, c])
            return n

        def dfs(r, c):
            grid[r][c] = "0" # 0
            for n in neighbors(r, c):
                if grid[n[0]][n[1]] == "1":
                    dfs(n[0], n[1])

        ans = 0
        for r in range(len(grid)): # 0
            for c in range(len(grid[0])): # 0
                if grid[r][c] == "1": # 1
                    ans += 1 # 1
                    dfs(r, c) # 0, 0

        return ans