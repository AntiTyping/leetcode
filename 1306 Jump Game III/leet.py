class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        def valid(i):
            return 0 <= i and i < len(arr)

        queue = deque()
        seen = set()

        queue.append(start)
        seen.add(start)

        while queue: # 5; 4, 6; 6, 1; 1; 3; 0;
            i = queue.popleft() # 5; 4; 6; 1; 3; 0

            if arr[i] == 0: # False; False; False; F; F
                return True
            neighbours = [i - arr[i], i + arr[i]] # 4, 6; 1, 7; 4, 8; -1, 3; 0, 6;
            for n in neighbours:
                if valid(n) and n not in seen: # True and True;
                    seen.add(n) # 5; 4, 6; 1; 3; 0
                    queue.append(n) # 4, 6; 6, 1; 3; 0

        return False