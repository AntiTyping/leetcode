/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let left = 0
    let right = 0

    while (right < nums.length) {
        if (nums[left] === nums[right]) {
            right++
        } else {
            left++
            nums[left] = nums[right]
            right++
        }
    }
    return left + 1
};