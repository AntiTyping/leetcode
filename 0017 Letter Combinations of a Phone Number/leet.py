class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        h = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        out = []

        def backtrack(curr, i):
            if len(curr) == len(digits):
                out.append("".join(curr[:]))
                return
            for l in list(h[digits[i]]):
                curr.append(l)
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)

        return out