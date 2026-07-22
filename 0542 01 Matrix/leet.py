class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and mat[r][c] == 1

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        queue = deque()
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 1))
                    seen.add((r,c))

        while queue: # (0, 1, 0)
            r1, c1, dist = queue.popleft() # 0, 1, 0
            for dir in dirs:
                r2, c2 = r1 + dir[0], c1 + dir[1]
                if (r2, c2) not in seen and valid(r2, c2):
                    seen.add((r2, c2))
                    queue.append((r2, c2, dist+1))
                    mat[r2][c2] = dist

        return mat