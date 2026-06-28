class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        n = len(arr)

        out = 0
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] == arr[i]:
                j += 1
            if j < n and arr[j] == arr[i] + 1:
                out += j - i
            i = j

        return out
