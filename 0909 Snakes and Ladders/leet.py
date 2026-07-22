class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        rows = len(board)
        cols = len(board[0])

        def boust_to_cart(a):
            y = (a - 1) // cols

            r = rows - 1 - (a - 1) // cols

            reminder = (a - 1) % cols
            if y % 2 == 0:
                c = reminder
            else:
                c = cols - reminder - 1
            return (r, c)

        def valid(a):
            return 1 <= a and a <= rows * cols

        dirs = [1, 2, 3, 4, 5, 6]

        queue = deque()
        queue.append(1)
        dist = {1: 0}

        while queue:
            p = queue.popleft()

            if p == rows * cols:
                return dist[p]

            for dir in dirs:
                p1 = p + dir
                if valid(p1):
                    r, c = boust_to_cart(p1)
                    if board[r][c] == -1:
                        if valid(p1) and p1 not in dist:
                            dist[p1] = dist[p] + 1
                            queue.append(p1)
                    else:
                        p1 = board[r][c]
                        if valid(p1) and p1 not in dist:
                            dist[p1] = dist[p] + 1
                            queue.append(p1)

        return -1
# [
# [-1,-1,-1],
# [-1, 9, 8],
# [-1, 8, 9]

#  7, 8, 9
#  6, 5, 4
#  1, 2, 3

# .4, 3
# 1, 2