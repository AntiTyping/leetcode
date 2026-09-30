# @param {Integer} n
# @return {Integer}
def reverse_bits(n)
    ans = 0
    (0..30).each do
        ans |= (n & 1)
        ans <<= 1
        n >>= 1
    end
    ans
end