class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        ans = -1
        for m in c:
            if c[m] == 1:
                ans = max(ans, m)

        return ans
