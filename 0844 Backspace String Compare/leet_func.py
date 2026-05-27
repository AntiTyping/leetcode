class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def process(s):
            a = []
            b = 0
            for i in range(len(s)-1, -1, -1):
                if s[i] == '#':
                    b += 1
                else:
                    if b > 0:
                        b -= 1
                    else:
                        a.append(s[i])
            return a

        return process(s) == process(t)