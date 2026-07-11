# n^2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return True
        return False

print(Solution().containsDuplicate([1, 2, 3, 1]))


# Time Limit Exceeded
# 65 / 77 testcases passed

# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109