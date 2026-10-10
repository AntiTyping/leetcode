function rob(nums: number[]): number {
    // const memo = new Array(nums.length).fill(-1);

    // const dp = (n: number): number => {
    //     if (memo[n] > -1) {
    //         return memo[n];
    //     }
    //     if (n == 0) {
    //         return nums[0];
    //     }
    //     if (n == 1) {
    //         return Math.max(...nums.slice(0, 2));
    //     }
    //     memo[n] = Math.max(dp(n-1), dp(n-2)+nums[n]);
    //     return memo[n];
    // }
    // return dp(nums.length-1)
    const dp = Array(nums.length).fill(0);

    dp[0] = nums[0];
    dp[1] = Math.max(...nums.slice(0,2));

    for (let i = 2; i < nums.length; i++) {
        dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i])
    }

    return dp[nums.length-1]
};