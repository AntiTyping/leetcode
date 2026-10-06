impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut memo = vec![-1i32; n];
        Self::rob_rec(nums.len()-1, &nums, &mut memo)
    }

    fn rob_rec(i: usize, nums: &Vec<i32>, memo: &mut Vec<i32>) -> i32 {
        if i == 0 { return nums[0]; }
        if i == 1 { return nums[0].max(nums[1]); }
        if memo[i] != -1 { return memo[i]; }
        memo[i] = Self::rob_rec(i - 1, nums, memo).max(Self::rob_rec(i - 2, nums, memo) + nums[i]);
        return memo[i]
    }
}