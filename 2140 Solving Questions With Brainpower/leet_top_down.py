class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        @cache
        def dp(i):
            if i < len(questions):
                return max(questions[i][0] + dp(i + questions[i][1]+1), dp(i + 1))
            else:
                return 0

        return dp(0)
