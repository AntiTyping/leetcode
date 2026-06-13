# Longest Repeating Character Replacement (LeetCode 424)

Given a string `s` and an integer `k`, find the length of the longest substring you can make all-identical by replacing **at most `k`** characters.

## Optimal Solution

```python
def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_freq = 0
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        # replacements needed = window_size - count of most frequent char
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result
```

## Core Idea

A window is **valid** when:

```
window_size - max_freq <= k
```

`window_size - max_freq` is exactly the number of characters you'd have to replace to make the whole window uniform. If that count fits within your replacement budget `k`, the window is achievable.

## Why It's O(n), Not O(26n)

The non-obvious part: **`max_freq` is never decremented**, even after the window slides and it becomes "stale."

That's fine because `result` only ever grows when you find a window with a genuinely higher `max_freq`. A stale `max_freq` can't produce a false larger answer — it just means the window slides forward (left and right advance together) without recording a new max. You never lose the true best.

## Why `if` Instead of `while`

Each outer iteration adds exactly one character on the right, so the window can need to shrink by at most one. The window only ever grows or shifts — it never actually contracts below its historical max size.

## Complexity

| Metric | Value |
|--------|-------|
| Time   | O(n) |
| Space  | O(1) — the count map holds at most 26 uppercase letters |

## Worth Internalizing

The naive instinct is to recompute `max_freq` over the whole map on each shrink. Skipping that recomputation is the whole trick — reason through why it's safe and the solution clicks.