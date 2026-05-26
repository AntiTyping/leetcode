class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # O(n^2)
        for row in range(9):
            s = set()
            s2 = set()
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in s:
                    return False
                s.add(num)

                num2 = board[col][row]
                if num2 == ".":
                    continue
                if num2 in s2:
                    return False
                s2.add(num2)

        # # O(n^2)
        # for col in range(9):
        #     s = set()
        #     for row in range(9):
        #         num = board[row][col]
        #         if num == ".":
        #             continue
        #         if num in s:
        #             return False
        #         s.add(num)

        # O(n^2)
        for row in range(3):
            for col in range(3):
                s = set()
                for r in range(3):
                    for c in range(3):
                        num = board[row * 3 + r][col * 3 + c]
                        if num == ".":
                            continue
                        if num in s:
                            return False
                        s.add(num)

        return True
