class Solution:
    def wordBreak(self, s, wordDict):

        memo = {}

        def dp(i):
            if i >= len(s):
                return True

            for word in wordDict:
                if (word, i) not in memo:
                    if s[i:(i + len(word))] == word:
                        r = dp(i + len(word))
                        memo[(word, i)] = r
                if (word, i) in memo and memo[(word, i)] == True:
                    return True

            return False

        return dp(0)