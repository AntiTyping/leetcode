function isPalindrome(s: string): boolean {

    var left = 0;
    const clean = s.toLowerCase().replace(/[^a-z0-9]/g, "")
    var right = clean.length - 1;

    while(left < right) {
        if (clean[left] != clean[right]) {
            return false
        }
        left += 1
        right -= 1
    }
    return true
};

console.log(isPalindrome("race a car"))
console.log(isPalindrome("A man, a plan, a canal: Panama"))