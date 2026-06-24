class Solution(object):
    def numberCount(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s = set()
        n = 0
        for k in range(a, b+1):
            a = str(k)
            if len(a) == len(set(a)):
                n += 1
        return n