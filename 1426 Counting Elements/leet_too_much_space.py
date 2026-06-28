class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        seen = set(arr)

        out = []
        for i in range(len(arr)):
            if arr[i] + 1 in seen:
                out.append(arr[i])

        return len(out)