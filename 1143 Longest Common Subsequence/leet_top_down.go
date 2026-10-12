func longestCommonSubsequence(text1 string, text2 string) int {
    memo := make([][]int, len(text1) + 1)
    for i := range memo {
        memo[i] = make([]int, len(text2) + 1)
        for j := range memo[i] {
            memo[i][j] = -1
        }
    }

    var dp func(i, j int) int

    dp = func(i, j int) int {
        if memo[i][j] > -1 {
            return memo[i][j]
        }
        if i == 0 || j == 0 {
            return 0
        }

        var ans int
        if text1[i - 1] == text2[j - 1] {
            ans = dp(i - 1, j - 1) + 1
        } else {
            ans = slices.Max([]int{dp(i - 1, j), dp(i, j - 1)})
        }
        memo[i][j] = ans
        return ans
    }

    return dp(len(text1), len(text2))
}