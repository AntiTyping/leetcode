impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n < 1 {
            return 0;
        }
        let n = n as usize;
        let mut memo = vec![0; n + 1];
        memo[1] = 1;
        for i in 2..=n {
            memo[i] = memo[i-1] + memo[i-2]
        }
        return memo[n]
    }
}