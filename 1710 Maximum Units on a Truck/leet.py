class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxes = [[b[1], b[0]] for b in boxTypes]
        boxes.sort(reverse=True)
        l = 0
        n = 0
        units = 0
        while l < len(boxes):
            if boxes[l][1] == 0:
                l += 1
            elif n < truckSize:
                n += 1
                units += boxes[l][0]
                boxes[l][1] -= 1
            else:
                return units

        return units
