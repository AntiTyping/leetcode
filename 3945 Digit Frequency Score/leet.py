class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = Counter(str(n))
        score = 0
        for d in c.items():
            score += int(d[0])*d[1]

        return score