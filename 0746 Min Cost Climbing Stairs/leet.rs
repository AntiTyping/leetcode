use std::collections::HashMap;
use std::cmp::min;

impl Solution {
    // pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
    //     Self::dp(cost.len(), &cost)
    // }

    // fn dp(n: usize, cost: &[i32]) -> i32 {
    //     use std::cmp::min;

    //     if n < 2 {
    //         return 0
    //     }
    //     return min(Self::dp(n-1, cost) + cost[n-1], Self::dp(n-2, cost)+cost[n-2])
    // }
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut memo = HashMap::new();

        Self::dp(cost.len(), &cost, &mut memo)
    }

    fn dp(n: usize, cost: &[i32], memo: &mut HashMap<i32, i32>) -> i32 {
        if let Some(&v) = memo.get(&(n as i32)) {
            return v
        }

        if n < 2 {
            return 0
        }
        let v = min(
            Self::dp(n - 1, cost, memo) + cost[n - 1],
            Self::dp(n - 2, cost, memo) + cost[n - 2]
        );
        memo.insert(n as i32, v);

        return v
    }
}