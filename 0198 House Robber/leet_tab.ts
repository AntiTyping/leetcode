function rob(nums: number[]): number {
    const dp = new Array<number>()

    dp[0] = nums[0]
    dp[1] = Math.max(...nums.slice(0, 2))

    for(let i = 2; i < nums.length; i++) {
        dp[i] = Math.max(dp[i-1], dp[i-2]+nums[i])
    }

    return dp[dp.length-1]
};