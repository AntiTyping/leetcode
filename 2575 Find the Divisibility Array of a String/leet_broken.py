class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = [0] * len(word)

        for i in range(len(word)):
            if int(word[:(i + 1)]) % m == 0:
                ans[i] = 1

        return ans