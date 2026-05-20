class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        l, r = 0, 0
        h = {}

        for r in range(len(nums)):
            if abs(r - l) > k:
                del h[nums[l]]
                l += 1
            if nums[r] in h:
                return True
            h[nums[r]] = r

        return False