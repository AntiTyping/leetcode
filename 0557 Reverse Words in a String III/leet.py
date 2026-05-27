class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        out = []

        for w in words:
            out.append("".join(reversed(w)))

        return " ".join(out)
