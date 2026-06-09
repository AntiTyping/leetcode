impl Solution {
    pub fn partition_array(nums: Vec<i32>, k: i32) -> i32 {
        let mut  nums = nums;
        nums.sort();

        let mut first = nums[0];
        let mut n = 1;
        for i in 1..nums.len() {
            if nums[i] > first + k {
                n += 1;
                first = nums[i];
            }
        }

        return n
    }
}