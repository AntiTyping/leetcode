class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        out = [""] * numRows
        direction = +1
        row = 0
        for c in s:
            out[row] += c
            if direction == 1 and row == numRows - 1:
                direction = -1
            elif direction == -1 and row == 0:
                direction = +1
            row += direction

        return "".join(out)


# 5 - 8
# 4 - 6
# 3 - 4