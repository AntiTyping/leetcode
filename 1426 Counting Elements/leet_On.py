class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # On(n)
        seen = set(arr)

        out = 0
        # O(n)
        for i in range(len(arr)):
            if arr[i] + 1 in seen:
                out += 1

        return out