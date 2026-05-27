class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        r = [w[::-1] for w in words]

        return " ".join(r)
