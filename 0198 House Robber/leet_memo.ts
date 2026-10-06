function rob(nums: number[]): number {
    const memo = new Map<number, number>()

    const dp = (i: number): number => {
        if (memo[i] != undefined) {
            return memo[i]
        }
        if (i == 0) {
            return nums[0];
        }
        if (i == 1) {
            return Math.max(...nums.slice(0, 2))
        }
        memo[i] = Math.max(dp(i - 1), dp(i-2)+nums[i])
        return memo[i]
    }
    return dp(nums.length-1)
};