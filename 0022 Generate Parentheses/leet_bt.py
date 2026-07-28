class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def bt(s, op, cp):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if op < n:
                bt(s + "(", op + 1, cp)
            if cp < op:
                bt(s + ")", op, cp + 1)

        bt("", 0, 0)

        return ans