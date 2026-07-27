class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = Counter(arr)

        n = 0
        i = 0
        for v,c in c.most_common():
            n += c
            i += 1
            if n >= len(arr) // 2:
                return i