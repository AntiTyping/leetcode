function rob(nums: number[]): number {
    const dp = (i: number): number => {
        if (i == 0) {
            return nums[0];
        }
        if (i == 1) {
            return Math.max(...nums.slice(0, 2))
        }
        return Math.max(dp(i - 1), dp(i-2)+nums[i])
    }
    return dp(nums.length-1)
};