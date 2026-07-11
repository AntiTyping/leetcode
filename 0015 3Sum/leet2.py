class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # O(n log n)
        nums.sort()

        ans = []

        # O(n^2)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return ans