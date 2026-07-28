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

        # for divisor in range(1, max(nums)+1):
        #     if div(divisor) <= threshold:
        #         return divisor
        l, r = 1, max(nums) + 1
        while l <= r:
            divisor = (l + r) // 2
            if div(divisor) > threshold:
                l = divisor + 1
            else:
                r = divisor - 1

        return l