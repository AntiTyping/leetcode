class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        min_ = nums[k-1] - nums[0]

        for i in range(len(nums)-k+1):
            if nums[i+k-1] - nums[i] < min_:
                min_ = nums[i+k-1] - nums[i]
        return min_
