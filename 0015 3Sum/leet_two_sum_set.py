class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # O(n log n)
        nums.sort()

        ans = set()

        # O(n^2)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            h = {}
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in h:
                    ans.add(tuple([nums[i], nums[j], diff]))
                else:
                    h[nums[j]] = j
        return list(ans)