class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = Counter(arr)

        n = len(arr)

        i = 0
        mc = c.most_common()
        ans = 0
        while n > len(arr) // 2:
            n -= mc[i][1]
            i += 1
            ans += 1

        return ans
