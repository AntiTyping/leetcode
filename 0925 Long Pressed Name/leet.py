class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0

        if name[0] != typed[0]:
            return False

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j] == typed[j - 1]:
                    j += 1
                else:
                    return False

        while j < len(typed):
            if typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name) and j == len(typed)