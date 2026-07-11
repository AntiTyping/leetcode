class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def edit(str):
            stack = []
            for c in str:
                if c == "#":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)

        return edit(s) == edit(t)