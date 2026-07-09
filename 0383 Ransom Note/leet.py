class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cr = Counter(ransomNote)
        cm = Counter(magazine)

        for l in cr.keys():
            if cm[l] < cr[l]:
                return False

        return True