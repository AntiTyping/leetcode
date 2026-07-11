# 427 ms Beats 70.37%
# 21.70 MB Beats 100.00%
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

        digit_sum = defaultdict(int)

        ans = -1

        for num in nums:
            d = sum_digits(num)
            if d in digit_sum:
                ans = max(ans, num + digit_sum[d])
            digit_sum[d] = max(num, digit_sum[d])

        return ans
