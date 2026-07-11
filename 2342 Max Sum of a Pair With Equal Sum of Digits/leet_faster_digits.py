# 419 ms Beats 72.22%
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def sum_digits(n):
            ans = n % 10
            while n > 0:
                n = n // 10
                ans += n % 10
            return ans

        digit_sum = defaultdict(list)

        for i in range(len(nums)):
            digit_sum[sum_digits(nums[i])].append(nums[i])

        ans = -1

        for k in digit_sum:
            m = digit_sum[k]
            if len(m) < 2:
                continue
            elif len(m) == 2:
                ans = max(ans, sum(m))
            else:
                m.sort()
                ans = max(ans, sum(m[-2:]))
        return ans
