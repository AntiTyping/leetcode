class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        rotten = []
        fresh1 = []
        # 100
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh1.append([r, c])
                if grid[r][c] == 2:
                    rotten.append([r, c])

        if len(fresh1) == 0:
            return 0

        days = 1
        infected = 0

        q = deque(rotten)

        def neighbours(a):
            ns = []
            r, c = a
            dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    ns.append([nr, nc])

            return ns

        def fresh(a):
            return grid[a[0]][a[1]] == 1

        def infect(a):
            grid[a[0]][a[1]] = 2

        while q:
            level = len(q)
            for i in range(level):
                a = q.popleft()
                for n in neighbours(a):
                    if fresh(n):
                        infect(n)
                        infected += 1
                        q.append(n)
                        if infected == len(fresh1):
                            return days
            days += 1

        return -1
