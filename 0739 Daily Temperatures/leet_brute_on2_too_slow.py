class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = []
        # O(n^2)
        for i in range(len(temperatures)):
            t = temperatures[i]
            d = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    d = j - i
                    break
            ans.append(d)

        return ans
