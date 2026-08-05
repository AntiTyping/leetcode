class Solution:
    def totalNQueens(self, n: int) -> int:

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n

        def good(baord, r, c):
            for r1 in range(r):
                c1 = c - (r - r1)
                if valid(r1, c1) and board[r1] & 1 << c1:
                    return False
                c1 = c + (r - r1)
                if valid(r1, c1) and board[r1] & 1 << c1:
                    return False
                if board[r1] & 1 << c:
                    return False
            return True

        board = [0] * n

        ans = 0
        # out = []

        def bt(r):
            nonlocal ans
            if r == n:
                ans += 1
                # out = [row[:] for row in board]
                return
            for c1 in range(n):
                if good(board, r, c1):
                    board[r] ^= 1 << c1
                    bt(r + 1)
                    board[r] ^= 1 << c1

        bt(0)

        return ans