class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        s = word
        count = 0
        while s in sequence:
            count += 1
            s += word
        return count
