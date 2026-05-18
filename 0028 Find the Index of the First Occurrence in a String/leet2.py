class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        left = 0
        right = 0

        while left < len(haystack):
            if right >= len(haystack):
                return -1
            if haystack[right] == needle[right - left]:
                right += 1
                if right - left == len(needle):
                    return left
            else:
                left += 1
                right = left
        return -1

