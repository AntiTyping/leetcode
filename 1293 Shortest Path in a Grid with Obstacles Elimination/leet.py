class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        queue = deque([(0, 0, 0, 0)])
        seen = {(0, 0, 0)}

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            r, c, distance, obstacles = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return distance
            for dr, dc in dirs:
                r1, c1 = r + dr, c + dc
                if valid(r1, c1):
                    if grid[r1][c1] == 0:
                        if (r1, c1, obstacles) not in seen:
                            seen.add((r1, c1, obstacles))
                            queue.append((r1, c1, distance + 1, obstacles))
                    elif obstacles < k and (r1, c1, obstacles + 1) not in seen:
                        seen.add((r1, c1, obstacles + 1))
                        queue.append((r1, c1, distance + 1, obstacles + 1))

        return -1