func gcdOfOddEvenSums(n int) int {
    sumOdd := n * n
    sumEven := 2 * n * n + n

    gcd := func(x, y int) int {
        for y != 0 {
            x, y = y, x % y
        }
        return x
    }

    return gcd(sumOdd, sumEven)
}