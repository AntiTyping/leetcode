class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int

        """
        c = Counter(arr)

        for _ in range(k):
            mc = c.most_common()[-1]
            if mc[1] == 1:
                del c[mc[0]]
            else:
                c[mc[0]] -= 1

        return len(c)