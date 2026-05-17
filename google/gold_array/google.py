"""
You're given an array of size 14. You need to determine if the array is "gold".
What does "gold" mean?
You must use all 14 numbers exactly once.

There must be:
1 pair (two identical numbers),
4 sets, where each set is either:
A triplet of identical numbers [x, x, x], OR
A consecutive increasing triplet [x, x+1, x+2].

🧪 Step 2: Try Examples and Work Through
✅ Example 1:

nums = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9]
Let's try to divide this:

Pair: [1, 1]

Set 1: [2, 2, 2] — triplet
Set 2: [3, 3, 3] — triplet
Set 3: [4, 5, 6] — consecutive
Set 4: [7, 8, 9] — consecutive

✅ Yes, this array is "gold".

follow up - So instead of 14 number you are given 13 number ,

You return -1 if you cannot enter any number to make it golden  array, and if you can return the number itself.
"""

nums = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9]

def func1(nums):
    h = {}

    for i in range(len(nums)):
        if nums[i] in h:
            h[nums[i]] += 1
        else:
            h[nums[i]] = 1

    print(h)

    pairs = 0
    triplets = 0

    a = set()

    for k,v in h.items():
        # print(k, v)
        if v == 2:
            pairs += 1
            a.add(k)
        if v == 3:
            triplets += 1
            a.add(k)

    print(a)

    if pairs != 1 and triplets != 2:
        return -1

    c = []
    for i in range(len(nums)):
        if nums[i] not in a:
            c.append(nums[i])
    print(c)

    c.sort()
    if c[2] - c[1] == c[1] - c[0] and c[1] - c[0] == 1 and c[5] - c[4] == c[4] - c[3] and c[4] - c[3] == 1:
        return

func1(nums)


