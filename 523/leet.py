class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        reminders = {0: -1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            r = sum % k
            if r not in reminders:
                reminders[r] = i
            else:
                if i - reminders[r] > 1:
                    return True
        return False

print(Solution().checkSubarraySum([23,2,4,6,7], 6))
