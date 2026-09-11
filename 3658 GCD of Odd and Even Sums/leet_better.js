/**
 * @param {number} n
 * @return {number}
 */
var gcdOfOddEvenSums = function(n) {
    const gcd = (x, y) => {
        while (y !== 0) {
            [x, y] = [y, x % y]
        }
        return x
    }
    const sumOdd = n * n
    const sumEven = 2 * n * n + n

    return gcd(sumOdd, sumEven)
};