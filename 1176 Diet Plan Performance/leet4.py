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
        T = sum(calories[:k])

        if T > upper:
            points += 1
        if T < lower:
            points -= 1

        for r in range(k, len(calories)):
            T = T - calories[r - k] + calories[r]
            if T > upper:
                points += 1
            if T < lower:
                points -= 1

        return points

