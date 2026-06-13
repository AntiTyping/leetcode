class Solution:
    def threeSum(self, nums):
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.append(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(set(ans))