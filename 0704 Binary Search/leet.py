class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = bisect.bisect_left(nums, target)
        if i < len(nums) and nums[i] == target:
            return i
        else:
            return -1
