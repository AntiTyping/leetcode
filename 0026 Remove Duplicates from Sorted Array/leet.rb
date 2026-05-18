# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    left = 0
    right = 0

    puts right

    while right < nums.size
        if nums[left] == nums[right]
            right = right + 1
        else
            left = left + 1
            nums[left] = nums[right]
            right =right + 1
        end
    end

    left + 1
end

puts remove_duplicates([1,1,2])