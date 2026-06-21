class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            found = True
            for j in range(len(goal)):
                if s[(i + j) % len(s)] != goal[j]:
                    found = False
                    break
            if found:
                return True
        return False