class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {0: 1}
        sum = 0
        n = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum - k in sums:
                n += sums[sum - k]

            if sum in sums:
                sums[sum] += 1
            else:
                sums[sum] = 1
        return n

# Solution().subarraySum([1,2,3], 3)
print(Solution().subarraySum([1, -1, 0], 0))
