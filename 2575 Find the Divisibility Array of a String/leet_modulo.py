class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = [0] * len(word)

        curr = int(word[0])
        if curr % m == 0:
            ans[0] = 1
        for i in range(1, len(word)):
            curr = curr * 10 + int(word[i])
            if curr % m == 0:
                ans[i] = 1
            curr %= m
        return ans