func rob(nums []int) int {
    memo := make(map[int]int)

    var dp func(int)int

    dp = func(i int) int {
        if i == 0 {
            return nums[0]
        } else if i == 1 {
            return slices.Max(nums[:2])
        } else {
            if _, ok := memo[i]; ok == false {
                p := slices.Max([]int{dp(i-1), dp(i-2)+nums[i]})
                memo[i] = p
            }
            return memo[i]
        }
    }
    return dp(len(nums)-1)
}