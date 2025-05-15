class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                d = [[0, 1], [-1, 0], [0, -1], [1, 0]]
                for dr, dc in d:
                    r, c = row + dr, col + dc
                    if r > -1 and r < len(grid) and c > -1 and c < len(grid[0]) and grid[r][c] == "1":
                        q.append((r, c))
                        grid[r][c] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
