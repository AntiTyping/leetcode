class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if len(stack) < 1:
                    return False
                if s[i] == ")":
                    if stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                if s[i] == "}":
                    if stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
                if s[i] == "]":
                    if stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0