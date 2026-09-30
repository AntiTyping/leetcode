impl Solution {
    pub fn reverse_bits(n: i32) -> i32 {
        let mut n = n as u32;
        let mut ans: u32 = 0;
        for _ in 0..31 {
            ans |= (n & 1);
            ans <<= 1;
            n >>= 1;
        }
        ans as i32
    }
}