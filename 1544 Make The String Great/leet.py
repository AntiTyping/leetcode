class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c.isupper() and len(stack) > 0 and stack[-1].islower() and c.lower() == stack[-1].lower():
                stack.pop()
            elif c.islower() and len(stack) > 0 and stack[-1].isupper() and c.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)