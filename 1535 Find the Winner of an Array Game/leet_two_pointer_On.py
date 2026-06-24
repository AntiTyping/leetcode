class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(arr):
            return max(arr)
        else:
            win = 0
            l = 0
            r = 1
            while win < k and win < len(arr) and r < len(arr):
                if arr[l] > arr[r]:
                    win += 1
                    r += 1
                else:
                    win = 1
                    l = r
                    r += 1
            return arr[l]
