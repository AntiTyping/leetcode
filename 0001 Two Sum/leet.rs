use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, i32>  = HashMap::new();
        for (i, &n) in nums.iter().enumerate() {
            let diff = target - nums[i];
            if let Some(&j) = seen.get(&diff) {
                return vec![j, i as i32]
            } else {
                seen.insert(n,  i as i32);
            }
        }
        return vec![]
    }
}