class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(d, c, start):
            if d == len(days):
                return 0

            current_day = days[d]

            if current_day < start + [1, 7, 30][c]:
                return dp(d + 1, c, start)
            else:
                return min(
                    costs[2] + dp(d + 1, 2, current_day),
                    costs[1] + dp(d + 1, 1, current_day),
                    costs[0] + dp(d + 1, 0, current_day))

        return min(
            costs[0] + dp(0, 0, days[0]),
            costs[1] + dp(0, 1, days[0]),
            costs[2] + dp(0, 2, days[0])
        )
