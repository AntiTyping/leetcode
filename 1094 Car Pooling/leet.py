class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mn = 0
        mx = 0
        for trip in trips:
            n, fr, to = trip
            mn = min(mn, fr)
            mx = max(mx, to)
        arr = [0] * (mx + 1)

        for trip in trips:
            n, fr, to = trip
            arr[fr] += n
            arr[to] -= n

        psum = [0] * (mx + 1)
        psum[0] = arr[0]
        for i in range(1, len(arr)):
            psum[i] = psum[i - 1] + arr[i]

        for i in range(len(psum)):
            if psum[i] > capacity:
                return False
        return True