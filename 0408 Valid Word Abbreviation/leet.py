class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        l, r = 0, 0

        while l < len(word) and r < len(abbr):
            if word[l] == abbr[r]:
                l += 1
                r += 1
            else:
                if abbr[r].isdigit():
                    if abbr[r] == "0":
                        return False
                    d = ""
                    while r < len(abbr) and abbr[r].isdigit():
                        d = d + abbr[r]
                        r += 1
                    l += int(d)
                else:
                    return False
        return l == len(word) and r == len(abbr)