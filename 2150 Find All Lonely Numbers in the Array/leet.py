class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = Counter(nums)

        out = []
        for n in nums:
            if n - 1 not in seen and n + 1 not in seen and seen[n] == 1:
                out.append(n)
        return out
