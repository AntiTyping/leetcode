class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        curr = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                curr += 1
            while curr > k:
                if nums[l] % 2 == 1:
                    curr -= 1
                l += 1
            if curr == k:
                ans += 1
        return ans
