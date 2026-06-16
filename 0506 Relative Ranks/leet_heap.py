class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]

        s = [-x for x in score]
        heapq.heapify(s)

        rank = {}
        for i in range(len(s)):
            hh = heapq.heappop(s)
            rank[-hh] = i
        ans = []
        for i in range(len(score)):
            r = rank[score[i]]
            if r < 3:
                ans.append(medals[r])
            else:
                ans.append(str(r+1))
        return ans
