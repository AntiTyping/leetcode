class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        c = Counter(text)

        ans = float('inf')
        for l in list("balloon"):
            if c[l] == 0:
                return 0

        for l in "balloon":
            ans = min(ans, c[l])

        ans = min(ans, c["l"] // 2, c["o"] // 2)

        return ans