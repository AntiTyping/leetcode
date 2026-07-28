class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        def div(divisor):
            sum = 0
            for num in nums:
                sum += ceil(float(num) / divisor)  #
            return sum

        for divisor in range(1, max(nums) + 1):
            if div(divisor) <= threshold:
                return divisor

        return 0