impl Solution {
    pub fn gcd_of_odd_even_sums(n: i32) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }

            return a
        }
        let sumEven = n * n;
        let sumOdd = 2 * n * n + n;

        return gcd(sumEven, sumOdd);
    }
}