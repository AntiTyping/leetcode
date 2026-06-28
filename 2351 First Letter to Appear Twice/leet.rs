use std::collections::HashSet;

impl Solution {
    pub fn repeated_character(s: String) -> char {
        let mut seen = HashSet::new();
        for c in s.chars() {
            if !seen.insert(c) {
                return c;
            }
        }
        unreachable!()
    }
}