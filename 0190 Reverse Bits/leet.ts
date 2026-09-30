function reverseBits(n: number): number {
    let ans = 0
    for (let i = 0; i < 31; i++) {
        ans = ans | (n & 1)
        ans = ans << 1
        n = n >> 1
    }
    return ans
};