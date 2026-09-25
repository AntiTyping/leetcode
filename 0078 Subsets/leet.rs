impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = Vec::new();
        let mut curr: Vec<i32> = Vec::new();

        fn bt(start: usize, nums: &Vec<i32>, ans: &mut Vec<Vec<i32>>, curr: &mut Vec<i32>) {
            ans.push(curr.clone());
            for i in start..nums.len() {
                curr.push(nums[i]);
                bt(i + 1, nums, ans, curr);
                curr.pop();
            }
        };

        bt(0, &nums, &mut ans, &mut curr);

        ans
    }
}