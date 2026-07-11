class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = [0] * 26

        for l in sentence:
            letters[ord(l) - ord('a')] += 1

        for l in letters:
            if l == 0:
                return False

        return True
