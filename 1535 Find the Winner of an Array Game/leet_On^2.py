class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        win = 0
        winner = -1
        # O(k*n)
        while win < len(arr) and win < k:
            if arr[0] > arr[1]:
                win += 1
                # O(n)
                tmp = arr.pop(1)
                # O(1)
                arr.append(tmp)
            else:
                win = 1
                # O(n)
                tmp = arr.pop(0)
                # O(1)
                arr.append(tmp)

        return arr[0]