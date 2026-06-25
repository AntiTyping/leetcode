class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        l, r = 0, len(letters)
        while l < r:
            m = l + (r - l) // 2

            if letters[m] > target:
                r = m
            else:
                l = m + 1

        return letters[l % len(letters)]