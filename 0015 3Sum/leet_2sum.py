class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            h = {}
            for j in range(i+1, len(nums)):
                diff =  - nums[i] - nums[j]
                if diff in h:
                    k = h[diff]
                    l = [nums[i], nums[j], nums[k]]
                    ans.append(tuple(sorted(l)))
                else:
                    h[nums[j]] = j
        return list(set(ans))
