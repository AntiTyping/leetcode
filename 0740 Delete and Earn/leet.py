class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        @cache
        def max_points(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            return max(points[num] + max_points(num - 2), max_points(num - 1))

        return max_points(max_number)

