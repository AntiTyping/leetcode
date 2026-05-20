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
        T = 0
        l, r = 0, k - 1

        for i in range(0, k):
            T += calories[i]
        if T > upper:
            points += 1
        if T < lower:
            points -= 1

        r += 1
        while r < len(calories):
            T -= calories[l]
            l += 1
            T += calories[r]

            if T > upper:
                points += 1
            if T < lower:
                points -= 1
            r += 1

        return points

