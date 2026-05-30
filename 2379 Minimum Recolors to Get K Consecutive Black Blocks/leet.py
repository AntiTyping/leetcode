class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_ = float('inf')

        # O(n)
        for i in range(0, len(blocks) - k + 1):
            c = 0;
            # O(k)
            for j in range(k):
                if blocks[i + j] == 'W':
                    c += 1
            if c < min_:
                min_ = c

        return min_
