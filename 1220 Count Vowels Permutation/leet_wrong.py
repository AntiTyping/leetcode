class Solution:
    def countVowelPermutation(self, n: int) -> int:
        v = list('aeiou')
        m = 10 ** 9 + 7

        @lru_cache(40000)
        def dp(s):
            i = len(s)
            if i == n:
                return 1;

            if s[i - 1] == "a":
                return dp(s + "e") % m
            if s[i - 1] == "e":
                return (dp(s + "a") + dp(s + "i")) % m
            if s[i - 1] == "i":
                su = 0
                for j in range(len(v)):
                    if v[j] != "i":
                        su += dp(s + v[j]) % m
                return su
            if s[i - 1] == "o":
                return (dp(s + "i") + dp(s + "u")) % m
            if s[i - 1] == "u":
                return dp(s + "a") % m

        su = 0
        for u in v:
            su += dp(u)

        return su

