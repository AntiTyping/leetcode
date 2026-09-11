class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # sumOdd = 0
        # sumEven = 0
        # for i in range(1, 2 * n + 1):
        #     if i % 2 == 0:
        #         sumEven += i
        #     else:
        #         sumOdd += i

        sumOdd = n**2
        sumEven = 2 * n**2 + n

        def gcd(x: int, y: int) -> int:
            while y != 0:
                x, y = y, x % y
            return x

        return gcd(sumEven, sumOdd)