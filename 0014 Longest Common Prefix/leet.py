class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        i = 0
        while True:
            for s in strs:
                if i == len(s):
                    return prefix
                a = strs[0][i]
                if s[i] != a:
                    return prefix
            prefix += a
            i += 1