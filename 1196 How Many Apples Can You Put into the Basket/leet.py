class Solution(object):
    def maxNumberOfApples(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        weight.sort()

        curr = 0
        n = 0
        l = 0
        while l < len(weight):
            if curr >= 5000:
                return n
            if curr + weight[l] <= 5000:
                curr += weight[l]
                l += 1
                n += 1
            else:
                return n

        return n

