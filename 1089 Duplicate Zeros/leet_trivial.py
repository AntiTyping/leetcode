class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        o = [0] * len(arr)
        j = 0
        i = 0
        while i < len(arr) and j < len(arr):
            if arr[i] == 0:
                o[j] = 0
                if j + 1 < len(arr):
                    o[j + 1] = 0
                    j += 1
                j += 1
            else:
                o[j] = arr[i]
                j += 1
            i += 1

        for i in range(len(arr)):
            arr[i] = o[i]
        return arr
