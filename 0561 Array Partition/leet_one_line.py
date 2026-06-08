class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: in
        """
        return sum(sorted(nums)[::2])
