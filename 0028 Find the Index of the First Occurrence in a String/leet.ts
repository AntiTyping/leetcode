function strStr(haystack: string, needle: string): number {
    if (haystack.length < needle.length) {
        return -1
    }

    let left = 0
    let n = needle.length

    while (left <= haystack.length - n) {
        if (haystack.slice(left, left + n) == needle) {
            return left
        }
        left += 1
    }
    return -1
};