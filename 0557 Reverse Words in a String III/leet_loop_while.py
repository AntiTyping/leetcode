class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        out = []
        for w in words:
            ww = list(w)
            l, r = 0, len(w) - 1
            while l < r:
                ww[l], ww[r] = ww[r], ww[l]
                l += 1
                r -= 1
            out.append("".join(ww))
        return " ".join(out)
