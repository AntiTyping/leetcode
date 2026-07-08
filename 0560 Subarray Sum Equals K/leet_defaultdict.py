class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = defaultdict(int)
        h[0] = 1
        curr = 0
        ans = 0
        for r in range(len(nums)):
            curr += nums[r]
            if curr - k in h:
                ans += h[curr - k]
            h[curr] += 1
        return ans

