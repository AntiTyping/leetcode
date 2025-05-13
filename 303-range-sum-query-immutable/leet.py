
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        p = [0] * len(nums)
        p[0] = nums[0]
        for i in range(1, len(nums)):
            p[i] = p[i - 1] + nums[i]
        self.p = p

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.p[right]
        else:
            return self.p[right] - self.p[left - 1]
