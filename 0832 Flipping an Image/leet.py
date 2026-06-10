class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        # O(n)
        for r in range(len(image)):
            row = image[r]
            l, r = 0, len(row) - 1
            # O(n)
            while l <= r:
                row[l], row[r] = row[r] ^ 1, row[l] ^ 1
                l += 1
                r -= 1

        return image

