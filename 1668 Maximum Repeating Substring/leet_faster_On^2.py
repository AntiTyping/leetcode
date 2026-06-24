class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        max_k = 0
        # O(n)
        i = 0
        while i < len(sequence):
            if sequence[i:i+len(word)] == word:
                n = 1
                max_k = max(max_k, n)
                l = i + len(word)
                i += len(word)
                # O(n)
                while sequence[l:l+len(word)] == word:
                    n += 1
                    max_k = max(max_k, n)
                    i = l
                    l += len(word)
                i += 1
            else:
                i += 1
        return max_k
