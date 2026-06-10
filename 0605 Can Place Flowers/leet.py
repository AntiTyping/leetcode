class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
        k = 0
        i = 0

        def available(i):
            if flowerbed[i] == 1:
                return False
            if i == 0:
                if flowerbed[i + 1] == 1:
                    return False
            elif i == len(nums) - 1:
                if flowerbed[i - 1] == 1:
                    return False
            else:
                if flowerbed[i + 1] == 1 or flowerbed[i - 1] == 1:
                    return False
            return True

        while i < len(flowerbed) and k < n:
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    k += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    k += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    k += 1
                    flowerbed[i] = 1
            i += 1

        return k == n
