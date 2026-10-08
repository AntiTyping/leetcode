impl Solution {
    pub fn fib(n: i32) -> i32 {
        let n = n as usize;
        let mut memo = vec![None; n + 1];
        Self::fib_memo(n, &mut memo)
    }

    fn fib_memo(n: usize, memo: &mut [Option<i32>]) -> i32 {
        if n <= 1 {
            return n as i32;
        }
        if let Some(v) = memo[n] {
            return v;
        }
        let v = Self::fib_memo(n - 1, memo) + Self::fib_memo(n - 2, memo);
        memo[n] = Some(v);
        v
    }
}