class Solution {
    func gcdOfOddEvenSums(_ n: Int) -> Int {
        func gcd(_ x: Int, _ y: Int) -> Int {
            var (a, b) = (x, y)
            while b != 0 {
                (a, b) = (b, a % b);
            }
            return a
        }
        return gcd(n*n, 2*n*n+n)
    }
}