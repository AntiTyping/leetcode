class Solution(object):
    def maximizeSweetness(self, sweetness, k):
        """
        :type sweetness: List[int]
        :type k: int
        :rtype: int
        """
        def div(limit):
            chunks = 0
            sum = 0
            for s in sweetness:
                sum += s
                if sum > limit:
                    chunks += 1
                    sum = 0
            return chunks

        l, r = 1, sum(sweetness) // (k + 1)
        while l <= r:
            m = (r + l) // 2
            if div(m) >= k + 1:
                l = m + 1
            else:
                r = m - 1

        return l
