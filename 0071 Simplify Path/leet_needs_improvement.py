class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for c in path:
            # .
            if len(stack) > 0 and c == "/":
                # /. /
                if len(stack) > 1 and stack[-1] == "." and stack[-2] == "/":
                    stack.pop()
                # /.. /
                elif len(stack) > 2 and stack[-1] == "." and stack[-2] == "." and stack[-3] == "/":
                    stack.pop()
                    stack.pop()
                    if len(stack) > 1:
                        stack.pop()
                    while len(stack) > 1 and stack[-1] != "/":
                        stack.pop()
                # / /
                elif stack[-1] == "/":
                    pass
                else:
                    stack.append(c)
            # ..
            else:
                stack.append(c)

        if len(stack) > 2 and stack[-1] == "." and stack[-2] == "." and stack[-3] == "/":
            stack.pop()
            stack.pop()
            if len(stack) > 1:
                stack.pop()
            while len(stack) > 1 and stack[-1] != "/":
                stack.pop()
        if len(stack) > 1 and stack[-1] == "." and stack[-2] == "/":
            stack.pop()
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        ans = "".join(stack)

        return ans
