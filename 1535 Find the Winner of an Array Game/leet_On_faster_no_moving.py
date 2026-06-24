class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        win = 0
        a = 0
        b = 1
        # O(n)
        while win < len(arr) and win < k:
            if arr[a] > arr[b]:
                win += 1
                b = min(b+1, len(arr)-1)
            else:
                win = 1
                a = b
                b = min(b+1, len(arr)-1)
                if a == len(arr)-1:
                    b = 0

        return arr[a]