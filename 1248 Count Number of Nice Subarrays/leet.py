class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f = defaultdict(int)
        f[0] = 1
        curr = 0
        ans = 0
        for r in range(len(nums)):
            curr += nums[r] % 2
            ans += f[curr - k]
            f[curr] += 1
        return ans
