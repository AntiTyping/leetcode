class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        cj = Counter(jewels)
        cs = Counter(stones)

        ans = 0
        for j in cj:
            ans += cs[j]

        return ans