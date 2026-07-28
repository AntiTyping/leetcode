class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def valid(s):
            stack = []
            for p in s:
                if p == ")":
                    if len(stack) == 0 or stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                if p == "(":
                    stack.append("(")
            return len(stack) == 0

        def dp(s):
            if len(s) == 2 * n:
                if valid(s):
                    ans.append(s)
                return
            dp(s + "(")
            dp(s + ")")

        dp("")

        return ans