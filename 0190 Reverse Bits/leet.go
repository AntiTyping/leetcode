func reverseBits(n int) int {
    var ans = 0
    for i := 0; i < 31; i++ {
        ans |= (n & 1)
        ans <<= 1
        n >>= 1
    }
    return ans
}