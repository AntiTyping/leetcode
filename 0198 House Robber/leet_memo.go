import "slices"
func rob(nums []int) int {
    memo := make(map[int]int)

    var dp func(i int) int

    dp = func (i int) int {
        if v, ok := memo[i]; ok {
            return v
        }
        if i == 0 {
            return nums[0]
        }
        if i == 1 {
            return slices.Max(nums[:2])
        }

        memo[i] = slices.Max([]int{dp(i-1), dp(i-2)+nums[i]})
        return memo[i]
    }

    return dp(len(nums)-1)
}