class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # O(n)
        bc = 0
        wc = 0
        for i in range(k):  # 0..10
            if blocks[i] == 'B':
                bc += 1
            else:
                wc += 1
        min_ = wc

        for i in range(1, len(blocks) - k + 1):  # 11..
            # O(1)
            if blocks[i - 1] == 'B':
                bc -= 1
            else:
                wc -= 1
            if blocks[i + k - 1] == 'B':
                bc += 1
            else:
                wc += 1

            if wc < min_:
                min_ = wc

        return min_
