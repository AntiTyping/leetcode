function minCostClimbingStairs(cost: number[]): number {
    // const memo = new Map<number, number>()
    // const dp = (n: number): number => {
    //     if (memo.has(n)) {
    //         return memo.get(n)
    //     }
    //     if (n < 2) {
    //         return 0
    //     }
    //     memo.set(n, Math.min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2]))
    //     return memo.get(n)
    // }

    // return dp(cost.length)
    const n = cost.length;
    const dp: number[] = new Array(n + 1).fill(0)

    for (let i = 2; i <= n; i++) {
        dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    }

    return dp[n]
}