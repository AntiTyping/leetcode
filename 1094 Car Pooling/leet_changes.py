class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = []

        for trip in trips:
            n, fr, to = trip
            changes.append((fr, n))
            changes.append((to, -n))

        changes.sort()

        # return changes

        curr = 0
        for change in changes:
            curr += change[1]
            if curr > capacity:
                return False
        return True
