class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        p = { ')': '(', '}': '{', ']': '['  }

        for c in s:
            if not c in p.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != p[c]:
                    return False
                stack.pop()

        return len(stack) == 0