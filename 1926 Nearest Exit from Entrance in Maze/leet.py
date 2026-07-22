class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype:1 int
        """
        rows = len(maze)
        cols = len(maze[0])

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.'

        def exit_maze(r, c):
            if r == entrance[0] and c == entrance[1]:
                return False
            return r == 0 or r == rows - 1 or c == 0 or c == cols - 1

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = deque()
        seen = set()

        queue.append((entrance[0], entrance[1], 0))  # 0, 0

        while queue:
            r, c, steps = queue.popleft()  # 0, 0, 0
            seen.add((r, c))  # 0, 0
            if exit_maze(r, c):
                return steps
            for dr, dc in dirs:
                r1, c1 = r + dr, c + dc
                if valid(r1, c1) and (r1, c1) not in seen:
                    seen.add((r1, c1))
                    queue.append((r1, c1, steps + 1))

        return -1