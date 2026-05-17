function isPalindrome(s: string): boolean {

    const clean: string[] = []

    for(const ch of s) {
        if (/[a-zA-Z0-9]/.test(ch) == true) {
            clean.push(ch.toLowerCase());
        }
    }
    console.log(clean)
    var left = 0;
    var right = clean.length - 1;

    while(left <= right) {
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