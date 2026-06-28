class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        for l in s:
            if l in seen:
                return l
            else:
                seen.add(l)
