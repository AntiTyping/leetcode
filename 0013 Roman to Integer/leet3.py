class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}.__getitem__
        total = prev = 0
        for c in reversed(s):
            v = m(c)
            if v < prev:
                total -= v
            else:
                total += v
                prev = v
        return total