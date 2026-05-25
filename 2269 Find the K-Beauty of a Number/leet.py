class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        # n
        n = str(num)
        x = 0
        # n
        for i in range(0, len(n) - k + 1):
            a = int(n[i:i + k])
            if a != 0 and num % a == 0:
                x += 1

        return x