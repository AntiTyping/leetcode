class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        dirs = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n and grid[r][c] == 0

        queue = deque()
        queue.append([0, 0, 1])

        if not valid(0, 0):
            return -1

        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for d in dirs:
                if valid(r + d[0], c + d[1]):
                    grid[r + d[0]][ c + d[1]] = 1
                    queue.append([r + d[0], c + d[1], dist + 1])

        return -1
