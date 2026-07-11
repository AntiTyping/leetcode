class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int

        """
        # O(n)
        c = Counter(arr)
        # O(n log n)
        a = c.most_common()[::-1]

        # O(n)
        for x in a:
            if x[1] < k:
                del c[x[0]]
                k -= x[1]
            else:
                c[x[0]] -= k
                k = 0
            if k == 0:
                break
        # O(n)
        ans = 0
        for i in c.items():
            if i[1] > 0:
                ans += 1
        # return len(set([x[0] for x in c.items() if x[1] > 0]))
        return ans
