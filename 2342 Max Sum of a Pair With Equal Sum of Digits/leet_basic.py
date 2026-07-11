# 1469 ms Beats 9.26%
# 22.66 MB Beats 12.96%
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def sum_digits(n):
            digits = list(str(n))
            return sum([int(d) for d in digits])

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
