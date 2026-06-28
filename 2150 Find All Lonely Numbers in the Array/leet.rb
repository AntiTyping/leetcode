# @param {Integer[]} nums
# @return {Integer[]}
def find_lonely(nums)
    seen = Hash.new(0)

    nums.each do |n|
        seen[n] += 1
    end

    out = []
    nums.each do |n|
        if !seen.key?(n - 1) && !seen.key?(n + 1) && seen[n] == 1
            out << n
        end
    end
    out
end