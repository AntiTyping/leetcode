class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = 0
        ones = 0
        diffs = {}

        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1

            if ones - zeros not in diffs:
                diffs[ones - zeros] = i

            if zeros == ones:
                ans = max(ans, zeros + ones)
            else:
                ans = max(ans, i - diffs[ones - zeros])
        return ans

# seek the longies
# length must be n*2
# we care about the diff
# lookup prefix that fixes the subarray
# subarrays are continous