class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        n = len(needle)

        for left in range(len(haystack) - len(needle) + 1):
            if haystack[left:left + n] == needle:
                return left
        return -1