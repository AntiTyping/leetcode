class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s:
            return 0

        num = ""
        i = 0
        if s[0] in "-+":
            if s[0] == "-":
                num += "-"
            i += 1
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        if len(num) == 0:
            return 0
        if len(num) == 1 and num[0] == "-":
            return 0

        return min(max(-2 ** 31, int(num)), 2 ** 31 - 1)




