impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut left = 0;
        let mut right = 0;

        while right < nums.len() {
            if nums[right] != val {
                nums[left] = nums[right];
                left += 1;
                right += 1;
            } else {
                right += 1
            }
        }
        return left.try_into().unwrap()
    }
}