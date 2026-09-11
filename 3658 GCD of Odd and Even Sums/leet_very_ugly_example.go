import "math"

func gcdOfOddEvenSums(n int) int {
    sumOdd := math.Pow(float64(n), float64(2))
    sumEven := 2.0 * math.Pow(float64(n), float64(2)) + float64(n)

    gcd := func(x, y int) int {
        for y != 0 {
            x, y = y, x % y
        }
        return x
    }

    return gcd(int(sumOdd), int(sumEven))
}