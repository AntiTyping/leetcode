
import "slices"
func minCostClimbingStairs(cost []int) int {
    memo := make(map[int]int)
    var dp func(n int) int
    dp = func(n int) int {
        if v, ok := memo[n]; ok == true {
            return v
        }
        if n <= 1 {
            return 0
        }
        memo[n] = slices.Min([]int{dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2]})
        return memo[n]
    }

    return dp(len(cost))
}