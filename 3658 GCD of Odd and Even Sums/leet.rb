# @param {Integer} n
# @return {Integer}
def gcd_of_odd_even_sums(n)
    def gcd(x, y)
        while y != 0
            x, y = y, x % y
        end
        x
    end

    gcd(n * n, 2 * n * n + n)
end