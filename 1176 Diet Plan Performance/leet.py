class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        points = 0
        l, r = 0, k - 1
        T = 0

        for i in range(0, k):
            T += calories[i]

        while r < len(calories) - 1:
            if T > upper:
                points += 1
            if T < lower:
                points -= 1
            T -= calories[l]
            l += 1
            r += 1
            T += calories[r]

        if T > upper:
            points += 1
        if T < lower:
            points -= 1

        return points

