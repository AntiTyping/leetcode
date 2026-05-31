class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()

        for n in nums:
            s.add(n)

        left = []
        right = []

        for n in nums:
            if (n - 1) not in s:
                left.append(n)
            if (n + 1) not in s:
                right.append(n)

        max_ = 0

        for l in left:
            n = 0
            ll = l
            while ll in s:
                n += 1
                ll += 1
            if n > max_:
                max_ = n

        return [left, right]
