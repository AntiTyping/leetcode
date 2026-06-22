class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [nums[0] ** 2]
        ans = [0] * len(nums)

        if True:
            l, r = 0, 0
            for i in range(len(nums)):
                if nums[i] < 0:
                    l = i
            r = l + 1
            i = 0
            while l >= 0 and r < len(nums):
                if nums[l] ** 2 < nums[r] ** 2:
                    ans[i] = nums[l] ** 2
                    l -= 1
                else:
                    ans[i] = nums[r] ** 2
                    r += 1
                i += 1
            while l >= 0:
                ans[i] = nums[l] ** 2
                l -= 1
                i += 1
            while r < len(nums):
                ans[i] = nums[r] ** 2
                r += 1
                i += 1

        return ans

