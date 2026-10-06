impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        Self::rob_rec(nums.len()-1, &nums)
    }

    fn rob_rec(i: usize, nums: &Vec<i32>) -> i32 {
        if i == 0 { return nums[0]; }
        if i == 1 { return nums[0].max(nums[1]); }
        Self::rob_rec(i - 1, nums).max(Self::rob_rec(i - 2, nums) + nums[i])
    }
}