# LeetCode 424: Longest Repeating Character Replacement

## Optimal Python Solution

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        best = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            max_freq = max(max_freq, count[ch])

            # Replacements needed = window size - most frequent character count
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
```

## Explanation

Use a sliding window to track the longest substring that can be converted into a string of the same character using at most `k` replacements.

For any current window:

```python
window_length = right - left + 1
replacements_needed = window_length - max_freq
```

Where `max_freq` is the frequency of the most common character in the current window.

If:

```python
replacements_needed > k
```

then the window is invalid, so move `left` forward until the window becomes valid again.

## Complexity

- Time complexity: `O(n)`
- Space complexity: `O(1)` because the input contains only uppercase English letters
