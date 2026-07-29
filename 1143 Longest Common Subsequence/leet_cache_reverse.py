class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        cache = {}

        def dp(i, j):
            if i >= 0 and j >= 0:
                if text1[i] == text2[j]:
                    if (i-1, j-1) not in cache:
                        cache[(i-1, j-1)] = dp(i - 1, j - 1)
                    return cache[(i-1, j-1)] + 1
                else:
                    if (i-1, j) not in cache:
                        cache[(i-1, j)] = dp(i - 1, j)
                    if (i, j-1) not in cache:
                        cache[(i, j-1)] = dp(i, j-1)
                    return max(cache[(i-1, j)], cache[(i, j-1)])
            else:
                return 0

        return dp(len(text1)-1, len(text2)-1)