class Solution {
    fun gcdOfOddEvenSums(n: Int): Int {
        fun gcd(x: Int, y: Int): Int {
            var a = x
            var b = y
            while (b != 0) {
                a = b.also { b = a % b }
            }
            return a
        }
        return gcd(n * n, 2 * n * n + n)
    }
}