class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        v = set()
        q = deque()

        rows, cols = len(rooms), len(rooms[0])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    v.add((r, c))

        d = 0

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                rooms[row][col] = d

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r > -1 and r < rows and c > -1 and c < cols and rooms[r][c] != -1 and (r, c) not in v:
                        q.append((r, c))
                        v.add((r, c))

            d += 1
