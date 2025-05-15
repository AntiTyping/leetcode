class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        one = 0
        two = 1

        for i in range(2, n + 1):
            fib = one + two
            one, two = two, fib

        return fib

print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(10))

