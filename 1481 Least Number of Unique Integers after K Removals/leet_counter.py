class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int

        """
        c = Counter(arr)

        mc = [list(m) for m in c.most_common()]
        i = -1
        for j in range(k):
            m = mc[i]
            if m[1] == 1:
                del c[m[0]]
                i -= 1
            else:
                m[1] -= 1
                c[m[0]] -= 1

        return len(c)