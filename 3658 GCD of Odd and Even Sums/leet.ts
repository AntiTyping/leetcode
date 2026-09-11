function gcdOfOddEvenSums(n: number): number {
    const gcd = (x: number , y: number): number => {
        while (y !== 0) {
            [x, y] = [y, x % y]
        }
        return x;
    }

    return gcd(n * n, 2 * n * n + n);
};