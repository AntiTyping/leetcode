class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}

        # n
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        # we have counts
        # n log n
        s = sorted(d.items(), key= lambda item: item[1], reverse=True)

        # n
        ans = []
        for i in range(k):
            ans.append(s[i][0])
        return ans
        # n + n log n + k