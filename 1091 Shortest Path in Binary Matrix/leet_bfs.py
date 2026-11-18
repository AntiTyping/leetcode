class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

        if grid[0][0] == 1:
            return - 1

        n = len(grid)

        q = deque([(0, 0, 1)])
        visited = {(0, 0)}

        def isOpen(r, c):
            return grid[r][c] == 0

        def neighbours(r, c):
            ns = []
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    ns.append((nr, nc))
            return ns

        while q:
            curr = q.popleft()
            r, c, l = curr
            if r == n - 1 and c == n - 1:
                return l
            for nr, nc in neighbours(r, c):
                if isOpen(nr, nc) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, l + 1))

        return -1