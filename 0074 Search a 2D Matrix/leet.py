class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        first = [x[-1] for x in matrix]

        row = bisect_left(first, target)

        if row == len(matrix):
            return False

        m = bisect_left(matrix[row], target)

        return matrix[row][m] == target
