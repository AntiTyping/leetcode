# Why `n & (n-1)` Solves "Number of 1 Bits" (LeetCode 191)

The trick works because **`n & (n-1)` clears the lowest set bit of `n`**, and nothing else. So if you keep applying it until `n` becomes 0, the number of times you loop equals the number of 1 bits.

## Why that single operation clears exactly the lowest 1

Subtracting 1 from a number flips the lowest set bit to 0 and turns every 0 *below* it into a 1. The bits above the lowest set bit are untouched. That's just how borrowing works in binary subtraction — you borrow from the first available 1.

Take `n = 12`:

```
n     = 1100
n - 1  = 1011
```

The lowest set bit was the `1` in the 4s place. After subtracting, that bit became 0 and the two zeros below it became 1s. The leading `1` (the 8s place) stayed put.

Now AND them:

```
  1100
& 1011
------
  1000
```

The lowest set bit got zeroed out, and everything above it survived because those bits were identical in `n` and `n-1`. You went from two 1 bits to one 1 bit — exactly one removed.

## The algorithm

```go
func hammingWeight(n uint32) int {
    count := 0
    for n != 0 {
        n &= n - 1 // drop the lowest set bit
        count++
    }
    return count
}
```

## Why it's better than the naive approach

The win over the naive "shift right and check each bit" approach is that this loops **once per set bit** rather than once per total bit. For a sparse 32-bit number with only 3 ones set, you do 3 iterations instead of 32. Worst case (all bits set) it's the same, but on average it's faster, and it reads nicely.

## Intuition to remember

`n - 1` always produces a "mask" of the form `...1 0000` → `...0 1111` at the boundary of the lowest 1, and ANDing with the original snips off precisely that boundary bit.

This is **Brian Kernighan's algorithm**, and the same `n & (n-1)` shows up in a couple of related problems:

- Checking if a number is a power of two: `n & (n-1) == 0`
- Clearing or isolating lowest bits in general