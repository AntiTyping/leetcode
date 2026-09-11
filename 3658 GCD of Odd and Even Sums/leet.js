/**
 * @param {number} n
 * @return {number}
 */
var gcdOfOddEvenSums = function(n) {
    let sumOdd = n * n
    let sumEven = 2 * n * n + n

    return function(x, y) {
        while (y != 0) {
            [x, y] = [y, x % y]
        }
        return x
    }(sumOdd, sumEven)
};