function longestCommonSubsequence(text1: string, text2: string): number {
    const memo: number[][] = Array.from(
        { length: text1.length + 1 },
        () => new Array(text2.length + 1).fill(-1),
    )

    const dp = (i: number, j: number): number => {
        if (memo[i][j] > -1) {
            return memo[i][j]
        }
        if (i == 0 || j == 0) {
            return 0
        }

        let ans: number
        if (text1[i - 1] == text2[j - 1]) {
            ans = dp(i - 1, j - 1) + 1
        } else {
            ans = Math.max(dp(i - 1, j), dp(i, j - 1))
        }
        memo[i][j] = ans
        return ans
    }

    return dp(text1.length, text2.length)
};