class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                num = int(num) - 1

                if rows[row][num] == True:
                    return False
                if cols[col][num] == True:
                    return False

                box = 3 * (row // 3) + col // 3

                if boxes[box][num] == True:
                    return False

                rows[row][num] = True
                cols[col][num] = True
                boxes[box][num] = True

        return True
