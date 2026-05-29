class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        def cnt(name):
            a = []
            prev = name[0]
            count = 1
            for i in range(1, len(name)):
                if name[i] == prev:
                    count += 1
                else:
                    a.append([prev, count])
                    prev = name[i]
                    count = 1
            a.append([prev, count])
            return a

        a = cnt(name)
        b = cnt(typed)
        if len(a) != len(b):
            return False

        for i in range(len(a)):
            if a[i][0] != b[i][0] or a[i][1] > b[i][1]:
                return False
        return True