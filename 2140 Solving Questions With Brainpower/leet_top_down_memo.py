class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        # state i
        #

        memo = {}

        def dp(i):
            if i >= len(questions):
                return 0

            j = i + questions[i][1] + 1
            if i not in memo:
                memo[i] = max(questions[i][0] + dp(j), dp(i + 1))
            return memo[i]

        return dp(0)
