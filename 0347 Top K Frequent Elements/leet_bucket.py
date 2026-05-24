class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # build counts
        # n
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)

        # buckets
        # n
        freq = [[] for x in range(len(nums) + 1)]
        for n, c in d.items():
            freq[c].append(n)

        # select top k
        # k
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

        return ans
        # n + n log n + k