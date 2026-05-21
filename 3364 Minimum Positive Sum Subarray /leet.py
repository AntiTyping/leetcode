class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        min_ = float('inf')
        for n in range(l, r + 1):
            for i in range(0, len(nums) - n + 1):
                s = sum(nums[i:i + n])
                if s > 0 and s < min_:
                    min_ = s
        if min_ < float('inf'):
            return min_
        else:
            return -1


