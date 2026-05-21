class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if set(s) != set(t):
            return False
        a, b = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            a[s[i]] += 1
        for j in range(len(t)):
            b[t[j]] += 1

        return a.items() == b.items()