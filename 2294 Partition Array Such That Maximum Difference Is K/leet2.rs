impl Solution {
    pub fn partition_array(nums: Vec<i32>, k: i32) -> i32 {
        let mut  nums = nums;
        nums.sort();

        let mut first = nums[0];
        let mut n = 1;
        for &num in &nums[1..] {
            if num > first + k {
                n += 1;
                first = num;
            }
        }

        return n
    }
}