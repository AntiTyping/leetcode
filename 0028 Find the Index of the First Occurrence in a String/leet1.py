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

        # 111222
        # .   222
        while left <= len(haystack) - len(needle):
            right = 0
            while right < len(needle):
                if haystack[left + right] == needle[right]:
                    right += 1
                else:
                    break
            if right == len(needle):
                return left
            left += 1
        return -1