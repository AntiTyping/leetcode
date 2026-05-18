impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = 0;

        while (right < nums.len()) {
            if (nums[left] == nums[right]) {
                right += 1;
            } else {
                left += 1;
                nums[left] = nums[right];
                right +=1;
            }
        }
        return (left + 1).try_into().unwrap()
    }
}