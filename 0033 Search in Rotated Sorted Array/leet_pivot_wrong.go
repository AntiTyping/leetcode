func search(nums []int, target int) int {
    l, r := 0, len(nums)-1

    for l < r {
        m := l + (r - l) / 2
        if nums[m] > nums[r] {
            l = m + 1
        } else {
            r = m
        }
    }

    pivot := l

    if nums[pivot] <= target && target <= nums[r] {
        l, r = pivot, len(nums)-1
    } else {
        l, r = 0, pivot
    }

    for l <= r {
        m := l + (r - l) / 2
        if nums[m] == target {
            return m
        } else if nums[m] > target {
            r = m - 1
        } else {
            l = m + 1
        }
    }

    return -1
}