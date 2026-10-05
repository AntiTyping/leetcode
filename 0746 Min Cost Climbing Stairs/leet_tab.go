
import "slices"
func minCostClimbingStairs(cost []int) int {
    dp := make([]int, len(cost) + 1)

    for i := 2; i < len(cost) + 1; i++ {
        dp[i] = slices.Min([]int{dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]})
    }
    return dp[len(dp)-1]
}